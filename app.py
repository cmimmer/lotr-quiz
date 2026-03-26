import streamlit as st
import random
import base64
import os

# --- 1. THE "MAGIC" TO LOAD LOCAL IMAGES ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    if os.path.exists(bin_file):
        bin_str = get_base64_of_bin_file(bin_file)
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

# Set the background using the file you uploaded to GitHub
# Make sure the filename here matches exactly what you uploaded!
set_png_as_page_bg('map.webp') 

# Custom CSS for fonts and boxes
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bilbo+Swash+Caps&family=MedievalSharp&display=swap');

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
        color: #fcf6e3 !important; 
        text-shadow: 1px 1px 2px #000;
    }

    .stInfo {
        background-color: rgba(25, 15, 5, 0.9) !important;
        border: 2px solid #FFD700 !important;
        border-radius: 15px;
        padding: 20px;
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
        background-color: rgba(30, 20, 10, 0.85);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE REST OF YOUR QUIZ LOGIC (SAME AS BEFORE) ---
LOCATIONS = [
    "The Shire", "Bree", "Weathertop", "Rivendell", "Moria", "Lothlórien", 
    "Amon Hen", "The Dead Marshes", "The Black Gate", "Mount Doom"
]

QUESTIONS = [
    {"quote": "All we have to decide is what to do with the time that is given us.", "correct": "Gandalf", "options": ["Elrond", "Galadriel", "Aragorn", "Gandalf"]},
    {"quote": "I can't carry it for you, but I can carry you!", "correct": "Samwise Gamgee", "options": ["Aragorn", "Merry", "Pippin", "Samwise Gamgee"]},
    {"quote": "One does not simply walk into Mordor.", "correct": "Boromir", "options": ["Aragorn", "Gimli", "Legolas", "Boromir"]},
    {"quote": "I am no man!", "correct": "Éowyn", "options": ["Arwen", "Galadriel", "Éomer", "Éowyn"]}
]

if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.quiz_data = QUESTIONS.copy()
    random.shuffle(st.session_state.quiz_data)

# Sidebar
with st.sidebar:
    st.header("⚙️ Adventure Settings")
    music_on = st.toggle("🎵 Background Music", value=False)
    if music_on:
        st.audio("http://soundimage.org/wp-content/uploads/2014/04/Fantascape.mp3", format="audio/mp3", autoplay=True, loop=True)
    
    st.divider()
    st.header("📜 Quest Progress")
    progress = st.session_state.current_idx / len(st.session_state.quiz_data)
    st.progress(progress)
    st.write(f"Score: {st.session_state.score}")

# Main UI
st.markdown('<h1 class="cursive-title">The One Ring Trivia</h1>', unsafe_allow_html=True)

if st.session_state.current_idx < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_idx]
    st.info(f"### \"{item['quote']}\"")
    
    with st.form(key=f"quiz_form_{st.session_state.current_idx}"):
        user_choice = st.radio("Who spoke these words?", item['options'])
        submit = st.form_submit_button("Cast into the Fire")
        
        if submit:
            if user_choice == item['correct']:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! It was {item['correct']}.")
            st.session_state.current_idx += 1
            st.form_submit_button("Continue")
else:
    st.balloons()
    st.markdown('<h1 class="cursive-title">Quest Complete!</h1>', unsafe_allow_html=True)
    if st.button("Start New Quest"):
        st.session_state.current_idx = 0
        st.session_state.score = 0
        st.rerun()
