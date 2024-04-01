<<<<<<< HEAD
import pickle
import streamlit as st

# Load the saved model
Diamond_price = pickle.load(open('diamond_price_model2.pkl', 'rb'))

# Page title
st.title('Diamond Price Prediction using ML')

# Input fields
col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

with col1:
    carat = st.text_input('Carat Value')

with col2:
    cut = st.text_input('Cut Level')

with col3:
    color = st.text_input('Diamond Color')

with col4:
    clarity = st.text_input('Clarity Level')

with col5:
    depth = st.text_input('Depth Value of Diamond')

with col6:
    table = st.text_input('Width of Top of Diamond')

with col7:
    x = st.text_input('X Dimension Value')

with col8:
    y = st.text_input('Y Dimension Value')

with col9:
    z = st.text_input('Z Dimension Value')

# Default value for price_prediction
price_prediction = ''

# Prediction button
if st.button('Predict Diamond Price'):
    # Ensure input data is valid and convert to appropriate types
    try:
        input_data = [[float(carat), float(cut), float(color), float(clarity),
                       float(depth), float(table), float(x), float(y), float(z)]]
        price_prediction = Diamond_price.predict(input_data)
        st.success(f'Predicted Diamond Price: ${price_prediction[0]:.2f}')
    except ValueError:
        st.error('Please enter valid numerical values for all input fields.')

# Display the prediction result
st.success(price_prediction)
=======
import pickle
import streamlit as st

# Load the saved model
Diamond_price = pickle.load(open('diamond_price_model.pkl', 'rb'))

# Page title
st.title('Diamond Price Prediction using ML')

# Input fields
col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

with col1:
    carat = st.text_input('Carat Value')

with col2:
    cut = st.text_input('Cut Level')

with col3:
    color = st.text_input('Diamond Color')

with col4:
    clarity = st.text_input('Clarity Level')

with col5:
    depth = st.text_input('Depth Value of Diamond')

with col6:
    table = st.text_input('Width of Top of Diamond')

with col7:
    x = st.text_input('X Dimension Value')

with col8:
    y = st.text_input('Y Dimension Value')

with col9:
    z = st.text_input('Z Dimension Value')

# Default value for price_prediction
price_prediction = ''

# Prediction button
if st.button('Predict Diamond Price'):
    # Ensure input data is valid and convert to appropriate types
    try:
        input_data = [[float(carat), float(cut), float(color), float(clarity),
                       float(depth), float(table), float(x), float(y), float(z)]]
        price_prediction = Diamond_price.predict(input_data)
        st.success(f'Predicted Diamond Price: ${price_prediction[0]:.2f}')
    except ValueError:
        st.error('Please enter valid numerical values for all input fields.')

# Display the prediction result
st.success(price_prediction)
>>>>>>> origin/main
