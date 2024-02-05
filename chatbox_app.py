import pickle
import streamlit as st
import tensorflow as tf

def load_model():
    model_path = r'C:\Users\pritesh.tiwary\Downloads\nlp_chatbot.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.set_page_config(page_title="NLP Chatbox for Accident", page_icon="🚑", layout="centered")
    st.title("NLP Chatbox for Accident")
    st.markdown('<style>h1{color: #336699;}</style>', unsafe_allow_html=True)
    nlp_model = load_model()
    tf_version = tf.__version__
    st.sidebar.header(f"Information (TensorFlow Version: {tf_version})")
    st.sidebar.markdown("This is a simple NLP chatbox for handling accident-related queries.")

    # User inputs for each column
    data_input = st.text_input("Data:")
    countries_input = st.text_input("Countries:")
    local_input = st.text_input("Local:")
    industry_sector_input = st.text_input("Industry Sector:")
    potential_accident_level_input = st.text_input("Potential Accident Level:")
    genre_input = st.text_input("Genre:")
    employee_third_party_input = st.text_input("Employee or Third Party:")
    critical_risk_input = st.text_input("Critical Risk:")
    description_input = st.text_area("Description:", height=100)

    if st.button("Submit"):
        collected_data = {
            "Data": data_input,
            "Countries": countries_input,
            "Local": local_input,
            "Industry Sector": industry_sector_input,
            "Potential Accident Level": potential_accident_level_input,
            "Genre": genre_input,
            "Employee or Third Party": employee_third_party_input,
            "Critical Risk": critical_risk_input,
            "Description": description_input
        }
        response = process_user_input(collected_data, nlp_model)
        st.text_area("Chatbot Response:", value=response, height=100, max_chars=500, key="chat_response", disabled=True)

def process_user_input(user_input, model):
    # Process the collected data and return a response from your model here.
    # For now, we'll just return a string representation of the user_input dictionary.
    return f"Received input: {user_input}"

if __name__ == "__main__":
    main()

