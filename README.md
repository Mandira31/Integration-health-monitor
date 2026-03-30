# Enterprise Integration Health Monitor

A real-time monitoring dashboard for tracking the health and performance of critical API integrations. Built to demonstrate operational systems thinking, API integration skills, and deployment monitoring capabilities.

## What This Demonstrates

This project showcases skills directly relevant to **deployment specialist**, **implementation engineer**, and **solutions consultant** roles:

- **API Integration**: Connects to multiple third-party status APIs and handles different response formats
- **Error Handling**: Gracefully handles timeouts, network failures, and API changes
- **Monitoring Logic**: Implements health check logic with status classification (healthy/degraded/down)
- **Real-time Dashboards**: Provides stakeholder-facing visibility into system health
- **Production Thinking**: Uses industry-standard patterns for monitoring critical integrations

## Features

- ✅ Real-time health monitoring for 4 major APIs (GitHub, Stripe, OpenAI, Datadog)
- ✅ Response time tracking in milliseconds
- ✅ Visual status indicators (green/yellow/red)
- ✅ Auto-refresh every 60 seconds
- ✅ Manual refresh on demand
- ✅ Error logging and display
- ✅ Clean, professional dashboard UI

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **APIs**: RESTful status endpoints from GitHub, Stripe, OpenAI, Datadog

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Quick Start (Demo Mode)

To run the app with simulated data (useful for demonstrations or network-restricted environments):

```bash
# Make the script executable (first time only)
chmod +x run_demo.sh

# Run in demo mode
./run_demo.sh
```

Or manually:
```bash
export DEMO_MODE=true
python app.py
```

### Production Mode (Real API Calls)

1. Clone this repository or download the files

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

The app will automatically check API health every 60 seconds.

## How It Works

### Backend (`app.py`)
- Defines 4 APIs to monitor using their public status endpoints
- `check_api_health()` function sends GET requests and measures response times
- Classifies each service as healthy/degraded/down based on response
- Stores results in memory (production version would use a database)
- Exposes Flask routes for the dashboard and API endpoints

### Frontend (`templates/dashboard.html`)
- Displays real-time status for all monitored services
- Shows summary metrics (total healthy, degraded, down)
- Auto-refreshes every 60 seconds
- Provides manual refresh button
- Color-coded status badges for quick visibility

## Use Cases

This monitoring pattern is used in production for:

1. **Post-Deployment Validation**: Confirm integrations are working after new releases
2. **Customer Health Dashboards**: Give enterprise customers visibility into their integrations
3. **SLA Monitoring**: Track uptime and response times for service-level agreements
4. **Incident Detection**: Alert teams when critical integrations fail
5. **Vendor Accountability**: Monitor third-party API reliability

## Extending This Project

Potential enhancements for production use:

- [ ] Add database (PostgreSQL/SQLite) to store historical health data
- [ ] Implement alerting (email/Slack notifications when services go down)
- [ ] Add authentication for multi-tenant deployments
- [ ] Create charts showing uptime trends over time
- [ ] Add more APIs relevant to specific business needs
- [ ] Implement retry logic with exponential backoff
- [ ] Add webhook support for real-time status updates

## Real-World Application

In deployment/implementation roles, I would use this pattern to:

- Monitor customer-specific integrations during onboarding
- Provide customers with real-time health dashboards post-deployment
- Proactively detect integration failures before customers report issues
- Track SLA compliance for enterprise contracts
- Document integration reliability in quarterly business reviews

## Author

**Mandira**  
MS Business Analytics | Simon Business School, University of Rochester  
Seeking deployment strategist, implementation specialist, and solutions consulting roles

**Skills Demonstrated**: API integration, error handling, monitoring systems, stakeholder dashboards, Python/Flask, production thinking

---

*Built as a portfolio project to demonstrate technical deployment and implementation capabilities.*
