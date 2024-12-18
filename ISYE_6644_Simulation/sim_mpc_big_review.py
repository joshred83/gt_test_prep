import streamlit as st
from .sim_states import Token

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
        st.session_state.token = Token()
        st.session_state.questions_initialized = False

    st.title("Select a Review Type")

    review_mapping = {
        "ISYE 6739 Midterm 1 (Modules 0-2)": "ISYE_6739_Midterm1",
        "ISYE 6739 Midterm 2 (Modules 0-5)": "ISYE_6739_Midterm2",
        "ISYE 6739 Final (All Modules)": "ISYE_6739_Final",
        # "ISYE 6644 Midterm 1 (Modules 1-5)": "Midterm_1",
        # "ISYE 6644 Midterm 2 (Modules 1-7)": "Midterm_2",
        # "ISYE 6644 Final (All Modules)": "Final"
    }

    review_choice = st.radio("Choose a review type", options=list(review_mapping.keys()))
    selected_state = review_mapping[review_choice]

    if st.button('Start Review') or st.session_state.questions_initialized:
        if not st.session_state.questions_initialized:
            try:
                st.session_state.token = Token(STATE=selected_state)
                st.session_state.token.initialize_mpc_questions()
                st.session_state.questions = st.session_state.token.mpc_questions
                st.session_state.questions_initialized = True
            except ValueError as e:
                st.error(f"Error: {e}")
                return

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
                if 'chapter_information' in q:
                    st.write(f"You can review {q['chapter_information']}")

if __name__ == "__main__":
    big_review()
