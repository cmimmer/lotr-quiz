import streamlit as st
import random

# Initializing the quiz data
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = [
        {"quote": "All we have to decide is what to do with the time that is given us.", "correct": "Gandalf", "options": ["Elrond", "Galadriel", "Aragorn", "Gandalf"]},
        {"quote": "I can't carry it for you, but I can carry you!", "correct": "Samwise Gamgee", "options": ["Aragorn", "Merry", "Pippin", "Samwise Gamgee"]},
        {"quote": "One does not simply walk into Mordor.", "correct": "Boromir", "options": ["Aragorn", "Gimli", "Legolas", "Boromir"]},
        {"quote": "I am no man!", "correct": "Éowyn", "options": ["Arwen", "Galadriel", "Éomer", "Éowyn"]},
    ]
    random.shuffle(st.session_state.quiz_data)
    st.session_state.score = 0
    st.session_state.current_idx = 0

st.title("🧙‍♂️ Middle-earth Quote Quiz")

if st.session_state.current_idx < len(st.session_state.quiz_data):
    item = st.session_state.quiz_data[st.session_state.current_idx]
    
    st.subheader(f"Question {st.session_state.current_idx + 1}")
    st.info(f"\"{item['quote']}\"")
    
    with st.form(key=f"quiz_form_{st.session_state.current_idx}"):
        # We shuffle the list of options so the correct answer isn't always in the same spot
        options = item['options']
        user_choice = st.radio("Who said it?", options)
        submit = st.form_submit_button("Submit Answer")
        
        if submit:
            if user_choice == item['correct']:
                st.success("Correct! ✨")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! It was {item['correct']}.")
            
            st.session_state.current_idx += 1
            st.button("Next Question")
else:
    st.balloons()
    st.header("Quiz Finished!")
    st.write(f"Your final score: {st.session_state.score}/{len(st.session_state.quiz_data)}")
    if st.button("Restart Quiz"):
        st.session_state.current_idx = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.quiz_data)
        st.rerun()

