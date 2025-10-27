import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, date, time
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io
import json
import requests
import altair as alt

# Page configuration
st.set_page_config(
    page_title="Streamlit Cheat Sheet",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        font-size: 3.5rem;
        color: #ff6b6b;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .section-header {
        font-size: 2.2rem;
        color: #4ecdc4;
        border-bottom: 3px solid #4ecdc4;
        padding-bottom: 0.5rem;
        margin: 2rem 0 1rem 0;
        font-weight: 600;
    }
    
    .subsection-header {
        font-size: 1.5rem;
        color: #45b7d1;
        margin: 1.5rem 0 0.8rem 0;
        font-weight: 500;
    }
    
    /* Code blocks */
    .code-block {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
    }
    
    /* Info boxes */
    .tip-box {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #ff9500;
    }
    
    .info-box {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #17a2b8;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #dc3545;
    }
    
    /* Cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 5px solid #4ecdc4;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-top: 3rem;
    }
    
    /* Metrics styling */
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Title with modern styling
st.markdown('<h1 class="main-header">🚀 Complete Streamlit Cheat Sheet</h1>', unsafe_allow_html=True)

# Create a modern hero section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; color: white; margin-bottom: 2rem;'>
        <h3>Your Ultimate Streamlit Reference Guide</h3>
        <p>🎯 Interactive examples • 📊 Live demonstrations • 💡 Best practices</p>
        <p><strong>Latest Update:</strong> July 2025 | <strong>Streamlit Version:</strong> 1.28+</p>
    </div>
    """, unsafe_allow_html=True)

# Quick stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📚 Sections", "15", "3 new")
with col2:
    st.metric("🔧 Features", "120+", "25 added")
with col3:
    st.metric("💻 Examples", "80+", "15 new")
with col4:
    st.metric("⭐ Rating", "5.0", "Perfect")

st.markdown("---")

# Enhanced sidebar navigation with modern design
st.sidebar.markdown("""
<div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 10px; color: white; margin-bottom: 1rem;'>
    <h2>🧭 Navigation</h2>
    <p>Choose a section to explore</p>
</div>
""", unsafe_allow_html=True)

sections = [
    "🏠 Overview & Getting Started",
    "📝 Basic Elements",
    "✍️ Text & Markdown", 
    "📊 Data Display",
    "🎛️ Input Widgets",
    "🎨 Media Elements",
    "📐 Layout & Containers",
    "📈 Charts & Plots",
    "⚡ Progress & Status",
    "🔄 Control Flow",
    "💾 Session State",
    "📁 File Operations",
    "🚀 Advanced Features",
    "🎭 Styling & Theming",
    "🔧 Performance & Optimization"
]

selected_section = st.sidebar.selectbox("Choose a section:", sections)

# Sidebar additional info
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
            padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
    <h4>💡 Quick Tips</h4>
    <ul>
        <li>Each section has live examples</li>
        <li>Copy code snippets directly</li>
        <li>Try interactive widgets</li>
        <li>Check the source code</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Resource links
st.sidebar.markdown("""
<div style='background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); 
            padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
    <h4>🔗 Useful Resources</h4>
    <p><a href='https://docs.streamlit.io' target='_blank'>📖 Official Docs</a></p>
    <p><a href='https://streamlit.io/gallery' target='_blank'>🎨 App Gallery</a></p>
    <p><a href='https://discuss.streamlit.io' target='_blank'>💬 Community Forum</a></p>
    <p><a href='https://github.com/streamlit/streamlit' target='_blank'>🐙 GitHub Repo</a></p>
</div>
""", unsafe_allow_html=True)

# Main content based on selection
if selected_section == "🏠 Overview & Getting Started":
    st.markdown('<h2 class="section-header">🏠 Overview & Getting Started</h2>', unsafe_allow_html=True)
    
    # Welcome section
    st.markdown("""
    <div class='info-box'>
        <h3>🎉 Welcome to the Ultimate Streamlit Cheat Sheet!</h3>
        <p>This comprehensive guide covers everything you need to know about building amazing web applications with Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # What is Streamlit
    st.subheader("🤔 What is Streamlit?")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Streamlit is an open-source Python library that makes it easy to create and share beautiful, 
        custom web apps for machine learning and data science. In just a few minutes you can build 
        and deploy powerful data apps.
        
        **Key Features:**
        - 🚀 **Fast Development**: Build apps in pure Python
        - 🎨 **Beautiful UI**: Professional-looking apps with minimal code
        - 📊 **Data-Friendly**: Built-in support for pandas, numpy, plotly
        - 🔄 **Live Updates**: Automatic rerun when code changes
        - 🌐 **Easy Deployment**: Deploy to Streamlit Cloud with one click
        """)
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <h4>📈 Why Choose Streamlit?</h4>
            <ul>
                <li>No HTML/CSS/JS required</li>
                <li>Pythonic and intuitive</li>
                <li>Great for prototyping</li>
                <li>Active community</li>
                <li>Extensive widget library</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Installation
    st.subheader("⚙️ Installation & Setup")
    
    tab1, tab2, tab3 = st.tabs(["💻 Installation", "🚀 First App", "📁 Project Structure"])
    
    with tab1:
        st.markdown("**Install Streamlit using pip:**")
        st.code("pip install streamlit", language='bash')
        
        st.markdown("**Or with conda:**")
        st.code("conda install -c conda-forge streamlit", language='bash')
        
        st.markdown("**Verify installation:**")
        st.code("streamlit hello", language='bash')
        
        st.info("💡 This will open a demo app in your browser!")
    
    with tab2:
        st.markdown("**Create your first Streamlit app:**")
        st.code("""
