"""
Advanced Streamlit Examples and Utilities
========================================

This module contains advanced examples and utility functions
for the Streamlit Cheat Sheet application.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time


def create_sample_dashboard():
    """Create a sample dashboard with multiple components"""
    
    st.title("📊 Sample Dashboard")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Sales", "$45,231", "12%")
    with col2:
        st.metric("New Customers", "1,235", "-2%")
    with col3:
        st.metric("Revenue", "$12,426", "8%")
    with col4:
        st.metric("Conversion Rate", "3.4%", "0.8%")
    
    # Charts row
    col1, col2 = st.columns(2)
    
    with col1:
        # Sample time series data
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        values = np.cumsum(np.random.randn(30)) + 100
        df = pd.DataFrame({'Date': dates, 'Value': values})
        
        fig = px.line(df, x='Date', y='Value', title='Sales Trend')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Sample bar chart
        categories = ['Product A', 'Product B', 'Product C', 'Product D']
        values = [23, 45, 56, 78]
        df_bar = pd.DataFrame({'Category': categories, 'Sales': values})
        
        fig_bar = px.bar(df_bar, x='Category', y='Sales', title='Product Sales')
        st.plotly_chart(fig_bar, use_container_width=True)


def create_data_processor():
    """Create an interactive data processing tool"""
    
    st.title("🔧 Data Processor")
    
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.subheader("📋 Data Preview")
        st.dataframe(df.head(), use_container_width=True)
        
        st.subheader("📊 Data Info")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Rows", len(df))
        with col2:
            st.metric("Columns", len(df.columns))
        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())
        
        # Data processing options
        st.subheader("🛠️ Processing Options")
        
        if st.checkbox("Remove missing values"):
            df = df.dropna()
            st.success(f"Removed missing values. New shape: {df.shape}")
        
        if st.checkbox("Show statistics"):
            st.dataframe(df.describe(), use_container_width=True)
        
        # Download processed data
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Processed Data",
            data=csv,
            file_name="processed_data.csv",
            mime="text/csv"
        )


def create_form_builder():
    """Create a dynamic form builder"""
    
    st.title("📝 Dynamic Form Builder")
    
    # Form configuration
    st.subheader("🔧 Form Configuration")
    
    form_title = st.text_input("Form Title", "User Information Form")
    num_fields = st.number_input("Number of Fields", min_value=1, max_value=10, value=3)
    
    # Build form fields
    fields = []
    for i in range(num_fields):
        st.write(f"**Field {i+1}:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            field_type = st.selectbox(
                f"Type {i+1}:",
                ["text", "number", "select", "checkbox", "date"],
                key=f"type_{i}"
            )
        
        with col2:
            field_label = st.text_input(f"Label {i+1}:", f"Field {i+1}", key=f"label_{i}")
        
        with col3:
            field_required = st.checkbox(f"Required {i+1}", key=f"required_{i}")
        
        fields.append({
            'type': field_type,
            'label': field_label,
            'required': field_required,
            'key': f"form_field_{i}"
        })
    
    # Generate form
    st.subheader("📋 Generated Form")
    
    with st.form("dynamic_form"):
        st.title(form_title)
        
        form_data = {}
        for field in fields:
            if field['type'] == 'text':
                form_data[field['key']] = st.text_input(field['label'])
            elif field['type'] == 'number':
                form_data[field['key']] = st.number_input(field['label'])
            elif field['type'] == 'select':
                form_data[field['key']] = st.selectbox(field['label'], ["Option 1", "Option 2", "Option 3"])
            elif field['type'] == 'checkbox':
                form_data[field['key']] = st.checkbox(field['label'])
            elif field['type'] == 'date':
                form_data[field['key']] = st.date_input(field['label'])
        
        submitted = st.form_submit_button("Submit Form")
        
        if submitted:
            st.success("Form submitted successfully!")
            st.json(form_data)


def create_chart_generator():
    """Create an interactive chart generator"""
    
    st.title("📈 Interactive Chart Generator")
    
    # Sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'] * 20,
        'Value': np.random.randn(100).cumsum(),
        'Size': np.random.randint(10, 100, 100),
        'Date': pd.date_range('2024-01-01', periods=100, freq='D')[:100]
    })
    
    # Chart configuration
    st.subheader("🎨 Chart Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        chart_type = st.selectbox(
            "Chart Type:",
            ["Line", "Bar", "Scatter", "Area", "Histogram"]
        )
        
        x_column = st.selectbox("X-axis:", data.columns)
    
    with col2:
        y_column = st.selectbox("Y-axis:", [col for col in data.columns if col != x_column])
        
        color_column = st.selectbox("Color by:", [None] + list(data.columns))
    
    # Generate chart
    st.subheader(f"📊 {chart_type} Chart")
    
    try:
        if chart_type == "Line":
            fig = px.line(data, x=x_column, y=y_column, color=color_column)
        elif chart_type == "Bar":
            fig = px.bar(data, x=x_column, y=y_column, color=color_column)
        elif chart_type == "Scatter":
            fig = px.scatter(data, x=x_column, y=y_column, color=color_column, size='Size')
        elif chart_type == "Area":
            fig = px.area(data, x=x_column, y=y_column, color=color_column)
        elif chart_type == "Histogram":
            fig = px.histogram(data, x=x_column, color=color_column)
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Chart customization
        if st.checkbox("Show chart data"):
            st.dataframe(data, use_container_width=True)
            
    except Exception as e:
        st.error(f"Error generating chart: {e}")


def create_live_data_monitor():
    """Create a live data monitoring dashboard"""
    
    st.title("📡 Live Data Monitor")
    
    # Auto-refresh toggle
    auto_refresh = st.checkbox("Auto-refresh every 2 seconds")
    
    if auto_refresh:
        # Create placeholder for dynamic content
        placeholder = st.empty()
        
        # Simulate live data
        for i in range(10):
            with placeholder.container():
                # Generate random metrics
                cpu_usage = np.random.randint(20, 90)
                memory_usage = np.random.randint(30, 85)
                network_traffic = np.random.randint(100, 1000)
                
                # Display metrics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("CPU Usage", f"{cpu_usage}%", f"{np.random.randint(-5, 5)}%")
                with col2:
                    st.metric("Memory Usage", f"{memory_usage}%", f"{np.random.randint(-3, 3)}%")
                with col3:
                    st.metric("Network Traffic", f"{network_traffic} MB/s", f"{np.random.randint(-50, 50)} MB/s")
                
                # Generate time series data
                timestamps = pd.date_range(datetime.now() - timedelta(minutes=10), periods=20, freq='30S')
                cpu_data = pd.DataFrame({
                    'Time': timestamps,
                    'CPU': np.random.randint(20, 90, 20),
                    'Memory': np.random.randint(30, 85, 20)
                })
                
                # Live chart
                fig = px.line(cpu_data, x='Time', y=['CPU', 'Memory'], title='System Performance')
                st.plotly_chart(fig, use_container_width=True)
                
                # Status indicators
                st.subheader("🚦 System Status")
                
                status_col1, status_col2, status_col3 = st.columns(3)
                
                with status_col1:
                    if cpu_usage > 80:
                        st.error("🔴 High CPU Usage")
                    elif cpu_usage > 60:
                        st.warning("🟡 Moderate CPU Usage")
                    else:
                        st.success("🟢 Normal CPU Usage")
                
                with status_col2:
                    if memory_usage > 80:
                        st.error("🔴 High Memory Usage")
                    elif memory_usage > 60:
                        st.warning("🟡 Moderate Memory Usage")
                    else:
                        st.success("🟢 Normal Memory Usage")
                
                with status_col3:
                    if network_traffic > 800:
                        st.error("🔴 High Network Traffic")
                    elif network_traffic > 500:
                        st.warning("🟡 Moderate Network Traffic")
                    else:
                        st.success("🟢 Normal Network Traffic")
            
            time.sleep(2)
    else:
        st.info("Enable auto-refresh to see live data updates!")


# Utility functions
def format_number(number):
    """Format numbers with appropriate suffixes"""
    if number >= 1_000_000:
        return f"{number/1_000_000:.1f}M"
    elif number >= 1_000:
        return f"{number/1_000:.1f}K"
    else:
        return str(number)


def create_color_palette(base_color="#ff6b6b", n_colors=5):
    """Generate a color palette based on a base color"""
    import colorsys
    
    # Convert hex to RGB
    base_rgb = tuple(int(base_color[i:i+2], 16) for i in (1, 3, 5))
    
    # Convert to HSV
    h, s, v = colorsys.rgb_to_hsv(base_rgb[0]/255, base_rgb[1]/255, base_rgb[2]/255)
    
    # Generate palette
    colors = []
    for i in range(n_colors):
        # Vary the hue slightly
        new_h = (h + i * 0.1) % 1.0
        new_rgb = colorsys.hsv_to_rgb(new_h, s, v)
        hex_color = "#{:02x}{:02x}{:02x}".format(
            int(new_rgb[0] * 255),
            int(new_rgb[1] * 255),
            int(new_rgb[2] * 255)
        )
        colors.append(hex_color)
    
    return colors


def display_code_with_copy(code, language="python"):
    """Display code with a copy button"""
    st.code(code, language=language)
    
    if st.button("📋 Copy Code", key=f"copy_{hash(code)}"):
        # In a real app, you'd use JavaScript to copy to clipboard
        st.success("Code copied to clipboard! (Note: Actual copying requires JavaScript)")


if __name__ == "__main__":
    st.set_page_config(page_title="Advanced Examples", layout="wide")
    
    st.title("🚀 Advanced Streamlit Examples")
    
    example_type = st.selectbox(
        "Choose an example:",
        [
            "Sample Dashboard",
            "Data Processor", 
            "Form Builder",
            "Chart Generator",
            "Live Data Monitor"
        ]
    )
    
    if example_type == "Sample Dashboard":
        create_sample_dashboard()
    elif example_type == "Data Processor":
        create_data_processor()
    elif example_type == "Form Builder":
        create_form_builder()
    elif example_type == "Chart Generator":
        create_chart_generator()
    elif example_type == "Live Data Monitor":
        create_live_data_monitor()
