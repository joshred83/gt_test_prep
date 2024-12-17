import streamlit as st
from sim_states import Token
import os

def apply_custom_css():
    custom_css = """
    <style>
        .question-style {
            font-size: 20px; 
            font-weight: bold; 
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def question_generator(label, options, question_key):
    return st.radio(label='Please select the correct answer', options=options, key=question_key)

def big_review():
    apply_custom_css()

    if 'token' not in st.session_state:
        st.session_state.token = Token(STATE='all')
        st.session_state.questions_initialized = False

    st.title("Select a Review Type")

    review_mapping = {
        "ISYE 6739 Final": ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
        "Midterm 1 (Modules 1-5)": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5'],
        "Midterm 2 (Modules 1-7)": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5', 'SIM_6', 'SIM_7'],
        "Final (All Modules)": ['SIM_1', 'SIM_2', 'SIM_3', 'SIM_4', 'SIM_5', 'SIM_6', 'SIM_7', 'SIM_8', 'SIM_9', 'SIM_10']
    }

    review_choice = st.radio("Choose a review type", options=list(review_mapping.keys()))
    selected_lessons = review_mapping[review_choice]

    if st.button('Start Review') or st.session_state.questions_initialized:
        if not st.session_state.questions_initialized:
            st.session_state.token.chapters_to_review = selected_lessons
            st.session_state.token.initialize_mpc_questions()
            st.session_state.questions = st.session_state.token.mpc_questions
            st.session_state.questions_initialized = True

        questions = st.session_state.questions

        for i, q in enumerate(questions):
            st.markdown('-------------------------------')
            st.markdown(f"**{q['question']}**")
            options = q['options_list']
            correct_answer = q['correct_answer']
            explanation = q.get('explanation', " ")
            question_key = f"question_{i}"

            selected_answer = question_generator(q['question'], options, question_key)

            if st.button('Submit', key=f"submit_{i}"):
                if selected_answer == correct_answer:
                    st.success('Great work!')
                    st.info(f'Explanation: \n\n{explanation}')
                else:
                    st.error(f"The correct answer was {correct_answer}")
                    st.info(f'Explanation: \n\n{explanation}')

if __name__ == "__main__":
    big_review()
