import requests
import time
import json
import random
from datetime import datetime
from zoneinfo import ZoneInfo
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# APIs to monitor - using public status pages
APIS = {
    'GitHub': 'https://www.githubstatus.com/api/v2/status.json',
    'Stripe': 'https://status.stripe.com/api/v2/status.json',
    'OpenAI': 'https://status.openai.com/api/v2/status.json',
    'Datadog': 'https://status.datadoghq.com/api/v2/status.json'
}

# Demo mode flag - set to True if running in restricted network environment
DEMO_MODE = os.getenv('DEMO_MODE', 'false').lower() == 'true'

# Store check results in memory (in production, use a database)
health_data = {
    'last_check': None,
    'results': {}
}

def check_api_health(name, url):
    """Check a single API's health and return status"""
    # Demo mode for environments with network restrictions
    if DEMO_MODE:
        return generate_mock_health_data(name)
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = round((time.time() - start_time) * 1000, 2)  # Convert to ms
        
        # Determine status based on response
<<<<<<< HEAD
        if response.status_code == 200:
            data = response.json()
            # Most status APIs return an 'indicator' field
            indicator = data.get('status', {}).get('indicator', 'unknown')
            
            if indicator == 'none':
                status = 'healthy'
            elif indicator in ['minor', 'maintenance']:
                status = 'degraded'
            else:
                status = 'down'
        else:
            status = 'down'
=======
         error = None

if response.status_code == 200:
    data = response.json()
    indicator = data.get('status', {}).get('indicator', 'unknown')

    if indicator == 'none':
        status = 'healthy'
    elif indicator in ['minor', 'maintenance']:
        status = 'degraded'
    else:
        status = 'down'

elif 400 <= response.status_code < 500:
    status = 'unknown'
    error = f"Monitoring endpoint error: {response.status_code}"

elif 500 <= response.status_code < 600:
    status = 'down'
    error = f"Server error: {response.status_code}"
>>>>>>> e166e7a (fix status logic and handle 404 correctly)
            
        return {
            'status': status,
            'response_time_ms': response_time,
            'status_code': response.status_code,
            'last_checked': datetime.now().isoformat(),
<<<<<<< HEAD
            'error': None
=======
            'error': error
>>>>>>> e166e7a (fix status logic and handle 404 correctly)
        }
    except requests.exceptions.Timeout:
        return {
            'status': 'down',
            'response_time_ms': None,
            'status_code': None,
            'last_checked': datetime.now().isoformat(),
            'error': 'Request timeout'
        }
    except Exception as e:
        return {
            'status': 'down',
            'response_time_ms': None,
            'status_code': None,
            'last_checked': datetime.now().isoformat(),
            'error': str(e)
        }

def generate_mock_health_data(name):
    """Generate realistic mock data for demo purposes"""
    # Simulate realistic response times and occasional issues
    statuses = ['healthy', 'healthy', 'healthy', 'degraded', 'healthy']  # 80% healthy
    status = random.choice(statuses)
    
    if status == 'healthy':
        response_time = random.randint(50, 300)
        status_code = 200
        error = None
    elif status == 'degraded':
        response_time = random.randint(500, 2000)
        status_code = 200
        error = None
    else:
        response_time = None
        status_code = None
        error = 'Service unavailable'
    
    return {
        'status': status,
        'response_time_ms': response_time,
        'status_code': status_code,
        'last_checked': datetime.now(ZoneInfo("America/New_York")).isoformat(),
        'error': error
    }

def run_health_checks():
    """Run health checks for all APIs"""
    results = {}
    for name, url in APIS.items():
        results[name] = check_api_health(name, url)
    
    health_data['last_check'] = datetime.now(ZoneInfo("America/New_York")).isoformat()
    health_data['results'] = results
    return results

@app.route('/')
def dashboard():
    """Render the main dashboard"""
    return render_template('dashboard.html')

@app.route('/api/health')
def get_health():
    """API endpoint to get current health status"""
    # Run fresh checks
    run_health_checks()
    return jsonify(health_data)

@app.route('/api/check')
def manual_check():
    """Trigger a manual health check"""
    results = run_health_checks()
    return jsonify({'success': True, 'results': results})

if __name__ == '__main__':
    # Run initial check on startup
    run_health_checks()
    # Start the Flask app
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
