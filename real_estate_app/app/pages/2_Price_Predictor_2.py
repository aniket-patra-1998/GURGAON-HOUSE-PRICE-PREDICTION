import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Set page title and icon
st.set_page_config(page_title="Property Price Predictor", page_icon="🏠")
st.title("Price Predictor")
# Custom CSS for styling
st.markdown(
    """
    <style>
    .header {
        color: #2a9df4;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        background-color: #f0f0f0;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .sidebar {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .button {
        color: #ffffff;
        background-color: #2a9df4;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
    .button:hover {
        background-color: #2578a8;
    }
    .result {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load data and model
with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

# Header
st.markdown('<h1 class="header">Property Price Predictor</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown('<div class="sidebar">Enter Property Details</div>', unsafe_allow_html=True)

# Sidebar inputs with emoji icons
property_type = st.sidebar.selectbox('Property Type 🏠', ['flat', 'house'])
sector = st.sidebar.selectbox('Sector 🏫', sorted(df['sector'].unique().tolist()))
bedrooms = float(st.sidebar.selectbox('Number of Bedrooms 🛏️', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.sidebar.selectbox('Number of Bathrooms 🚽', sorted(df['bathroom'].unique().tolist())))
balcony = st.sidebar.selectbox('Balconies 🌆', sorted(df['balcony'].unique().tolist()))
property_age = st.sidebar.selectbox('Property Age 🕰️', sorted(df['agePossession'].unique().tolist()))
built_up_area = float(st.sidebar.number_input('Built Up Area (sq. ft.) 📏'))
servant_room = float(st.sidebar.selectbox('Servant Room 👨‍💼', [0.0, 1.0]))
store_room = float(st.sidebar.selectbox('Store Room 🗄️', [0.0, 1.0]))
furnishing_type = st.sidebar.selectbox('Furnishing Type 🛋️', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.sidebar.selectbox('Luxury Category 💎', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.sidebar.selectbox('Floor Category 👞', sorted(df['floor_category'].unique().tolist()))

# Display image for flat locality
#st.image("https://images.unsplash.com/photo-1567538098723-4aafe42e0db3", use_column_width=True)

# Predict button
if st.sidebar.button('Predict', key='predict_button'):
    # Form dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']
    one_df = pd.DataFrame(data, columns=columns)

    # Predict price
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # Display results
    st.markdown('<div class="result"><h2>Predicted Price</h2>'
                f"<p>The average price of the property is <strong>{round(base_price, 2)} Cr</strong>.</p>"
                f"<p>The price of the flat is between <strong>{round(low, 2)} Cr</strong> and <strong>{round(high, 2)} Cr</strong>.</p></div>",
                unsafe_allow_html=True)
