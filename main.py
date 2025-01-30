import pickle
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Car Price Predictions App")

# Load the cars list and model
cars = pickle.load(open('cars_list.pkl', 'rb'))
car_data = pd.DataFrame(cars)

# Load the trained model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# App Title
st.markdown("""<span style ="color : red ; font-weight: bold; font-size: 40px;">Car Price Predictions System </span>""", unsafe_allow_html=True)

# Select car brand (company)
st.markdown("""<span style ="font-size: 22px; font-weight: bold; color: #D8D8D8; margin-bottom: -20px; ">Select the Brand : </span>""", unsafe_allow_html=True)
selected_car_brand = st.selectbox("", car_data['company'].dropna().unique().tolist(), label_visibility="collapsed")

# Filter car names based on selected brand
filtered_cars = car_data[car_data['company'] == selected_car_brand]  # Get cars matching the selected brand
filtered_car_names = filtered_cars['name'].dropna().unique().tolist()  # Extract unique car names

# Select car name (only showing names of the selected brand)
st.markdown("""<span style ="font-size: 22px; font-weight: bold; color: #D8D8D8; margin-bottom: -20px; ">Select the Name : </span>""", unsafe_allow_html=True)
selected_car_name = st.selectbox("", filtered_car_names, label_visibility="collapsed")

# Select car year
st.markdown("""<span style ="font-size: 22px; font-weight: bold; color: #D8D8D8; margin-bottom: -20px; ">Select the Year : </span>""", unsafe_allow_html=True)
selected_year = st.selectbox("", car_data['year'].dropna().unique().tolist(), label_visibility="collapsed")

# Input for kilometers driven
st.markdown("""<span style ="font-size: 22px; font-weight: bold; color: #D8D8D8; margin-bottom: -20px; ">Enter Kilometers Driven (in thousands) : </span>""", unsafe_allow_html=True)
kms_driven = st.number_input("", min_value=0, value=50 ,label_visibility="collapsed")

# Select fuel type
st.markdown("""<span style ="font-size: 22px; font-weight: bold; color: #D8D8D8; margin-bottom: -20px; ">Select Fuel Type : </span>""", unsafe_allow_html=True)
fuel_type = st.selectbox("", car_data['fuel_type'].dropna().unique().tolist(), label_visibility="collapsed")

# Prepare data for prediction
input_data = pd.DataFrame([[selected_car_name, selected_car_brand, selected_year, kms_driven, fuel_type]],columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

# # Make prediction when button is pressed
# if st.button('Predict Price'):
#     predicted_price = model.predict(input_data)
#     st.markdown(f"<h3 style='color: #FFFFFF;'>Predicted Price: ₹{predicted_price[0]:.2f}</h3>", unsafe_allow_html=True)

# Make prediction when button is pressed
if st.button('Predict Price'):
    predicted_price = model.predict(input_data)
    if predicted_price<0:
        predicted_price = predicted_price*(-1)
    # Style the predicted price with HTML
    price_html = f"""
    <div style="font-size: 30px; font-weight: bold; color: #FFFFFF; background-color: #282828; padding: 20px; border-radius: 10px; text-align: center;">
        Predicted Price: <span style="color: red;">₹{predicted_price[0]:.2f}</span>
    </div>
    """
    
    # Display the styled result
    st.markdown(price_html, unsafe_allow_html=True)
