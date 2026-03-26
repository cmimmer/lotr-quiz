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

# --- 3. CUSTOM CSS FOR THE "READABILITY SCRIM" & THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bilbo+Swash+Caps&family=MedievalSharp&display=swap');

    /* The dark container that makes text readable over the map */
    .readability-scrim {
        background-color: rgba(15, 10, 5, 0.88); 
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #FFD700;
        box-shadow: 0 10px 30px rgba(0,0,0,0.9);
        margin-bottom: 20px;
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
        color: #f7e9cd !important;
        text-shadow: 1px 1px 2px #000;
    }

    .stInfo {
        background-color: rgba(45, 30, 15, 1.0) !important;
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
        background-color: rgba(30, 20, 10, 0.95);
    }
    
    .stProgress > div > div > div > div {
        background-color: #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. JOURNEY LOCATIONS (20 STEPS) ---
LOCATIONS = [
    "The Shire (Bag End)", "Bucklebury Ferry", "Bree (The Prancing Pony)", 
    "Weathertop (Amon Sûl)", "Trollshaws", "Rivendell", "Redhorn Pass", 
    "Moria (West Gate)", "Bridge of Khazad-dûm", "Lothlórien", 
    "Argonath (Pillars of Kings)", "Amon Hen", "Emyn Muil", "The Dead Marshes", 
    "The Black Gate", "Ithilien", "Minas Morgul", "Shelob's Lair", 
    "Plateau of Gorgoroth", "Mount Doom"
]

# --- 5. QUIZ DATA (20 QUESTIONS) ---
QUESTIONS = [
    {"quote": "All we have to decide is what to do with the time that is given us.", "correct": "Gandalf", "options": ["Elrond", "Galadriel", "Aragorn", "Gandalf"]},
    {"quote": "I can't carry it for you, but I can carry you!", "correct": "Samwise Gamgee", "options": ["Aragorn", "Merry", "Pippin", "Samwise Gamgee"]},
    {"quote": "One does not simply walk into Mordor.", "correct": "Boromir", "options": ["Aragorn", "Gimli", "Legolas", "Boromir"]},
    {"quote": "I am no man!", "correct": "Éowyn", "options": ["Arwen", "Galadriel", "Éomer", "Éowyn"]},
    {"quote": "My precious.", "correct": "Gollum", "options": ["Bilbo", "Frodo", "Sauron", "Gollum"]},
    {"quote": "Even the smallest person can change the course of the future.", "correct": "Galadriel", "options": ["Gandalf", "Elrond", "Bilbo", "Galadriel"]},
    {"quote": "Po-ta-toes! Boil 'em, mash 'em, stick 'em in a stew.", "correct": "Samwise Gamgee", "options": ["Gollum", "Merry", "Pippin", "Samwise Gamgee"]},
    {"quote": "Not all those who wander are lost.", "correct": "Bilbo Baggins", "options": ["Aragorn", "Gandalf", "Frodo", "Bilbo Baggins"]},
    {"quote": "Fly, you fools!", "correct": "Gandalf", "options": ["Saruman", "Boromir", "Aragorn", "Gandalf"]},
    {"quote": "For Frodo.", "correct": "Aragorn", "options": ["Sam", "Legolas", "Gimli", "Aragorn"]},
    {"quote": "I would have followed you, my brother... my captain... my king.", "correct": "Boromir", "options": ["Faramir", "Aragorn", "Legolas", "Boromir"]},
    {"quote": "A wizard is never late, Frodo Baggins.", "correct": "Gandalf", "options": ["Saruman", "Radagast", "Bilbo", "Gandalf"]},
    {"quote": "There is some good in this world, Mr. Frodo, and it’s worth fighting for.", "correct": "Samwise Gamgee", "options": ["Gandalf", "Aragorn", "Galadriel", "Samwise Gamgee"]},
    {"quote": "Looks like meat's back on the menu, boys!", "correct": "Uglúk", "options": ["Lurtz", "Gothmog", "Grishnákh", "Uglúk"]},
    {"quote": "You shall not pass!", "correct": "Gandalf", "options": ["Aragorn", "Elrond", "Galadriel", "Gandalf"]},
    {"quote": "The board is set, the pieces are moving.", "correct": "Gandalf", "options": ["Saruman", "Denethor", "Elrond", "Gandalf"]},
    {"quote": "I don't know half of you half as well as I should like.", "correct": "Bilbo Baggins", "options": ["Gandalf", "Frodo", "Pippin", "Bilbo Baggins"]},
    {"quote": "Don't adventures ever have an end?", "correct": "Bilbo Baggins", "options": ["Frodo", "Sam", "Aragorn", "Bilbo Baggins"]},
    {"quote": "My friends, you bow to no one.", "correct": "Aragorn", "options": ["Gandalf", "Elrond", "Théoden", "Aragorn"]},
    {"quote": "It’s gone. It’s done.", "correct": "Frodo Baggins", "options": ["Sam", "Gollum", "Aragorn", "Frodo Baggins"]},
]

# Initialize Session State
if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.quiz_data = QUESTIONS.copy()
    random.shuffle(st.session_state.quiz_data)

# --- 6. SIDEBAR SETTINGS ---
with st.sidebar:
    st.header("⚙️ Adventure Settings")
    
    # Music Toggle
    music_on = st.toggle("🎵 Background Music", value=False)
    if music_on:
        st.audio("http://soundimage.org/wp-content/uploads/2014/04/Fantascape.mp3", format="audio/mp3", autoplay=True, loop=True)
    
    # Difficulty Selector (Hard Mode Re-included)
    difficulty = st.radio("Difficulty Level", ["Easy (Multiple Choice)", "Hard (Text Input)"])
    
    st.divider()
    
    # Journey Progress (Re-included)
    st.header("📜 Quest Progress")
    current_loc = LOCATIONS[st.session_state.current_idx] if st.session_state.current_idx < 20 else "Mount Doom"
    st.subheader(f"📍 {current_loc}")
    
    progress = st.session_state.current_idx / 20
    st.progress(progress)
    st.write(f"**Score:** {st.session_state.score} / 20")
    if st.session_state.current_idx > 0:
        st.write(f"You have traveled {int(progress*100)}% of the way to Mordor.")

# --- 7. MAIN UI ---
st.markdown('<div class="readability-scrim">', unsafe_allow_html=True)
st.markdown('<h1 class="cursive-title">The One Ring Trivia</h1>', unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

if st.session_state.current_idx < 20:
    item = st.session_state.quiz_data[st.session_state.current_idx]
    
    st.subheader(f"Encounter {st.session_state.current_idx + 1}")
    st.info(f"### \"{item['quote']}\"")
    
    with st.form(key=f"quiz_form_{st.session_state.current_idx}"):
        # Toggle between radio and text input based on sidebar selection
        if difficulty == "Easy (Multiple Choice)":
            user_choice = st.radio("Who spoke these words?", item['options'])
        else:
            user_choice = st.text_input("Type the character's full name:")

        submit = st.form_submit_button("Cast into the Fire")
        
        if submit:
            correct_name = item['correct']
            # Validation for both modes
            if (difficulty == "Easy (Multiple Choice)" and user_choice == correct_name) or \
               (difficulty == "Hard (Text Input)" and user_choice.strip().lower() == correct_name.lower()):
                st.success("Correct! The light of Eärendil shines upon you. ✨")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! It was {correct_name}. ❌")
            
            st.session_state.current_idx += 1
            st.form_submit_button("Next Trial")

else:
    st.balloons()
    st.markdown('<h1 class="cursive-title">Quest Won!</h1>', unsafe_allow_html=True)
    st.write(f"### Final Score: {st.session_state.score} / 20")
    
    if st.button("Start New Quest"):
        st.session_state.current_idx = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.quiz_data)
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
