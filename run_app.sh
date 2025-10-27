#!/bin/bash

# Streamlit Cheat Sheet Runner for macOS/Linux
# ============================================

set -e  # Exit on any error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

echo "🚀 Starting Streamlit Cheat Sheet..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    print_error "Virtual environment not found!"
    echo "Please run setup.sh first to create the environment."
    exit 1
fi

# Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    print_error "Streamlit not found in virtual environment!"
    echo "Please run setup.sh to install dependencies."
    exit 1
fi

print_success "Environment ready!"
echo
print_status "Starting Streamlit application..."
echo
echo "🌐 The app will be available at: http://localhost:8501"
echo "📱 Mobile-friendly and responsive design"
echo "⚡ Press Ctrl+C to stop the application"
echo

# Try to open browser (works on macOS and most Linux systems)
if command -v open &> /dev/null; then
    # macOS
    (sleep 3; open http://localhost:8501) &
elif command -v xdg-open &> /dev/null; then
    # Linux
    (sleep 3; xdg-open http://localhost:8501) &
fi

# Run the Streamlit app
streamlit run streamlit_cheatsheet.py