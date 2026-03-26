import streamlit as st
import random
import base64
import os

# --- 1. IMAGE LOADING HELPERS ---
# Function to convert a local image file to a Base64 string.
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Sets the main page background using 'map.webp'
def set_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    if bin_str:
        st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("data:image/webp;base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """, unsafe_allow_html=True)

# Helper function specifically to display an encoded image with a width of 300px
def display_encoded_image(bin_file, caption_text):
    bin_str = get_base64_of_bin_file(bin_file)
    if bin_str:
        st.image(f"data:image/png;base64,{bin_str}", width=300, caption=caption_text)
    else:
        # Fallback if the specific filename is not found
        st.caption(f"({bin_file} image not found, check filename on GitHub)")

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="One Ring Trivia", page_icon="💍", layout="centered")

# Attempt to load your main background file
set_page_bg('map.webp') 

# --- 3. CUSTOM CSS (STYLING THE CONTENT BOX, FONTS, & INSULTS) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bilbo+Swash+Caps&family=MedievalSharp&display=swap');

/* Style the main content area as the dark "scrim" box */
.block-container {
    background-color: rgba(15, 10, 5, 0.92) !important;
    padding: 3rem 2rem !important;
    border-radius: 20px !important;
    border: 2px solid #FFD700 !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.9) !important;
    margin-top: 2rem;
}

.cursive-title {
    font-family: 'Bilbo Swash Caps', cursive;
    color: #FFD700;
    text-align: center;
    font-size: 80px !important;
    text-shadow: 3px 3px 5px #000;
    margin-bottom: 0px;
}

h1, h2, h3, p, label, .stMarkdown {
