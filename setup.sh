#!/bin/bash

# Streamlit Cheat Sheet Setup Script for macOS/Linux
# ==================================================

set -e  # Exit on any error

echo "========================================"
echo "   Streamlit Cheat Sheet Setup"
echo "========================================"
echo

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
print_status "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        print_error "Python is not installed or not in PATH"
        echo "Please install Python from https://python.org"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
print_success "Python $PYTHON_VERSION found"

# Check if version is 3.8+
PYTHON_MAJOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.major)")
PYTHON_MINOR=$($PYTHON_CMD -c "import sys; print(sys.version_info.minor)")

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    print_error "Python 3.8+ is required. Found Python $PYTHON_VERSION"
    exit 1
fi

print_status "[1/5] Python version check passed"
echo

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_status "[2/5] Creating virtual environment..."
    $PYTHON_CMD -m venv venv
    if [ $? -ne 0 ]; then
        print_error "Failed to create virtual environment"
        exit 1
    fi
    print_success "Virtual environment created successfully!"
else
    print_status "[2/5] Virtual environment already exists, skipping creation..."
fi
echo

# Activate virtual environment
print_status "[3/5] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    print_error "Failed to activate virtual environment"
    exit 1
fi
print_success "Virtual environment activated!"
echo

# Upgrade pip
print_status "[4/5] Upgrading pip..."
python -m pip install --upgrade pip --quiet
print_success "Pip upgraded successfully!"
echo

# Install requirements
print_status "[5/5] Installing required packages..."
pip install -r requirements.txt --quiet
if [ $? -ne 0 ]; then
    print_error "Failed to install requirements"
    exit 1
fi
print_success "All packages installed successfully!"
echo

echo "========================================"
echo "     Setup completed successfully!"
echo "========================================"
echo
print_success "🎉 Your Streamlit Cheat Sheet is ready to run!"
echo
echo "To start the application:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the app: streamlit run streamlit_cheatsheet.py"
echo
echo "Or simply run: ./run_app.sh"
echo
echo "The app will be available at: http://localhost:8501"
echo "Press Ctrl+C to stop the application."
echo

# Ask if user wants to start the app now
read -p "Would you like to start the application now? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_status "Starting Streamlit application..."
    echo
    echo "🚀 Opening http://localhost:8501 in your browser..."
    echo "📱 The app is mobile-friendly and works on all devices!"
    echo "⚡ Use Ctrl+C to stop the application when you're done."
    echo
    
    # Try to open browser (works on macOS and most Linux systems)
    if command -v open &> /dev/null; then
        # macOS
        (sleep 3; open http://localhost:8501) &
    elif command -v xdg-open &> /dev/null; then
        # Linux
        (sleep 3; xdg-open http://localhost:8501) &
    fi
    
    streamlit run streamlit_cheatsheet.py
fi