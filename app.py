import streamlit as st
import random

# --- THE "ONE RING" THEME (CSS) ---
st.set_page_config(page_title="LOTR Quote Quiz", page_icon="💍")

st.markdown("""
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: #1a1a1a;
        color: #FFD700;
    }
    /* Styling the headers */
    h1, h2, h3 {
        color: #FF4500 !important;
        text-shadow: 2px 2px #000000;
        font-family: 'Georgia', serif;
    }
    /* Styling the quote box */
    .stInfo {
        background-color: #2b2b2b !important;
        color: #FFD700 !important;
        border: 2px solid #FF4500 !important;
        border-radius: 15px;
    }
    /* Customizing buttons */
    .stButton>button {
        background-color: #FFD700 !important;
        color: black !important;
        font-weight: bold;
        border-radius: 20px;
        border: 2px solid #FF4500;
    }
    .stButton>button:hover {
        background-color: #FF4500 !important;
        color: white !important;
    }
    /* Radio button text color */
    div[role="radiogroup"] label {
        color: #FFD700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- QUIZ DATA ---
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = [
        {"quote": "All we have to decide is what to do with the time that is given us.", "correct": "Gandalf", "options": ["Elrond", "Galadriel", "Aragorn", "Gandalf"]},
        {"quote": "I can't carry it for you, but I can carry you!", "correct": "Samwise Gamgee", "options": ["Aragorn", "Merry", "Pippin", "Samwise Gamgee"]},
        {"quote": "One does not simply walk into Mordor.", "correct": "Boromir", "options": ["Aragorn", "Gimli", "Legolas", "Boromir"]},
        {"quote": "I am no man!", "correct": "Éowyn", "options": ["Arwen", "Galadriel", "Éomer", "Éowyn"]},
        {"quote": "My precious.", "correct": "Gollum", "options": ["Bilbo", "Frodo", "Sauron", "Gollum"]},
    ]
    random.shuffle(st.session_state.quiz_data)
    st.session_state.score = 0
    st.session_state.current_idx = 0

# --- THE UI ---
st.title("💍 The One Ring Trivia")
st.write("---")

if st.session_state.current_idx < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_idx]
    
    st.subheader(f"Scroll {st.session_state.current_idx + 1}")
    st.info(f"*{item['quote']}*")
    
    with st.form(key=f"quiz_form_{st.session_state.current_idx}"):
        user_choice = st.radio("Who spoke these words?", item['options'])
        submit = st.form_submit_button("Cast into the Fire")
        
        if submit:
            if user_choice == item['correct']:
                st.success("Correct! The light of Eärendil shines upon you. ✨")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! It was {item['correct']}. To the dungeons with you!")
            
            st.session_state.current_idx += 1
            st.button("Next Trial")
else:
    st.balloons()
    st.header("The Quest is Complete!")
    st.subheader(f"Your final score: {st.session_state.score}/{len(st.session_state.quiz_data)}")
    
    if st.session_state.score == len(st.session_state.quiz_data):
        st.write("🏆 You are a true Lore-master of Middle-earth!")
    else:
        st.write("Keep studying the ancient scrolls...")

    if st.button("Start a New Quest"):
        st.session_state.current_idx = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.quiz_data)
        st.rerun()