# hello_streamlit.py
import streamlit as st

st.title("My First Streamlit App! 🎉")
st.write("Hello, World!")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Add some data
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10)
})

st.line_chart(data.set_index('x'))
        """, language='python')
        
        st.markdown("**Run your app:**")
        st.code("streamlit run hello_streamlit.py", language='bash')
    
    with tab3:
        st.markdown("**Recommended project structure:**")
        st.code("""
my_streamlit_app/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .streamlit/
│   ├── config.toml       # App configuration
│   └── secrets.toml      # API keys and secrets
├── data/                 # Data files
├── components/           # Custom components
├── utils/               # Utility functions
└── README.md           # Documentation
        """, language='text')
        
        st.info("💡 Use this structure for larger applications to keep your code organized!")
    
    # Quick Start Checklist
    st.subheader("✅ Quick Start Checklist")
    
    checklist_items = [
        "Install Streamlit (`pip install streamlit`)",
        "Create your first app file (e.g., `app.py`)",
        "Add basic elements (title, text, widgets)",
        "Run your app (`streamlit run app.py`)",
        "Explore the documentation",
        "Join the Streamlit community"
    ]
    
    for i, item in enumerate(checklist_items):
        if st.checkbox(item, key=f"checklist_{i}"):
            st.success(f"✅ {item}")
    
    # Useful Commands
    st.subheader("🛠️ Useful Commands")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Development Commands:**
        ```bash
        streamlit run app.py        # Run your app
        streamlit run app.py --server.port 8502  # Custom port
        streamlit hello            # Demo app
        streamlit config show      # Show config
        streamlit cache clear      # Clear cache
        ```
        """)
    
    with col2:
        st.markdown("""
        **Debugging Commands:**
        ```bash
        streamlit run app.py --logger.level debug
        streamlit run app.py --server.headless true
        streamlit run app.py --runner.magicEnabled false
        streamlit run app.py --global.developmentMode true
        ```
        """)

elif selected_section == "📝 Basic Elements":
    st.markdown('<h2 class="section-header">Basic Elements</h2>', unsafe_allow_html=True)
    
    # Title and headers
    st.subheader("Titles and Headers")
    code_example = '''
# In your Streamlit app:
st.title("Main Title")
st.header("Header")
st.subheader("Subheader")
st.caption("This is a caption")
'''
    st.code(code_example, language='python')
    
    # Example output
    st.markdown("**Example Output:**")
    st.title("Main Title")
    st.header("Header") 
    st.subheader("Subheader")
    st.caption("This is a caption")
    
    # Write and text
    st.subheader("Text Display")
    code_example = '''
st.write("Hello, World!")
st.text("Fixed width text")
st.markdown("**Bold** and *italic* text")
st.latex(r'\\sum_{i=1}^{n} x_i^2')
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    st.write("Hello, World!")
    st.text("Fixed width text")
    st.markdown("**Bold** and *italic* text")
    st.latex(r'\sum_{i=1}^{n} x_i^2')

elif selected_section == "✍️ Text & Markdown":
    st.markdown('<h2 class="section-header">Text & Markdown</h2>', unsafe_allow_html=True)
    
    st.subheader("Markdown Formatting")
    code_example = '''
# Headers
st.markdown("# H1 Header")
st.markdown("## H2 Header") 
st.markdown("### H3 Header")

# Text formatting
st.markdown("**Bold text**")
st.markdown("*Italic text*")
st.markdown("~~Strikethrough~~")
st.markdown("`Inline code`")

# Lists
st.markdown("""
- Bullet point 1
- Bullet point 2
  - Nested point
  
1. Numbered item 1
2. Numbered item 2
""")

# Links and images
st.markdown("[Link text](https://streamlit.io)")
st.markdown("![Alt text](image_url)")
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    st.markdown("# H1 Header")
    st.markdown("## H2 Header")
    st.markdown("### H3 Header")
    st.markdown("**Bold text**")
    st.markdown("*Italic text*")
    st.markdown("~~Strikethrough~~")
    st.markdown("`Inline code`")
    
    st.markdown("""
- Bullet point 1
- Bullet point 2
  - Nested point
  
1. Numbered item 1
2. Numbered item 2
""")

