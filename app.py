import streamlit as st
import random
import base64
import os

# --- 1. THE "MAGIC" TO LOAD LOCAL IMAGES ---
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

def set_png_as_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="One Ring Trivia", page_icon="💍", layout="centered")

# Set the background using your uploaded file 'map.webp'
set_png_as_page_bg('map.webp') 

# --- 3. CUSTOM CSS FOR MAIN CONTENT STYLING & THEME ---
# The logic here is to style Streamlit's *actual* content container directly, 
# ensuring text sits on top of the dark scrim background.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bilbo+Swash+Caps&family=MedievalSharp&display=swap');

    /* The true fix: Styling the Streamlit block-container as the scrim background. */
    /* This ensures all components render CORRECTLY inside the dark area. */
    .block-container {
        background-color: rgba(15, 10, 5, 0.88) !important; /* The scrim color */
        padding: 40px !important;
        border-radius: 20px !important;
        border: 2px solid #FFD700 !important; /* Gold border */
        box-shadow: 0 10px 30px rgba(0,0,0,0.9) !important;
        margin-bottom: 20px !important;
        color: #f7e9cd !important; /* Default soft cream text inside scrim */
    }

    .cursive-title {
        font-family: 'Bilbo Swash Caps', cursive;
        color: #FFD700;
        text-align: center;
        font-size: 80px !important;
        text-shadow: 3px 3px 5px #000;
        margin-top: -30px;
    }

    h1, h2, h3, p, label, .stMarkdown {
        font-family: 'MedievalSharp', serif !important;
        color: #f7e9cd !important; /* Set default text color for softness */
        text-shadow: 1px 1px 2px #000;
    }

    /* Style the stInfo box to ensure readable gold text */
    .stInfo {
        background-color: rgba(45, 30, 15, 1.0) !important;
        border: 2px solid #FFD700 !important;
        border-radius: 15px;
        padding: 20px;
