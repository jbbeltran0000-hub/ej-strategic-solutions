import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import json

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Weather Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .weather-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .temp-display {
        font-size: 48px;
        font-weight: bold;
        margin: 10px 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border-left: 4px solid #667eea;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #667eea;
    }
    .metric-label {
        font-size: 12px;
        color: #666;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- WEATHER API FUNCTIONS ---
def get_weather_by_city(city_name, api_key):
    """Fetch current weather data from OpenWeatherMap API"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def get_forecast(city_name, api_key):
    """Fetch 5-day forecast data from OpenWeatherMap API"""
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching forecast data: {e}")
        return None

def get_air_quality(lat, lon, api_key):
    """Fetch air quality data from OpenWeatherMap API"""
    base_url = "https://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.warning(f"Could not fetch air quality data: {e}")
        return None

def get_aqi_label(aqi):
    """Convert AQI number to label"""
    labels = {
        1: "Good ✅",
        2: "Fair 🟡",
        3: "Moderate 🟠",
        4: "Poor 🔴",
        5: "Very Poor ⛔"
    }
    return labels.get(aqi, "Unknown")

# --- HEADER ---
st.title("🌤️ Weather Dashboard")
st.write("Get real-time weather information and forecasts for any city worldwide")

st.divider()

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("⚙️ Configuration")
st.sidebar.info("""
    This dashboard uses the **OpenWeatherMap API** (free tier).
    
    Get your free API key:
    1. Visit https://openweathermap.org/api
    2. Sign up for free
    3. Generate an API key
    4. Paste it below
""")

api_key = st.sidebar.text_input("Enter your OpenWeatherMap API Key:", type="password")

# --- MAIN CONTENT ---
if not api_key:
    st.warning("⚠️ Please enter your OpenWeatherMap API key in the sidebar to get started!")
    st.info("""
        **How to get a free API key:**
        1. Go to https://openweathermap.org/api
        2. Click "Sign Up"
        3. Complete registration
        4. Go to your API keys page
        5. Copy your default API key
        6. Paste it in the sidebar (left panel)
    """)
else:
    # --- SEARCH SECTION ---
    col1, col2 = st.columns([4, 1])
    
    with col1:
        city_input = st.text_input(
            "Enter city name:",
            value="San Francisco",
            placeholder="e.g., London, Tokyo, New York"
        )
    
    with col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    if city_input or search_button:
        city_name = city_input if city_input else "San Francisco"
        
        with st.spinner(f"Fetching weather data for {city_name}..."):
            weather_data = get_weather_by_city(city_name, api_key)
        
        if weather_data:
            # --- CURRENT WEATHER DISPLAY ---
            st.divider()
            st.subheader(f"Current Weather in {weather_data['name']}, {weather_data['sys']['country']}")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                    <div class="weather-card">
                        <div>{weather_data['weather'][0]['main']}</div>
                        <div class="temp-display">{weather_data['main']['temp']:.1f}°C</div>
                        <div style="font-size: 14px; opacity: 0.9;">
                            Feels like {weather_data['main']['feels_like']:.1f}°C
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # --- WEATHER METRICS ---
            with col2:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Humidity</div>
                        <div class="metric-value">{weather_data['main']['humidity']}%</div>
                    </div>
                    <br>
                    <div class="metric-card">
                        <div class="metric-label">Pressure</div>
                        <div class="metric-value">{weather_data['main']['pressure']} hPa</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Wind Speed</div>
                        <div class="metric-value">{weather_data['wind']['speed']:.1f} m/s</div>
                    </div>
                    <br>
                    <div class="metric-card">
                        <div class="metric-label">Visibility</div>
                        <div class="metric-value">{weather_data['visibility'] / 1000:.1f} km</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # --- DETAILED INFO ---
            st.divider()
            st.subheader("📊 Detailed Information")
            
            detail_col1, detail_col2, detail_col3, detail_col4 = st.columns(4)
            
            with detail_col1:
                st.metric("Max Temperature", f"{weather_data['main']['temp_max']:.1f}°C")
            with detail_col2:
                st.metric("Min Temperature", f"{weather_data['main']['temp_min']:.1f}°C")
            with detail_col3:
                st.metric("Cloud Coverage", f"{weather_data['clouds']['all']}%")
            with detail_col4:
                st.metric("Wind Direction", f"{weather_data['wind'].get('deg', 'N/A')}°")
            
            # --- AIR QUALITY ---
            lat, lon = weather_data['coord']['lat'], weather_data['coord']['lon']
            air_quality = get_air_quality(lat, lon, api_key)
            
            if air_quality and 'list' in air_quality and len(air_quality['list']) > 0:
                st.divider()
                st.subheader("🌍 Air Quality Index (AQI)")
                
                aqi_data = air_quality['list'][0]
                aqi = aqi_data.get('main', {}).get('aqi', None)
                
                if aqi:
                    aqi_col1, aqi_col2 = st.columns(2)
                    with aqi_col1:
                        st.metric("AQI Status", get_aqi_label(aqi))
                    with aqi_col2:
                        st.metric("AQI Level", aqi)
                    
                    # Pollutants
                    if 'components' in aqi_data:
                        st.write("**Pollutant Levels (μg/m³):**")
                        pollutants = aqi_data['components']
                        pollutant_cols = st.columns(4)
                        
                        pollutant_names = ['pm2_5', 'pm10', 'o3', 'no2']
                        for i, pollutant in enumerate(pollutant_names):
                            if pollutant in pollutants:
                                with pollutant_cols[i]:
                                    st.metric(
                                        pollutant.upper().replace('_', ' '),
                                        f"{pollutants[pollutant]:.1f}"
                                    )
            
            # --- FORECAST ---
            st.divider()
            st.subheader("📅 5-Day Forecast")
            
            forecast_data = get_forecast(city_name, api_key)
            
            if forecast_data:
                # Parse forecast data
                forecast_list = forecast_data['list']
                forecast_df_list = []
                
                for item in forecast_list[::8]:  # Every 24 hours
                    forecast_df_list.append({
                        'Date': datetime.fromtimestamp(item['dt']).strftime('%a, %b %d'),
                        'Temp (°C)': f"{item['main']['temp']:.1f}",
                        'Condition': item['weather'][0]['main'],
                        'Humidity (%)': item['main']['humidity'],
                        'Wind (m/s)': f"{item['wind']['speed']:.1f}"
                    })
                
                forecast_df = pd.DataFrame(forecast_df_list)
                st.dataframe(forecast_df, use_container_width=True, hide_index=True)
                
                # Hourly forecast chart
                st.write("**Temperature Trend (Next 5 Days):**")
                chart_data = []
                for item in forecast_list:
                    chart_data.append({
                        'Time': datetime.fromtimestamp(item['dt']),
                        'Temperature': item['main']['temp']
                    })
                
                chart_df = pd.DataFrame(chart_data)
                st.line_chart(data=chart_df.set_index('Time')['Temperature'], use_container_width=True)
            
            # --- RAW DATA (Advanced) ---
            with st.expander("📋 View Raw JSON Data"):
                st.json(weather_data)
        
        else:
            st.error(f"Could not find weather data for '{city_name}'. Please check the spelling and try again.")

# --- FOOTER ---
st.divider()
st.markdown("""
    <footer style="text-align: center; color: #666; font-size: 12px; margin-top: 30px;">
        <p>Weather data powered by <a href="https://openweathermap.org/" target="_blank">OpenWeatherMap</a></p>
        <p>Dashboard built with Streamlit | Updated: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</p>
    </footer>
    """, unsafe_allow_html=True)
