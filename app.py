import requests
import streamlit as st
from PIL import Image

url = "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}
history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "cody",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        data = response.json()
        actual_response = data['response']
        return actual_response
    else:
        raise Exception(f"Error: {response.text}")


# Streamlit app initialization.
st.set_page_config(page_title="Iridium AI")

# Load and display Iridium logo.
logo_path = "Images/IridiumAILogo.png"
iridium_logo = Image.open(logo_path)
st.image(iridium_logo, use_column_width=False)

st.header("Cody: AI Powered Code Assistant")

prompt = st.text_area("Enter your Prompt", height=100)
if st.button("Generate"):
    try:
        response = generate_response(prompt)
        st.text("Response:")
        st.write(response)
    except Exception as e:
        st.error(str(e))
