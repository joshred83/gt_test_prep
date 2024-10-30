import streamlit as st
from .dl_states import Token
import os
# Map quizzes to their corresponding lesson indices
quiz_mapping = {
    "Quiz 1": [0, 1],  # Corresponds to Lesson 1 and Lesson 2
    "Quiz 2": [2, 4], # subtract 1
    "Quiz 3": [4, 5, 6, 8],  # subtract 1
    "Quiz 4": [10,12,13,14], # subtract 1
} 

def question_generator(label, options, question_key):
    question = st.radio(label=' ', options=options, key=question_key)
    return question

def big_review():
    # Ensure the token is initialized with state 'all'
    if 'token' not in st.session_state:
        st.session_state.token = Token(STATE='all')
        st.session_state.questions_initialized = False

    # Select Quiz
    st.title("Select a Quiz")
    quiz_choice = st.radio("Choose a quiz", options=["Quiz 1", "Quiz 2","Quiz 3","Quiz 4" ])

    # Get lessons for the selected quiz
    selected_quiz_lessons = quiz_mapping[quiz_choice]

    # When the button is clicked, initialize questions based on the selected quiz
    if st.button('Start Quiz') or st.session_state.questions_initialized:
        if not st.session_state.questions_initialized:
            # Initialize the questions for the selected quiz
            st.session_state.token.chapters_to_review = selected_quiz_lessons
            st.session_state.token.initialize_mpc_questions()
            st.session_state.questions = st.session_state.token.mpc_questions
            st.session_state.questions_initialized = True

        questions = st.session_state.questions

        for i, q in enumerate(questions, start=0):
            label = q['question']
            options = q['options_list']
            # Correct answer handling
            correct_answer = q['correct_answer']
            
            # If the correct answer is 'True' or 'False', keep it as it is
            if correct_answer in ['True', 'False']:
                correct_answer = correct_answer
            
            # If the correct answer is a single letter ('A', 'B', 'C', or 'D'), 
            # convert it to the corresponding option
            elif correct_answer[0] in ['A', 'B', 'C', 'D'] and len(correct_answer) == 1:
                correct_answer_letter = correct_answer
                correct_answer = options[ord(correct_answer_letter) - ord('A')]
            question_key = f"question_{i}"
            explanation = ''
            if 'explanation' in q and q['explanation']:
                explanation = q['explanation']

            st.markdown('-------------------------------')
            st.markdown(f"**{label}**")

            question = question_generator(label, options, question_key)
            
            image_dir = os.path.join(os.getcwd(), 'CS_7643_Deep_Learning/')
            if 'image' in q and q['image']:
                image_path = os.path.join(image_dir, q['image'])
                # st.write(f"Current working directory: {os.getcwd()}")

                if os.path.exists(image_path):
                    st.image(image_path, use_column_width=True)
                else:
                    st.write("Image not found.")

            if st.button('Submit', key=f"submit_{i}"):
                if 'submitted_answers' not in st.session_state:
                    st.session_state.submitted_answers = {}

                st.session_state.submitted_answers[question_key] = question

                if question == correct_answer:
                    st.success('Great work!')
                    st.info(f'Explanation: \n\n{explanation}')
                else:
                    st.error(f"The correct answer was {correct_answer}")
                    st.info(f'Explanation: \n\n{explanation}')

                if 'chapter_information' in q:
                    st.write(f"You can review {q['chapter_information']}")

if __name__ == "__main__":
    big_review()
