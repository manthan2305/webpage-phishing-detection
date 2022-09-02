import joblib
import streamlit as st

from scripts.feature_extractor import extract_features

# Load model & scaler transformation
clf = joblib.load("models/random_forest_clf_all.joblib")
scaler = joblib.load("models/scaler.joblib")

# Header
st.header("Webpage phishing detection")

# Sub-header
st.subheader("Detect website is phishing or not")

# Input text for URL
url = st.text_input("Enter URL")

if st.button("Submit"):

    print(url)

    features = extract_features(url, 'dummy_status')
    x_features = features[1:-1]

    # transform features
    x_test = scaler.transform([x_features])

    # predict the class
    y_pred = clf.predict(x_test)

    if y_pred[0] == 0:
        st.success('Legitimate')
    else:
        st.error('Phishing')
    

