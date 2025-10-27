# Deployment Guide

This guide covers various ways to deploy your Streamlit Cheat Sheet application.

## Table of Contents

- [Local Development](#local-development)
- [Docker Deployment](#docker-deployment)
- [Streamlit Cloud](#streamlit-cloud)
- [Heroku](#heroku)
- [Railway](#railway)
- [Render](#render)
- [DigitalOcean App Platform](#digitalocean-app-platform)
- [AWS EC2](#aws-ec2)
- [Environment Variables](#environment-variables)

## Local Development

### Quick Start (Windows)
```bash
# Double-click run_app.bat or run in terminal:
.\run_app.bat
```

### Quick Start (macOS/Linux)
```bash
# Make executable and run:
chmod +x setup.sh run_app.sh
./setup.sh
./run_app.sh
```

### Manual Setup
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run streamlit_cheatsheet.py
```

## Docker Deployment

### Using Docker Compose (Recommended)
```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d --build

# Stop the application
docker-compose down
```

### Using Docker directly
```bash
# Build the image
docker build -t streamlit-cheatsheet .

# Run the container
docker run -p 8501:8501 streamlit-cheatsheet

# Run in background
docker run -d -p 8501:8501 --name cheatsheet streamlit-cheatsheet

# Stop the container
docker stop cheatsheet
docker rm cheatsheet
```

## Streamlit Cloud

### Prerequisites
- GitHub account
- Repository pushed to GitHub

### Steps
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set main file path: `streamlit_cheatsheet.py`
6. Click "Deploy"

### Configuration
Create `.streamlit/secrets.toml` for sensitive data:
```toml
[secrets]
api_key = "your-secret-api-key"
```

## Heroku

### Prerequisites
- Heroku account
- Heroku CLI installed

### Files needed
Create these files in your project root:

**Procfile:**
```
web: sh setup.sh && streamlit run streamlit_cheatsheet.py --server.port=$PORT --server.address=0.0.0.0
```

**setup.sh:**
```bash
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

### Deployment Steps
```bash
# 1. Login to Heroku
heroku login

# 2. Create app
heroku create your-app-name

# 3. Deploy
git push heroku main

# 4. Open app
heroku open
```

## Railway

### Steps
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will auto-detect Python and deploy

### Configuration
Add environment variables in Railway dashboard:
- `PORT`: 8501
- `PYTHONPATH`: /app

## Render

### Steps
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New Web Service"
4. Connect your repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run streamlit_cheatsheet.py --server.port=$PORT --server.address=0.0.0.0`

## DigitalOcean App Platform

### Steps
1. Go to [cloud.digitalocean.com](https://cloud.digitalocean.com)
2. Create new App
3. Connect GitHub repository
4. Configure:
   - **Source Directory**: `/`
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `streamlit run streamlit_cheatsheet.py --server.port=$PORT --server.address=0.0.0.0`

## AWS EC2

### Prerequisites
- AWS account
- EC2 instance running Ubuntu/Amazon Linux

### Steps
```bash
# 1. Connect to EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# 2. Update system
sudo apt update && sudo apt upgrade -y

# 3. Install Python and pip
sudo apt install python3 python3-pip git -y

# 4. Clone repository
git clone https://github.com/hakkache/Streamlit_cheatsheet.git
cd Streamlit_cheatsheet

# 5. Install dependencies
pip3 install -r requirements.txt

# 6. Run with nohup (background process)
nohup streamlit run streamlit_cheatsheet.py --server.port=8501 --server.address=0.0.0.0 &

# 7. Configure security group to allow port 8501
```

### Using PM2 (Process Manager)
```bash
# Install PM2
sudo npm install -g pm2

# Create ecosystem file
cat > ecosystem.config.js << EOL
module.exports = {
  apps: [{
    name: 'streamlit-cheatsheet',
    script: 'streamlit',
    args: 'run streamlit_cheatsheet.py --server.port=8501 --server.address=0.0.0.0',
    interpreter: 'python3',
    env: {
      PYTHONPATH: '.'
    }
  }]
}
EOL

# Start with PM2
pm2 start ecosystem.config.js

# Save PM2 configuration
pm2 save
pm2 startup
```

## Environment Variables

### Common Environment Variables
```bash
# Streamlit specific
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Python specific
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1

# Application specific
APP_ENV=production
DEBUG=false
```

### Setting Environment Variables

#### Local (.env file)
```bash
# Create .env file
STREAMLIT_SERVER_PORT=8501
APP_ENV=development
```

#### Heroku
```bash
heroku config:set STREAMLIT_SERVER_PORT=8501
```

#### Docker
```bash
# In docker-compose.yml
environment:
  - STREAMLIT_SERVER_PORT=8501
  - APP_ENV=production
```

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Find process using port 8501
lsof -i :8501  # macOS/Linux
netstat -ano | findstr :8501  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

**Memory issues:**
- Increase container memory limits
- Optimize data loading with caching
- Use pagination for large datasets

**Slow loading:**
- Enable Streamlit caching
- Optimize imports
- Use lazy loading for heavy components

**Permission denied:**
```bash
# Fix file permissions
chmod +x setup.sh run_app.sh
```

### Performance Optimization

1. **Enable caching:**
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv('data.csv')
   ```

2. **Optimize imports:**
   ```python
   # Import only what you need
   from pandas import DataFrame
   ```

3. **Use session state wisely:**
   ```python
   if 'data' not in st.session_state:
       st.session_state.data = load_data()
   ```

## Monitoring and Logging

### Health Checks
```python
# Add to your app
def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}
```

### Logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Application started")
```

## Security Best Practices

1. **Environment Variables**: Never commit secrets to git
2. **HTTPS**: Always use HTTPS in production
3. **Authentication**: Add authentication for sensitive apps
4. **Input Validation**: Validate all user inputs
5. **Rate Limiting**: Implement rate limiting for APIs

## Support

For deployment issues:
1. Check the [Streamlit documentation](https://docs.streamlit.io)
2. Review platform-specific guides
3. Check application logs
4. Open an issue on GitHub

Happy deploying! 🚀