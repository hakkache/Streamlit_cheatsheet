"""
Streamlit Multi-Page App Example
==============================

This example demonstrates how to create a multi-page Streamlit application
with navigation, state management, and various components.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta
import time
import json

# Page configuration
st.set_page_config(
    page_title="Multi-Page App Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-nav {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .nav-link {
        color: white;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0 0.25rem;
        transition: background 0.3s ease;
    }
    
    .nav-link:hover {
        background: rgba(255, 255, 255, 0.2);
    }
    
    .page-header {
        background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        border-left: 4px solid #4ecdc4;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

if 'app_metrics' not in st.session_state:
    st.session_state.app_metrics = {
        'total_visits': 0,
        'features_used': set(),
        'last_visit': datetime.now()
    }

# Sidebar navigation
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 10px; color: white; margin-bottom: 1rem;'>
        <h2>🧭 Navigation</h2>
        <p>Multi-Page App Demo</p>
    </div>
    """, unsafe_allow_html=True)
    
    pages = [
        "🏠 Home",
        "📊 Dashboard", 
        "📈 Analytics",
        "🎛️ Settings",
        "📝 Data Entry",
        "📋 Reports",
        "🎨 Playground"
    ]
    
    selected_page = st.selectbox("Select Page:", pages, key="page_selector")
    st.session_state.page = selected_page
    
    # User info
    st.markdown("---")
    st.markdown("### 👤 User Info")
    
    if 'username' not in st.session_state:
        username = st.text_input("Username:", placeholder="Enter your name")
        if username:
            st.session_state.username = username
            st.rerun()
    else:
        st.success(f"Welcome, {st.session_state.username}!")
        if st.button("Logout"):
            del st.session_state.username
            st.rerun()
    
    # App statistics
    st.markdown("---")
    st.markdown("### 📊 App Stats")
    st.session_state.app_metrics['total_visits'] += 1
    
    st.metric("Total Visits", st.session_state.app_metrics['total_visits'])
    st.metric("Features Used", len(st.session_state.app_metrics['features_used']))
    
    # Quick actions
    st.markdown("---")
    st.markdown("### ⚡ Quick Actions")
    
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.success("Data refreshed!")
    
    if st.button("📥 Export Settings"):
        settings_json = json.dumps(st.session_state.user_data, indent=2)
        st.download_button(
            "Download JSON",
            settings_json,
            "app_settings.json",
            "application/json"
        )

