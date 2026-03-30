#!/bin/bash

# Start the Integration Health Monitor in demo mode
echo "Starting Integration Health Monitor in DEMO MODE..."
echo "Demo mode uses mock data to simulate API responses"
echo ""
echo "To run with REAL API calls (requires unrestricted network):"
echo "  python app.py"
echo ""
echo "Dashboard will be available at: http://localhost:5000"
echo ""

export DEMO_MODE=true
python3 app.py
