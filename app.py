import streamlit as st
import random
import base64
import os

# --- 1. BACKGROUND IMAGE HELPER ---
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

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

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="One Ring Trivia", page_icon="💍", layout="centered")

# Attempt to load your background file
set_page_bg('map.webp') 

# --- 3. CUSTOM CSS (STYLING THE SCRIM & FONTS) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bilbo+Swash+Caps&family=MedievalSharp&display=swap');

/* Style the main content area as the dark "scrim" box */
.block-container {
    background-color: rgba(15, 10, 5, 0.9) !important;
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
    font-family: 'MedievalSharp', serif !important;
    color: #f7e9cd !important;
    text-shadow: 1px 1px 2px #000;
}

.stInfo {
    background-color: rgba(45, 30, 15, 1.0) !important;
    border: 1px solid #FFD700 !important;
    border-radius: 10px;
}

div.stButton > button {
    display: block;
    margin: 0 auto;
    background-color: #5c0000 !important;
    color: #FFD700 !important;
    border: 2px solid #FFD700 !important;
    font-size: 20px;
    padding: 10px 40px;
}

section[data-testid="stSidebar"] {
    background-color: rgba(30, 20, 10, 0.95);
}

.stProgress > div > div > div > div {
    background-color: #FFD700;
}
</style>
""", unsafe_allow_html=True)

# --- 4. DATA & JOURNEY ---
LOCATIONS = [
    "The Shire", "Bucklebury Ferry", "Bree", "Weathertop", "Trollshaws", 
    "Rivendell", "Redhorn Pass", "Moria", "Khazad-dûm", "Lothlórien", 
    "Argonath", "Amon Hen", "Emyn Muil", "Dead Marshes", "Black Gate", 
    "Ithilien", "Minas Morgul", "Shelob's Lair", "Gorgoroth", "Mount Doom"
]

QUESTIONS = [
    {"quote": "All we have to decide is what to do with the time that is given us.", "correct": "Gandalf", "options": ["Elrond", "Galadriel", "Aragorn", "Gandalf"]},
    {"quote": "I can't carry it for you, but I can carry you!", "correct": "Samwise Gamgee", "options": ["Aragorn", "Merry", "Pippin", "Samwise Gamgee"]},
    {"quote": "One does not simply walk into Mordor.", "correct": "Boromir", "options": ["Aragorn", "Gimli", "Legolas", "Boromir"]},
    {"quote": "I am no man!", "correct": "Éowyn", "options": ["Arwen", "Galadriel", "Éomer", "Éowyn"]},
    {"quote": "My precious.", "correct": "Gollum", "options": ["Bilbo", "Frodo", "Sauron", "Gollum"]},
    {"quote": "Even the smallest person can change the course of the future.", "correct": "Galadriel", "options": ["Gandalf", "Elrond", "Bilbo", "