# Main content area
def render_home_page():
    """Render the home page"""
    st.markdown("""
    <div class='page-header'>
        <h1>🚀 Welcome to the Multi-Page App Demo</h1>
        <p>Explore different features and capabilities of Streamlit</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature overview
    st.subheader("🎯 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>📊 Interactive Dashboard</h3>
            <p>Real-time data visualization with dynamic charts and metrics</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>📈 Advanced Analytics</h3>
            <p>Deep dive into your data with statistical analysis and insights</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>🎛️ Customizable Settings</h3>
            <p>Personalize your experience with flexible configuration options</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent activity
    st.subheader("📋 Recent Activity")
    
    activities = [
        {"time": "2 minutes ago", "action": "Dashboard viewed", "user": "Current User"},
        {"time": "5 minutes ago", "action": "Data exported", "user": "Current User"},
        {"time": "10 minutes ago", "action": "Settings updated", "user": "Current User"},
        {"time": "15 minutes ago", "action": "Report generated", "user": "Current User"}
    ]
    
    for activity in activities:
        st.markdown(f"""
        <div style='background: #f8f9fa; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; 
                    border-left: 4px solid #4ecdc4;'>
            <strong>{activity['action']}</strong><br>
            <small>{activity['time']} • {activity['user']}</small>
        </div>
        """, unsafe_allow_html=True)


def render_dashboard_page():
    """Render the dashboard page"""
    st.markdown("""
    <div class='page-header'>
        <h1>📊 Interactive Dashboard</h1>
        <p>Monitor your key metrics and performance indicators</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.app_metrics['features_used'].add('Dashboard')
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Revenue", "$45,231", "12%")
    with col2:
        st.metric("Users", "1,235", "-2%")
    with col3:
        st.metric("Conversion", "3.4%", "0.8%")
    with col4:
        st.metric("Retention", "89%", "5%")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Revenue Trend")
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        revenue = np.cumsum(np.random.randn(30) * 100) + 1000
        df_revenue = pd.DataFrame({'Date': dates, 'Revenue': revenue})
        
        fig = px.line(df_revenue, x='Date', y='Revenue', title='Daily Revenue')
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 User Segments")
        segments = ['New Users', 'Returning', 'Premium', 'Enterprise']
        values = [234, 567, 123, 89]
        
        fig = px.pie(values=values, names=segments, title='User Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    # Real-time data simulation
    st.subheader("📡 Live Data Feed")
    
    if st.checkbox("Enable live updates"):
        placeholder = st.empty()
        
        for i in range(10):
            with placeholder.container():
                # Simulate real-time metrics
                current_users = np.random.randint(50, 200)
                server_load = np.random.randint(20, 90)
                response_time = np.random.randint(100, 500)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("👥 Active Users", current_users, f"{np.random.randint(-10, 20)}")
                with col2:
                    st.metric("⚡ Server Load", f"{server_load}%", f"{np.random.randint(-5, 5)}%")
                with col3:
                    st.metric("⏱️ Response Time", f"{response_time}ms", f"{np.random.randint(-50, 50)}ms")
            
            time.sleep(1)


def render_analytics_page():
    """Render the analytics page"""
    st.markdown("""
    <div class='page-header'>
        <h1>📈 Advanced Analytics</h1>
        <p>Deep insights and statistical analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.app_metrics['features_used'].add('Analytics')
    
    # Data filters
    st.subheader("🔍 Data Filters")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        date_range = st.date_input(
            "Date Range:",
            value=[date.today() - timedelta(days=30), date.today()],
            key="analytics_date_range"
        )
    with col2:
        metric_type = st.selectbox(
            "Metric Type:",
            ["Revenue", "Users", "Sessions", "Conversion"]
        )
    with col3:
        granularity = st.selectbox(
            "Granularity:",
            ["Daily", "Weekly", "Monthly"]
        )
    
    # Generate sample data based on filters
    if isinstance(date_range, list) and len(date_range) == 2:
        start_date, end_date = date_range
        days = (end_date - start_date).days + 1
        
        dates = pd.date_range(start_date, end_date, freq='D')
        np.random.seed(42)  # For consistent data
        
        if metric_type == "Revenue":
            values = np.cumsum(np.random.randn(days) * 50) + 1000
            unit = "$"
        elif metric_type == "Users":
            values = np.random.poisson(100, days) + np.random.randint(50, 150, days)
            unit = ""
        elif metric_type == "Sessions":
            values = np.random.poisson(200, days) + np.random.randint(100, 300, days)
            unit = ""
        else:  # Conversion
            values = np.random.uniform(0.02, 0.08, days)
            unit = "%"
        
        df_analytics = pd.DataFrame({
            'Date': dates[:len(values)],
            'Value': values,
            'Metric': metric_type
        })
        
        # Main chart
        st.subheader(f"📊 {metric_type} Analysis")
        
        fig = px.line(
            df_analytics, 
            x='Date', 
            y='Value',
            title=f"{metric_type} Over Time"
        )
        
        if unit == "%":
            fig.update_yaxis(tickformat='.2%')
        elif unit == "$":
            fig.update_yaxis(tickformat='$,.0f')
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Statistical summary
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Statistical Summary")
            summary_stats = {
                "Mean": df_analytics['Value'].mean(),
                "Median": df_analytics['Value'].median(),
                "Std Dev": df_analytics['Value'].std(),
                "Min": df_analytics['Value'].min(),
                "Max": df_analytics['Value'].max()
            }
            
            for stat, value in summary_stats.items():
                if unit == "%":
                    st.metric(stat, f"{value:.2%}")
                elif unit == "$":
                    st.metric(stat, f"${value:,.0f}")
                else:
                    st.metric(stat, f"{value:.0f}")
        
        with col2:
            st.subheader("📈 Trend Analysis")
            
            # Calculate trend
            x = np.arange(len(df_analytics))
            slope, intercept = np.polyfit(x, df_analytics['Value'], 1)
            
            if slope > 0:
                trend = "📈 Increasing"
                trend_color = "green"
            elif slope < 0:
                trend = "📉 Decreasing" 
                trend_color = "red"
            else:
                trend = "➡️ Stable"
                trend_color = "blue"
            
            st.markdown(f"""
            <div style='background: {trend_color}20; padding: 1rem; border-radius: 8px; 
                        border-left: 4px solid {trend_color};'>
                <h4>{trend}</h4>
                <p>Slope: {slope:.2f} per day</p>
            </div>
            """, unsafe_allow_html=True)


def render_settings_page():
    """Render the settings page"""
    st.markdown("""
    <div class='page-header'>
        <h1>🎛️ Application Settings</h1>
        <p>Customize your app experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.app_metrics['features_used'].add('Settings')
    
    # User preferences
    st.subheader("👤 User Preferences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        theme = st.selectbox(
            "Color Theme:",
            ["Light", "Dark", "Auto"],
            key="theme_setting"
        )
        
        language = st.selectbox(
            "Language:",
            ["English", "Spanish", "French", "German"],
            key="language_setting"
        )
        
        timezone = st.selectbox(
            "Timezone:",
            ["UTC", "EST", "PST", "GMT"],
            key="timezone_setting"
        )
    
    with col2:
        notifications = st.checkbox("Enable notifications", value=True)
        auto_refresh = st.checkbox("Auto-refresh data", value=False)
        advanced_mode = st.checkbox("Advanced mode", value=False)
    
    # Display preferences
    st.subheader("🎨 Display Preferences")
    
    chart_type = st.radio(
        "Default chart type:",
        ["Line", "Bar", "Area"],
        horizontal=True
    )
    
    items_per_page = st.slider("Items per page:", 10, 100, 25)
    
    decimal_places = st.number_input("Decimal places:", 0, 5, 2)
    
    # Data preferences
    st.subheader("📊 Data Preferences")
    
    default_date_range = st.slider(
        "Default date range (days):",
        1, 365, 30
    )
    
    auto_save = st.checkbox("Auto-save settings", value=True)
    
    # Save settings
    if st.button("💾 Save Settings"):
        settings = {
            "theme": theme,
            "language": language,
            "timezone": timezone,
            "notifications": notifications,
            "auto_refresh": auto_refresh,
            "advanced_mode": advanced_mode,
            "chart_type": chart_type,
            "items_per_page": items_per_page,
            "decimal_places": decimal_places,
            "default_date_range": default_date_range,
            "auto_save": auto_save,
            "saved_at": datetime.now().isoformat()
        }
        
        st.session_state.user_data.update(settings)
        st.success("✅ Settings saved successfully!")
        
        # Show saved settings
        with st.expander("View saved settings"):
            st.json(settings)


def render_data_entry_page():
    """Render the data entry page"""
    st.markdown("""
    <div class='page-header'>
        <h1>📝 Data Entry Form</h1>
        <p>Enter and manage your data</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.app_metrics['features_used'].add('Data Entry')
    
    # Initialize data storage
    if 'entered_data' not in st.session_state:
        st.session_state.entered_data = []
    
    # Data entry form
    with st.form("data_entry_form", clear_on_submit=True):
        st.subheader("📊 Enter New Record")
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name:", placeholder="Enter name")
            category = st.selectbox("Category:", ["Sales", "Marketing", "Support", "Development"])
            value = st.number_input("Value:", min_value=0.0, step=0.01)
        
        with col2:
            date_entered = st.date_input("Date:", value=date.today())
            priority = st.radio("Priority:", ["Low", "Medium", "High"], horizontal=True)
            notes = st.text_area("Notes:", placeholder="Additional notes...")
        
        tags = st.multiselect(
            "Tags:",
            ["Important", "Urgent", "Review", "Follow-up", "Complete"],
            default=[]
        )
        
        submitted = st.form_submit_button("➕ Add Record", use_container_width=True)
        
        if submitted and name and value:
            new_record = {
                "id": len(st.session_state.entered_data) + 1,
                "name": name,
                "category": category,
                "value": value,
                "date": date_entered.isoformat(),
                "priority": priority,
                "notes": notes,
                "tags": tags,
                "created_at": datetime.now().isoformat()
            }
            
            st.session_state.entered_data.append(new_record)
            st.success(f"✅ Record '{name}' added successfully!")
    
    # Display entered data
    if st.session_state.entered_data:
        st.subheader("📋 Entered Records")
        
        # Convert to DataFrame for display
        df = pd.DataFrame(st.session_state.entered_data)
        
        # Add filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            category_filter = st.multiselect(
                "Filter by category:",
                df['category'].unique(),
                default=df['category'].unique()
            )
        
        with col2:
            priority_filter = st.multiselect(
                "Filter by priority:",
                df['priority'].unique(),
                default=df['priority'].unique()
            )
        
        with col3:
            min_value = st.number_input("Min value:", value=0.0)
        
        # Apply filters
        filtered_df = df[
            (df['category'].isin(category_filter)) &
            (df['priority'].isin(priority_filter)) &
            (df['value'] >= min_value)
        ]
        
        # Display data
        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )
        
        # Summary statistics
        if not filtered_df.empty:
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Records", len(filtered_df))
            with col2:
                st.metric("Total Value", f"${filtered_df['value'].sum():,.2f}")
            with col3:
                st.metric("Average Value", f"${filtered_df['value'].mean():,.2f}")
            with col4:
                st.metric("High Priority", len(filtered_df[filtered_df['priority'] == 'High']))
        
        # Export options
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📥 Export to CSV"):
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    "Download CSV",
                    csv,
                    "data_export.csv",
                    "text/csv"
                )
        
        with col2:
            if st.button("🗑️ Clear All Data"):
                st.session_state.entered_data = []
                st.rerun()


# Page routing
page_functions = {
    "🏠 Home": render_home_page,
    "📊 Dashboard": render_dashboard_page,
    "📈 Analytics": render_analytics_page,
    "🎛️ Settings": render_settings_page,
    "📝 Data Entry": render_data_entry_page,
}

# Render selected page
if st.session_state.page in page_functions:
    page_functions[st.session_state.page]()
else:
    st.error("Page not found!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🚀 Multi-Page Streamlit App Demo | Built with ❤️ using Streamlit</p>
    <p><small>This demo showcases various Streamlit features in a multi-page application</small></p>
</div>
""", unsafe_allow_html=True)
