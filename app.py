import streamlit as st
import random

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(page_title="One Ring Trivia", page_icon="💍", layout="centered")

# Custom CSS for the "Parchment & Gold" look
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Bilbo+Swash+Caps&family=MedievalSharp&display=swap');

    /* Background Image (Parchment Texture) */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/old-map.png");
        background-color: #2b1d0e; /* Dark fallback */
        background-attachment: fixed;
    }

    /* THE CURSIVE TITLE */
    .cursive-title {
        font-family: 'Bilbo Swash Caps', cursive;
        color: #FFD700; /* Gold */
        text-align: center;
        font-size: 72px !important;
        text-shadow: 3px 3px 5px #000;
        margin-bottom: 0px;
    }

    /* Subheaders and Text */
    h3, p, label {
        font-family: 'MedievalSharp', serif !important;
        color: #f4e4bc !important; /* Cream color */
    }

    /* The Question Box */
    .stInfo {
        background-color: rgba(50, 30, 10, 0.8) !important;
        border: 2px solid #FFD700 !important;
        color: #f4e4bc !important;
        border-radius: 15px;
    }

    /* Centering the Buttons */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #8b0000 !important; /* Deep Red */
        color: white !important;
        border: 2px solid #FFD700 !important;
        padding: 10px 30px;
        font-size: 20px;
    }
    
    /* Progress Bar Color */
    .stProgress > div > div > div > div {
        background-color: #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. QUIZ DATA ---
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = [
        {"quote": "All we have to decide is what to do with the time that is given us.", "correct": "Gandalf", "options": ["Elrond", "Galadriel", "Aragorn", "Gandalf"]},
        {"quote": "I can't carry it for you, but I can carry you!", "correct": "Samwise Gamgee", "options": ["Aragorn", "Merry", "Pippin", "Samwise Gamgee"]},
        {"quote": "One does not simply walk into Mordor.", "correct": "Boromir", "options": ["Aragorn", "Gimli", "Legolas", "Boromir"]},
        {"quote": "I am no man!", "correct": "Éowyn", "options": ["Arwen", "Galadriel", "Éomer", "Éowyn"]},
        {"quote": "My precious.", "correct": "Gollum", "options": ["Bilbo", "Frodo", "Sauron", "Gollum"]},
        {"quote": "Even the smallest person can change the course of the future.", "correct": "Galadriel", "options": ["Gandalf", "Elrond", "Bilbo", "Galadriel"]},
    ]
    random.shuffle(st.session_state.quiz_data)
    st.session_state.score = 0
    st.session_state.current_idx = 0

# --- 3. SIDEBAR (QUEST TRACKER) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/The_One_Ring_Inscription.svg/1200px-The_One_Ring_Inscription.svg.png")
    st.header("Quest Tracker")
    st.write(f"**Current Score:** {st.session_state.score}")
    progress = st.session_state.current_idx / len(st.session_state.quiz_data)
    st.progress(progress)
    if st.session_state.current_idx > 0:
        st.write(f"You have traveled {int(progress*100)}% of the way to Mount Doom.")

# --- 4. MAIN INTERFACE ---
st.markdown('<h1 class="cursive-title">The One Ring Trivia</h1>', unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

if st.session_state.current_idx < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_idx]
    
    st.subheader(f"Scroll {st.session_state.current_idx + 1}")
    st.info(f"### \"{item['quote']}\"")
    
    # Form for submission
    with st.form(key=f"quiz_form_{st.session_state.current_idx}"):
        user_choice = st.radio("Who spoke these words?", item['options'])
        submit = st.form_submit_button("Cast into the Fire")
        
        if submit:
            if user_choice == item['correct']:
                st.success("Correct! The light of Eärendil shines upon you.")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! It was {item['correct']}. You shall not pass!")
            
            st.session_state.current_idx += 1
            st.button("Continue the Journey")
else:
    st.balloons()
    st.markdown('<h1 class="cursive-title">The Quest is Won!</h1>', unsafe_allow_html=True)
    st.write(f"### Final Score: {st.session_state.score} / {len(st.session_state.quiz_data)}")
    
    if st.button("Start a New Quest"):
        st.session_state.current_idx = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.quiz_data)
        st.rerun()