elif selected_section == "📊 Data Display":
    st.markdown('<h2 class="section-header">📊 Data Display</h2>', unsafe_allow_html=True)
    
    # Create sample data
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin'],
        'Salary': [50000, 60000, 70000, 55000, 65000],
        'Department': ['IT', 'HR', 'Finance', 'Marketing', 'IT'],
        'Start Date': pd.date_range('2020-01-01', periods=5, freq='6M')
    })
    
    st.subheader("📋 DataFrames and Tables")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 DataFrame", "📋 Table", "✏️ Data Editor", "🎛️ Column Config"])
    
    with tab1:
        code_example = '''
# Interactive DataFrame with search, sort, and filter
st.dataframe(
    df,
    use_container_width=True,    # Fill container width
    hide_index=True,             # Hide row index
    height=300                   # Fixed height
)

# DataFrame with custom styling
st.dataframe(
    df.style.highlight_max(axis=0),  # Highlight max values
    use_container_width=True
)
'''
        st.code(code_example, language='python')
        
        st.markdown("**Interactive DataFrame:**")
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("**Styled DataFrame:**")
        st.dataframe(
            df.style.highlight_max(axis=0).format({'Salary': '${:,.0f}'}),
            use_container_width=True
        )
    
    with tab2:
        code_example = '''
# Static table (no interaction)
st.table(df)

# Table with subset of data
st.table(df.head(3))
'''
        st.code(code_example, language='python')
        
        st.markdown("**Static Table:**")
        st.table(df.head(3))
    
    with tab3:
        code_example = '''
# Editable table
edited_df = st.data_editor(
    df,
    num_rows="dynamic",          # Allow adding/deleting rows
    use_container_width=True,
    column_config={
        "Salary": st.column_config.NumberColumn(
            "Salary ($)",
            help="Annual salary in USD",
            min_value=0,
            max_value=200000,
            step=1000,
            format="$%d"
        ),
        "Start Date": st.column_config.DateColumn(
            "Start Date",
            min_value=date(2020, 1, 1),
            max_value=date(2025, 12, 31),
            format="DD/MM/YYYY"
        )
    }
)
'''
        st.code(code_example, language='python')
        
        st.markdown("**Editable Table:**")
        edited_df = st.data_editor(
            df.copy(),
            num_rows="dynamic",
            use_container_width=True,
            key="data_editor_1"
        )
    
    with tab4:
        st.markdown("**Advanced Column Configuration:**")
        code_example = '''
# Column configuration examples
column_config = {
    "Name": st.column_config.TextColumn(
        "Full Name",
        help="Employee full name",
        max_chars=50,
        validate="^[A-Za-z ]+$"  # Only letters and spaces
    ),
    "Salary": st.column_config.NumberColumn(
        "Annual Salary",
        help="Salary in USD",
        min_value=0,
        max_value=200000,
        step=1000,
        format="$%d"
    ),
    "City": st.column_config.SelectboxColumn(
        "Office Location",
        help="Primary office location",
        options=["New York", "London", "Tokyo", "Paris", "Berlin"]
    ),
    "Department": st.column_config.SelectboxColumn(
        "Department",
        options=["IT", "HR", "Finance", "Marketing", "Sales"]
    )
}

st.data_editor(df, column_config=column_config)
'''
        st.code(code_example, language='python')
    
    st.subheader("📊 Metrics and KPIs")
    
    # Enhanced metrics section
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_salary = df['Salary'].mean()
        salary_change = int(np.random.choice([-1, 1]) * np.random.randint(1000, 5000))
        st.metric(
            label="💰 Average Salary",
            value=f"${avg_salary:,.0f}",
            delta=f"${salary_change:,}",
            delta_color="normal"
        )
    
    with col2:
        total_employees = len(df)
        emp_change = int(np.random.choice([-1, 1]) * np.random.randint(1, 3))
        st.metric(
            label="👥 Total Employees",
            value=total_employees,
            delta=emp_change,
            delta_color="normal"
        )
    
    with col3:
        avg_age = df['Age'].mean()
        age_change = round(np.random.uniform(-0.5, 0.5), 1)
        st.metric(
            label="📅 Average Age",
            value=f"{avg_age:.1f} years",
            delta=f"{age_change:+.1f}",
            delta_color="off"
        )
    
    with col4:
        departments = df['Department'].nunique()
        st.metric(
            label="🏢 Departments",
            value=departments,
            delta="1 new",
            delta_color="normal"
        )
    
    # Advanced metrics code
    code_example = '''
# Advanced metrics with custom styling
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Revenue",
        value="$1.2M",
        delta="15.3%",
        delta_color="normal",  # "normal", "inverse", or "off"
        help="Total revenue this quarter"
    )

with col2:
    st.metric(
        label="Users",
        value="1,234",
        delta="-2.1%",
        delta_color="inverse"  # Red when negative is good
    )

with col3:
    st.metric(
        label="Conversion",
        value="23.4%",
        delta="1.2%",
        delta_color="off"  # No color for delta
    )
'''
    st.code(code_example, language='python')
    
    st.subheader("📈 JSON Display")
    
    sample_json = {
        "user": {
            "id": 123,
            "name": "John Doe",
            "email": "john@example.com",
            "preferences": {
                "theme": "dark",
                "notifications": True,
                "language": "en"
            }
        },
        "metadata": {
            "created": "2025-01-01",
            "last_login": "2025-07-09",
            "login_count": 42
        }
    }
    
    code_example = '''
# Display JSON data
import json

data = {
    "user": {"id": 123, "name": "John Doe"},
    "preferences": {"theme": "dark", "notifications": True}
}

st.json(data)  # Pretty-printed JSON
'''
    st.code(code_example, language='python')
    
    st.markdown("**JSON Output:**")
    st.json(sample_json)

