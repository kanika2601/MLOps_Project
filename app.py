import streamlit as st
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Load the trained model from the .h5 file
model = load_model('/Users/kanikagulati/Desktop/11/ann_model.h5')

# Streamlit page configuration
st.set_page_config(page_title="Emotion Prediction", layout="centered")
st.markdown(
    """
    <style>
    body {
        color: #333;
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    .main {
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    h1 {
        color: #4CAF50;
    }
    .btn-primary {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("Emotion Prediction from Audio Features")

# Input fields for the 60 features
st.write("### Enter the 60 features for emotion prediction:")
input_features = []
for i in range(60):
    value = st.number_input(f"Feature {i+1}", step=0.01)
    input_features.append(value)

# Button for prediction
if st.button("Predict Emotion"):
    # Preprocess the input features
    feature_array = np.array(input_features).reshape(1, -1)
    scaler = StandardScaler()
    feature_scaled = scaler.fit_transform(feature_array)

    # Predict the emotion label
    predicted_label = np.argmax(model.predict(feature_scaled), axis=1)

    # Display the prediction
    st.write("### Predicted Emotion Label:", predicted_label[0])
