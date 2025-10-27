# Streamlit App Configuration
# ===========================

import streamlit as st

# App metadata
APP_TITLE = "Complete Streamlit Cheat Sheet"
APP_ICON = "📊"
APP_VERSION = "2.0"
APP_DESCRIPTION = "Your ultimate reference for building amazing Streamlit applications"

# Theme colors
COLORS = {
    "primary": "#ff6b6b",
    "secondary": "#4ecdc4", 
    "accent": "#45b7d1",
    "success": "#51cf66",
    "warning": "#ffd43b",
    "error": "#ff6b6b",
    "info": "#74c0fc"
}

# Layout settings
LAYOUT_CONFIG = {
    "wide_mode": True,
    "initial_sidebar_state": "expanded",
    "menu_items": {
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': f"# {APP_TITLE} v{APP_VERSION}\n{APP_DESCRIPTION}"
    }
}

# Custom CSS styles
CUSTOM_CSS = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root variables */
    :root {
        --primary-color: #ff6b6b;
        --secondary-color: #4ecdc4;
        --accent-color: #45b7d1;
        --success-color: #51cf66;
        --warning-color: #ffd43b;
        --error-color: #ff6b6b;
        --info-color: #74c0fc;
        --text-color: #262730;
        --bg-color: #ffffff;
        --card-bg: #f8f9fa;
        --border-radius: 12px;
        --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        --transition: all 0.3s ease;
    }
    
    /* Main app styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        font-family: 'Inter', sans-serif;
    }
    
    /* Headers */
    .main-header {
        font-size: 3.5rem;
        color: var(--primary-color);
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .section-header {
        font-size: 2.2rem;
        color: var(--secondary-color);
        border-bottom: 3px solid var(--secondary-color);
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
        font-weight: 600;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 0;
        width: 50px;
        height: 3px;
        background: var(--primary-color);
    }
    
    .subsection-header {
        font-size: 1.5rem;
        color: var(--accent-color);
        margin: 1.5rem 0 0.8rem 0;
        font-weight: 500;
    }
    
    /* Cards and containers */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        margin: 1rem 0;
        border-left: 5px solid var(--secondary-color);
        transition: var(--transition);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(255,107,107,0.02) 0%, rgba(78,205,196,0.02) 100%);
        pointer-events: none;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid var(--info-color);
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .tip-box {
        background: linear-gradient(135deg, #fff8e1 0%, #fce4ec 100%);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid var(--warning-color);
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #ffebee 0%, #fce4ec 100%);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid var(--error-color);
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Code blocks */
    .code-block {
        background: linear-gradient(135deg, #263238 0%, #37474f 100%);
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
        font-family: 'Fira Code', monospace;
        position: relative;
        overflow-x: auto;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        transition: var(--transition);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Metrics styling */
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        text-align: center;
        transition: var(--transition);
        border-top: 4px solid var(--secondary-color);
    }
    
    .metric-container:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, var(--primary-color) 0%, var(--accent-color) 100%);
        color: white;
        border-radius: var(--border-radius);
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: var(--border-radius);
        color: white;
        text-align: center;
        margin-top: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.1;
        pointer-events: none;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--accent-color) 100%);
        border-radius: 10px;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        padding: 0.5rem 1rem;
        transition: var(--transition);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: var(--secondary-color);
        color: white;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        border-radius: var(--border-radius);
        border: 2px solid transparent;
        transition: var(--transition);
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: var(--secondary-color);
        box-shadow: 0 0 0 2px rgba(78, 205, 196, 0.2);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border-radius: var(--border-radius);
        border: 2px solid transparent;
        transition: var(--transition);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--secondary-color);
        box-shadow: 0 0 0 2px rgba(78, 205, 196, 0.2);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate-fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.5rem;
        }
        
        .section-header {
            font-size: 1.8rem;
        }
        
        .feature-card {
            padding: 1rem;
        }
    }
</style>
"""

# JavaScript for enhanced functionality
CUSTOM_JS = """
<script>
    // Add smooth scrolling
    document.documentElement.style.scrollBehavior = 'smooth';
    
    // Add intersection observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, observerOptions);
    
    // Observe all feature cards
    setTimeout(() => {
        document.querySelectorAll('.feature-card').forEach(card => {
            observer.observe(card);
        });
    }, 100);
    
    // Add copy to clipboard functionality
    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(() => {
            // Show success message
            const toast = document.createElement('div');
            toast.textContent = 'Copied to clipboard!';
            toast.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: #51cf66;
                color: white;
                padding: 1rem;
                border-radius: 8px;
                z-index: 1000;
                animation: slideInRight 0.3s ease-out;
            `;
            document.body.appendChild(toast);
            
            setTimeout(() => {
                toast.remove();
            }, 2000);
        });
    }
    
    // Add slide in animation for toast
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
    `;
    document.head.appendChild(style);
</script>
"""

def apply_custom_css():
    """Apply custom CSS to the Streamlit app"""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    st.markdown(CUSTOM_JS, unsafe_allow_html=True)

def configure_page():
    """Configure the Streamlit page with custom settings"""
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="wide" if LAYOUT_CONFIG["wide_mode"] else "centered",
        initial_sidebar_state=LAYOUT_CONFIG["initial_sidebar_state"],
        menu_items=LAYOUT_CONFIG["menu_items"]
    )