elif selected_section == "🎛️ Input Widgets":
    st.markdown('<h2 class="section-header">🎛️ Input Widgets</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📝 Text Input", "🔢 Numbers", "🎯 Selection", "📅 Date/Time", "🎨 Advanced"])
    
    with tab1:
        st.subheader("Text Input Widgets")
        code_example = '''
# Text inputs
name = st.text_input(
    "Full Name:",
    placeholder="Enter your full name",
    help="This will be displayed on your profile"
)

message = st.text_area(
    "Message:",
    placeholder="Type your message here...",
    height=100,
    max_chars=500
)

password = st.text_input(
    "Password:",
    type="password",
    help="Password must be at least 8 characters"
)

# Text input with validation
email = st.text_input(
    "Email Address:",
    placeholder="user@example.com"
)
if email and "@" not in email:
    st.error("Please enter a valid email address")
'''
        st.code(code_example, language='python')
        
        st.markdown("**Try it out:**")
        name = st.text_input("Full Name:", placeholder="Enter your full name")
        message = st.text_area("Message:", placeholder="Type your message here...", height=100, max_chars=500)
        password = st.text_input("Password:", type="password")
        
        if name:
            st.success(f"Hello, {name}!")
        if message:
            st.info(f"Message length: {len(message)}/500 characters")
    
    with tab2:
        st.subheader("Number Input Widgets")
        code_example = '''
# Number inputs
age = st.number_input(
    "Age:",
    min_value=0,
    max_value=120,
    value=25,
    step=1,
    help="Your current age"
)

price = st.number_input(
    "Price ($):",
    min_value=0.0,
    value=100.0,
    step=0.01,
    format="%.2f"
)

# Slider variations
rating = st.slider(
    "Rating:",
    min_value=1,
    max_value=5,
    value=3,
    step=1,
    format="%d ⭐"
)

temperature = st.slider(
    "Temperature (°C):",
    min_value=-50.0,
    max_value=50.0,
    value=20.0,
    step=0.5
)

# Range slider
price_range = st.slider(
    "Price Range ($):",
    min_value=0,
    max_value=1000,
    value=(200, 800),
    step=50
)
'''
        st.code(code_example, language='python')
        
        st.markdown("**Try it out:**")
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age:", min_value=0, max_value=120, value=25)
            rating = st.slider("Rating:", 1, 5, 3, format="%d ⭐")
        with col2:
            price = st.number_input("Price ($):", min_value=0.0, value=100.0, step=0.01, format="%.2f")
            price_range = st.slider("Price Range ($):", 0, 1000, (200, 800))
        
        if age > 0:
            st.info(f"You are {age} years old with a {rating}⭐ rating")
    
    with tab3:
        st.subheader("Selection Widgets")
        code_example = '''
# Selection widgets
country = st.selectbox(
    "Country:",
    ["USA", "Canada", "UK", "Germany", "France", "Japan"],
    index=0,  # Default selection
    help="Select your country"
)

languages = st.multiselect(
    "Programming Languages:",
    ["Python", "JavaScript", "Java", "C++", "Go", "Rust"],
    default=["Python"],  # Default selections
    help="Select all languages you know"
)

experience = st.radio(
    "Experience Level:",
    ["Beginner", "Intermediate", "Advanced", "Expert"],
    horizontal=True,  # Horizontal layout
    help="Your current skill level"
)

newsletter = st.checkbox(
    "Subscribe to newsletter",
    value=True,  # Default checked
    help="Receive updates and news"
)

# Advanced selection
framework = st.selectbox(
    "Favorite Framework:",
    ["Streamlit", "Flask", "Django", "FastAPI"],
    format_func=lambda x: f"🚀 {x}"  # Custom display format
)
'''
        st.code(code_example, language='python')
        
        st.markdown("**Try it out:**")
        col1, col2 = st.columns(2)
        with col1:
            country = st.selectbox("Country:", ["USA", "Canada", "UK", "Germany", "France", "Japan"])
            experience = st.radio("Experience:", ["Beginner", "Intermediate", "Advanced"], horizontal=True)
        with col2:
            languages = st.multiselect("Languages:", ["Python", "JavaScript", "Java", "C++"], default=["Python"])
            newsletter = st.checkbox("Subscribe to newsletter", value=True)
        
        if languages:
            st.success(f"You selected: {', '.join(languages)}")
    
    with tab4:
        st.subheader("Date and Time Widgets")
        code_example = '''
# Date and time inputs
birth_date = st.date_input(
    "Birth Date:",
    value=date(1990, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    help="Your date of birth"
)

appointment_time = st.time_input(
    "Appointment Time:",
    value=time(9, 0),  # 9:00 AM
    help="Preferred appointment time"
)

# Date range
vacation_dates = st.date_input(
    "Vacation Period:",
    value=[date.today(), date.today() + pd.Timedelta(days=7)],
    help="Select start and end dates"
)

# Datetime (requires datetime object)
from datetime import datetime
event_datetime = st.date_input(
    "Event Date:",
    value=datetime.now().date()
)
event_time = st.time_input(
    "Event Time:",
    value=datetime.now().time()
)
'''
        st.code(code_example, language='python')
        
        st.markdown("**Try it out:**")
        col1, col2 = st.columns(2)
        with col1:
            birth_date = st.date_input("Birth Date:", value=date(1990, 1, 1))
            event_time = st.time_input("Event Time:", value=time(9, 0))
        with col2:
            vacation_dates = st.date_input("Vacation Period:", value=[date.today(), date.today() + pd.Timedelta(days=7)])
        
        if isinstance(vacation_dates, list) and len(vacation_dates) == 2:
            duration = (vacation_dates[1] - vacation_dates[0]).days
            st.info(f"Vacation duration: {duration} days")
    
    with tab5:
        st.subheader("Advanced Input Widgets")
        code_example = '''
# Color picker
favorite_color = st.color_picker(
    "Favorite Color:",
    "#ff6b6b",  # Default color
    help="Pick your favorite color"
)

# File uploader with multiple types
uploaded_files = st.file_uploader(
    "Upload Files:",
    type=['txt', 'csv', 'json', 'png', 'jpg'],
    accept_multiple_files=True,
    help="Drag and drop files here"
)

# Camera input (for mobile/webcam)
camera_photo = st.camera_input(
    "Take a photo:",
    help="Use your camera to take a photo"
)

# Audio input
audio_file = st.audio_input(
    "Record audio:",
    help="Record a voice message"
)
'''
        st.code(code_example, language='python')
        
        st.markdown("**Try it out:**")
        col1, col2 = st.columns(2)
        with col1:
            favorite_color = st.color_picker("Favorite Color:", "#ff6b6b")
            st.markdown(f"""
            <div style='background: {favorite_color}; padding: 1rem; border-radius: 10px; color: white; text-align: center;'>
                <h4>Your Color Choice</h4>
                <p>{favorite_color}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            uploaded_files = st.file_uploader("Upload Files:", type=['txt', 'csv', 'json'], accept_multiple_files=True)
            if uploaded_files:
                st.success(f"Uploaded {len(uploaded_files)} file(s)!")
                for file in uploaded_files:
                    st.write(f"📁 {file.name} ({file.size} bytes)")
    
    # Widget states and callbacks
    st.subheader("🔧 Widget States and Callbacks")
    
    code_example = '''
# Widget with callback
def on_text_change():
    st.session_state.text_changed = True
    st.write("Text was changed!")

user_input = st.text_input(
    "Type something:",
    on_change=on_text_change,
    key="text_input_with_callback"
)

# Disable widgets conditionally
enable_widgets = st.checkbox("Enable advanced options")

advanced_option = st.selectbox(
    "Advanced Option:",
    ["Option 1", "Option 2", "Option 3"],
    disabled=not enable_widgets  # Disable if checkbox is unchecked
)

# Widget with session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Increment"):
        st.session_state.counter += 1
with col2:
    if st.button("Decrement"):
        st.session_state.counter -= 1
with col3:
    if st.button("Reset"):
        st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")
'''
    st.code(code_example, language='python')
    
    st.markdown("**Try it out:**")
    enable_widgets = st.checkbox("Enable advanced options")
    advanced_option = st.selectbox(
        "Advanced Option:",
        ["Option 1", "Option 2", "Option 3"],
        disabled=not enable_widgets
    )
    
    if enable_widgets:
        st.success(f"Selected: {advanced_option}")

elif selected_section == "🎨 Media Elements":
    st.markdown('<h2 class="section-header">Media Elements</h2>', unsafe_allow_html=True)
    
    st.subheader("Images")
    code_example = '''
# Display images
st.image("image.jpg", caption="Image caption", width=300)

# From PIL Image
from PIL import Image
img = Image.open("image.jpg")
st.image(img, caption="PIL Image")

# From URL
st.image("https://example.com/image.jpg")
'''
    st.code(code_example, language='python')
    
    # Create a sample image
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title("Sample Plot")
    
    # Convert to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    
    st.markdown("**Example Output:**")
    st.image(img, caption="Generated sample image", width=400)
    plt.close()
    
    st.subheader("Audio and Video")
    code_example = '''
# Audio
st.audio("audio.mp3")

# Video  
st.video("video.mp4")

# From URL
st.video("https://example.com/video.mp4")
'''
    st.code(code_example, language='python')

elif selected_section == "📐 Layout & Containers":
    st.markdown('<h2 class="section-header">Layout & Containers</h2>', unsafe_allow_html=True)
    
    st.subheader("Columns")
    code_example = '''
# Create columns
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Column 1")
    
with col2:
    st.write("Column 2")
    
with col3:
    st.write("Column 3")

# Different column widths
col1, col2 = st.columns([2, 1])  # 2:1 ratio
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("Column 1")
    with col2:
        st.success("Column 2")
    with col3:
        st.warning("Column 3")
    
    st.subheader("Containers and Expansions")
    code_example = '''
# Container
with st.container():
    st.write("This is inside a container")
    
# Expander
with st.expander("Click to expand"):
    st.write("Hidden content here")
    
# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Content of tab 1")
with tab2:
    st.write("Content of tab 2")
with tab3:
    st.write("Content of tab 3")
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    with st.expander("Click to expand"):
        st.write("This is hidden content that appears when expanded!")
    
    tab1, tab2, tab3 = st.tabs(["📈 Chart", "📋 Data", "🗃 Config"])
    with tab1:
        st.write("Chart content would go here")
    with tab2:
        st.write("Data content would go here")
    with tab3:
        st.write("Configuration options would go here")

elif selected_section == "📈 Charts & Plots":
    st.markdown('<h2 class="section-header">Charts & Plots</h2>', unsafe_allow_html=True)
    
    # Generate sample data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.subheader("Built-in Charts")
    code_example = '''
import pandas as pd
import numpy as np

# Sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Line chart
st.line_chart(chart_data)

# Area chart  
st.area_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Scatter chart
st.scatter_chart(chart_data)
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Line Chart:")
        st.line_chart(chart_data)
        st.write("Bar Chart:")
        st.bar_chart(chart_data.head(5))
    with col2:
        st.write("Area Chart:")
        st.area_chart(chart_data)
        st.write("Scatter Chart:")
        st.scatter_chart(chart_data.head(10))
    
    st.subheader("Plotly Charts")
    code_example = '''
import plotly.express as px
import plotly.graph_objects as go

# Plotly Express
fig = px.scatter(df, x="Age", y="Salary", color="City")
st.plotly_chart(fig)

# Plotly Graph Objects
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13]))
st.plotly_chart(fig)
'''
    st.code(code_example, language='python')
    
    # Create sample plotly chart
    df_plot = pd.DataFrame({
        'x': range(10),
        'y': np.random.randn(10).cumsum(),
        'category': ['A'] * 5 + ['B'] * 5
    })
    
    fig = px.line(df_plot, x='x', y='y', color='category', title="Sample Plotly Chart")
    st.plotly_chart(fig)

elif selected_section == "⚡ Progress & Status":
    st.markdown('<h2 class="section-header">Progress & Status</h2>', unsafe_allow_html=True)
    
    st.subheader("Progress Indicators")
    code_example = '''
import time

# Progress bar
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)

# Spinner
with st.spinner('Loading...'):
    time.sleep(3)
    
# Status messages
st.success("Success message!")
st.info("Info message!")
st.warning("Warning message!")
st.error("Error message!")
st.exception(Exception("This is an exception"))
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    if st.button("Show Progress Bar"):
        import time as time_module  # Import locally to avoid conflict
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time_module.sleep(0.01)
    
    st.success("✅ Success message!")
    st.info("ℹ️ Info message!")
    st.warning("⚠️ Warning message!")
    st.error("❌ Error message!")
    
    st.subheader("Balloons and Snow")
    code_example = '''
# Celebration effects
st.balloons()  # Show balloons animation
st.snow()      # Show snow animation
'''
    st.code(code_example, language='python')
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎈 Balloons"):
            st.balloons()
    with col2:
        if st.button("❄️ Snow"):
            st.snow()

elif selected_section == "🔄 Control Flow":
    st.markdown('<h2 class="section-header">Control Flow</h2>', unsafe_allow_html=True)
    
    st.subheader("Stopping Execution")
    code_example = '''
# Stop execution with message
st.stop()

# Stop execution conditionally
if not user_authenticated:
    st.error("Please log in first")
    st.stop()
'''
    st.code(code_example, language='python')
    
    st.subheader("Rerun and Buttons")
    code_example = '''
# Button that triggers rerun
if st.button("Refresh Data"):
    # Code to refresh data
    st.rerun()

# Form to group inputs
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Hello {name}, you are {age} years old")
'''
    st.code(code_example, language='python')
    
    st.markdown("**Try it out:**")
    with st.form("demo_form"):
        name_form = st.text_input("Name")
        age_form = st.number_input("Age", min_value=0, max_value=120)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(f"Hello {name_form}, you are {age_form} years old!")

elif selected_section == "💾 Session State":
    st.markdown('<h2 class="section-header">Session State</h2>', unsafe_allow_html=True)
    
    st.subheader("Managing State")
    code_example = '''
# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Update session state
if st.button("Increment"):
    st.session_state.counter += 1

# Display session state
st.write(f"Counter: {st.session_state.counter}")

# Delete from session state
if st.button("Reset"):
    del st.session_state.counter
    st.rerun()
'''
    st.code(code_example, language='python')
    
    st.markdown("**Try it out:**")
    if 'demo_counter' not in st.session_state:
        st.session_state.demo_counter = 0
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Increment"):
            st.session_state.demo_counter += 1
    with col2:
        if st.button("➖ Decrement"):
            st.session_state.demo_counter -= 1
    with col3:
        if st.button("🔄 Reset"):
            st.session_state.demo_counter = 0
    
    st.write(f"Counter value: **{st.session_state.demo_counter}**")
    
    st.subheader("Callbacks")
    code_example = '''
# Callback function
def on_change():
    st.write("Input changed!")

# Widget with callback
text = st.text_input("Type something:", on_change=on_change)

# Using session state in callbacks
def increment_counter():
    st.session_state.counter += 1

st.button("Click me", on_click=increment_counter)
'''
    st.code(code_example, language='python')

elif selected_section == "📁 File Operations":
    st.markdown('<h2 class="section-header">File Operations</h2>', unsafe_allow_html=True)
    
    st.subheader("File Upload")
    code_example = '''
# Single file upload
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read file
    bytes_data = uploaded_file.read()
    st.write("Filename:", uploaded_file.name)

# Multiple files
uploaded_files = st.file_uploader(
    "Choose files", 
    accept_multiple_files=True
)

# Specific file types
csv_file = st.file_uploader(
    "Upload CSV", 
    type=['csv']
)
if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.dataframe(df)
'''
    st.code(code_example, language='python')
    
    st.markdown("**Try it out:**")
    uploaded_file = st.file_uploader("Choose a file (demo)")
    if uploaded_file is not None:
        st.success(f"File uploaded: {uploaded_file.name}")
        st.write(f"File size: {len(uploaded_file.read())} bytes")
    
    st.subheader("File Download")
    code_example = '''
# Download button
csv_data = df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="data.csv",
    mime="text/csv"
)

# Download different file types
import json
json_data = json.dumps({"key": "value"})
st.download_button(
    label="Download JSON",
    data=json_data,
    file_name="data.json",
    mime="application/json"
)
'''
    st.code(code_example, language='python')
    
    st.markdown("**Try it out:**")
    sample_data = pd.DataFrame({
        'Column1': [1, 2, 3],
        'Column2': ['A', 'B', 'C']
    })
    csv_data = sample_data.to_csv(index=False)
    st.download_button(
        label="📥 Download Sample CSV",
        data=csv_data,
        file_name="sample_data.csv",
        mime="text/csv"
    )

elif selected_section == "🚀 Advanced Features":
    st.markdown('<h2 class="section-header">Advanced Features</h2>', unsafe_allow_html=True)
    
    st.subheader("Caching")
    code_example = '''
# Cache data loading
@st.cache_data
def load_data():
    # Expensive data loading operation
    return pd.read_csv("large_file.csv")

# Cache resource (like database connections)
@st.cache_resource  
def init_model():
    # Load ML model
    return load_model("model.pkl")

# Clear cache
st.cache_data.clear()
st.cache_resource.clear()
'''
    st.code(code_example, language='python')
    
    st.subheader("Custom Components")
    code_example = '''
# HTML component
st.components.v1.html("""
<div style="background-color: lightblue; padding: 10px;">
    <h3>Custom HTML Component</h3>
    <p>This is custom HTML content</p>
</div>
""", height=200)

# IFrame
st.components.v1.iframe("https://example.com", height=400)
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    st.components.v1.html("""
    <div style="background-color: lightblue; padding: 10px; border-radius: 5px;">
        <h3>🎨 Custom HTML Component</h3>
        <p>This is custom HTML content embedded in Streamlit!</p>
    </div>
    """, height=120)
    
    st.subheader("Secrets Management")
    code_example = '''
# Access secrets from .streamlit/secrets.toml
api_key = st.secrets["api_key"]
db_password = st.secrets["database"]["password"]

# Check if secret exists
if "optional_key" in st.secrets:
    optional_value = st.secrets["optional_key"]
'''
    st.code(code_example, language='python')
    
    st.subheader("Configuration")
    code_example = '''
# .streamlit/config.toml file example:
[theme]
primaryColor = "#ff6b6b"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"

[server]
port = 8501
maxUploadSize = 1028
'''
    st.code(code_example, language='toml')

elif selected_section == "🎭 Styling & Theming":
    st.markdown('<h2 class="section-header">🎭 Styling & Theming</h2>', unsafe_allow_html=True)
    
    st.subheader("🎨 Custom CSS")
    code_example = '''
# Add custom CSS
st.markdown("""
<style>
    .big-font {
        font-size: 30px !important;
        color: #ff6b6b;
    }
    .highlight-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ff6b6b;
    }
</style>
""", unsafe_allow_html=True)

# Use custom CSS classes
st.markdown('<p class="big-font">Big Red Text!</p>', unsafe_allow_html=True)
st.markdown('<div class="highlight-box">Highlighted content</div>', unsafe_allow_html=True)
'''
    st.code(code_example, language='python')
    
    st.markdown("**Example Output:**")
    st.markdown("""
    <style>
        .big-font {
            font-size: 30px !important;
            color: #ff6b6b;
        }
        .highlight-box {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 10px;
            border-left: 5px solid #ff6b6b;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Big Red Text!</p>', unsafe_allow_html=True)
    st.markdown('<div class="highlight-box">Highlighted content in a custom box</div>', unsafe_allow_html=True)
    
    st.subheader("🌈 Color Schemes")
    color_schemes = {
        "Ocean Blue": {"primary": "#0066cc", "secondary": "#4da6ff", "background": "#f0f8ff"},
        "Sunset Orange": {"primary": "#ff6b35", "secondary": "#f7931e", "background": "#fff8f0"},
        "Forest Green": {"primary": "#2d5a27", "secondary": "#40826d", "background": "#f0fff0"},
        "Purple Gradient": {"primary": "#667eea", "secondary": "#764ba2", "background": "#f8f9ff"},
        "Rose Gold": {"primary": "#e8b4b8", "secondary": "#c9a96e", "background": "#fdf8f8"}
    }
    
    selected_scheme = st.selectbox("Choose a color scheme:", list(color_schemes.keys()))
    scheme = color_schemes[selected_scheme]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style='background: {scheme["primary"]}; padding: 1rem; border-radius: 10px; color: white; text-align: center;'>
            <h4>Primary Color</h4>
            <p>{scheme["primary"]}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style='background: {scheme["secondary"]}; padding: 1rem; border-radius: 10px; color: white; text-align: center;'>
            <h4>Secondary Color</h4>
            <p>{scheme["secondary"]}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div style='background: {scheme["background"]}; padding: 1rem; border-radius: 10px; color: #333; text-align: center; border: 1px solid #ddd;'>
            <h4>Background Color</h4>
            <p>{scheme["background"]}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("🎯 Theme Configuration")
    st.markdown("Create a `.streamlit/config.toml` file for custom theming:")
    
    config_example = f'''
[theme]
primaryColor = "{scheme["primary"]}"
backgroundColor = "{scheme["background"]}"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
headless = false

[browser]
gatherUsageStats = false
'''
    st.code(config_example, language='toml')
    
    if st.button("💾 Download Theme Config"):
        st.download_button(
            label="Download config.toml",
            data=config_example,
            file_name="config.toml",
            mime="text/plain"
        )

elif selected_section == "🔧 Performance & Optimization":
    st.markdown('<h2 class="section-header">🔧 Performance & Optimization</h2>', unsafe_allow_html=True)
    
    st.subheader("⚡ Caching Strategies")
    
    tab1, tab2, tab3 = st.tabs(["📊 @st.cache_data", "🔗 @st.cache_resource", "🧹 Cache Management"])
    
    with tab1:
        st.markdown("**Use `@st.cache_data` for data processing:**")
        code_example = '''
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    """Cache expensive data loading operations"""
    return pd.read_csv(file_path)

@st.cache_data
def process_data(df):
    """Cache data transformations"""
    return df.groupby('category').sum()

@st.cache_data(ttl=60*60)  # Cache for 1 hour
def fetch_api_data(api_url):
    """Cache API calls with TTL"""
    response = requests.get(api_url)
    return response.json()

# Usage
data = load_data("large_dataset.csv")
processed = process_data(data)
st.dataframe(processed)
'''
        st.code(code_example, language='python')
        
        st.info("� Use `@st.cache_data` for pandas DataFrames, lists, dictionaries, and other serializable objects.")
    
    with tab2:
        st.markdown("**Use `@st.cache_resource` for global resources:**")
        code_example = '''
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import joblib

@st.cache_resource
def load_model():
    """Cache ML models"""
    return joblib.load('model.pkl')

@st.cache_resource  
def init_database_connection():
    """Cache database connections"""
    return create_connection(DATABASE_URL)

@st.cache_resource
def load_large_dataset():
    """Cache large datasets that don't change"""
    return pd.read_parquet('huge_dataset.parquet')

# Usage
model = load_model()
db_conn = init_database_connection()
predictions = model.predict(input_data)
'''
        st.code(code_example, language='python')
        
        st.warning("⚠️ Use `@st.cache_resource` for non-serializable objects like ML models, database connections, or global configurations.")
    
    with tab3:
        st.markdown("**Cache Management:**")
        code_example = '''
# Clear specific cache
st.cache_data.clear()
st.cache_resource.clear()

# Clear cache for specific function
@st.cache_data
def my_function():
    return expensive_computation()

# Clear this function's cache
my_function.clear()

# Cache configuration
@st.cache_data(
    ttl=3600,           # Time to live (seconds)
    max_entries=100,    # Maximum cache entries
    show_spinner=False, # Hide spinner
    persist="disk"      # Persist to disk
)
def cached_function():
    return data
'''
        st.code(code_example, language='python')
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Clear Data Cache"):
                st.cache_data.clear()
                st.success("Data cache cleared!")
        with col2:
            if st.button("🗑️ Clear Resource Cache"):
                st.cache_resource.clear()
                st.success("Resource cache cleared!")
    
    st.subheader("🚀 Performance Best Practices")
    
    best_practices = [
        {
            "title": "Use Appropriate Caching",
            "description": "Cache expensive operations like data loading, API calls, and model inference",
            "icon": "💾"
        },
        {
            "title": "Optimize Data Loading",
            "description": "Load only necessary data, use efficient formats (parquet, feather)",
            "icon": "📊"
        },
        {
            "title": "Lazy Loading",
            "description": "Load data only when needed, not at app startup",
            "icon": "⏱️"
        },
        {
            "title": "Efficient Widgets",
            "description": "Use forms to batch widget interactions, avoid unnecessary reruns",
            "icon": "🎛️"
        },
        {
            "title": "Memory Management",
            "description": "Clear large variables when done, use session state wisely",
            "icon": "🧠"
        },
        {
            "title": "Async Operations",
            "description": "Use asyncio for concurrent operations where possible",
            "icon": "🔄"
        }
    ]
    
    for practice in best_practices:
        st.markdown(f"""
        <div class='feature-card'>
            <h4>{practice['icon']} {practice['title']}</h4>
            <p>{practice['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("📊 Performance Monitoring")
    
    # Simulate performance metrics
    import random
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        load_time = round(random.uniform(0.1, 2.0), 2)
        load_change = f"{random.choice(['-', '+'])}{random.randint(1, 5)}%"
        st.metric("⏱️ Load Time", f"{load_time}s", load_change)
    with col2:
        memory_usage = random.randint(50, 200)
        memory_change = f"{random.choice(['-', '+'])}{random.randint(1, 10)}MB"
        st.metric("🧠 Memory Usage", f"{memory_usage}MB", memory_change)
    with col3:
        cache_hits = random.randint(85, 99)
        cache_change = f"+{random.randint(1, 3)}%"
        st.metric("💾 Cache Hit Rate", f"{cache_hits}%", cache_change)
    with col4:
        active_users = random.randint(10, 100)
        user_change = f"+{random.randint(1, 5)}"
        st.metric("👥 Active Users", active_users, user_change)
    
    # Performance tips based on metrics
    if load_time > 1.5:
        st.warning("⚠️ Consider adding caching to improve load times")
    if memory_usage > 150:
        st.warning("⚠️ High memory usage detected - consider optimizing data structures")
    if cache_hits < 90:
        st.info("💡 Low cache hit rate - review your caching strategy")

# Footer with enhanced styling
st.markdown("---")

# Create footer with proper Streamlit layout
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 2rem; border-radius: 15px; color: white; text-align: center; margin-top: 3rem;'>
    <h3>🚀 Ready to Build Amazing Apps?</h3>
    <p>You now have all the tools you need to create incredible Streamlit applications!</p>
</div>
""", unsafe_allow_html=True)

# Resource links using Streamlit columns for better compatibility
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 1rem 0;'>
        <h4>📚 Learn More</h4>
        <p><a href='https://docs.streamlit.io' target='_blank' style='color: #ffd700; text-decoration: none;'>Official Documentation</a></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 1rem 0;'>
        <h4>🎨 Get Inspired</h4>
        <p><a href='https://streamlit.io/gallery' target='_blank' style='color: #ffd700; text-decoration: none;'>App Gallery</a></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 1rem 0;'>
        <h4>💬 Get Help</h4>
        <p><a href='https://discuss.streamlit.io' target='_blank' style='color: #ffd700; text-decoration: none;'>Community Forum</a></p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 1rem 0;'>
        <h4>🐙 Contribute</h4>
        <p><a href='https://github.com/streamlit/streamlit' target='_blank' style='color: #ffd700; text-decoration: none;'>GitHub Repository</a></p>
    </div>
    """, unsafe_allow_html=True)

# Final footer with version info
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 2rem; border-radius: 15px; color: white; text-align: center; margin-top: 2rem;'>
    <hr style='margin: 2rem 0; border: 1px solid rgba(255,255,255,0.3);'>
    <p><strong>📚 Complete Streamlit Cheat Sheet</strong> | Made with ❤️ using Streamlit</p>
    <p><small>Last updated: July 2025 • Version 2.0 • Covers Streamlit 1.28+</small></p>
    <div style='margin-top: 1rem; font-size: 1.5rem;'>
        ⭐ 🚀 💡 🎯 📊
    </div>
</div>
""", unsafe_allow_html=True)
