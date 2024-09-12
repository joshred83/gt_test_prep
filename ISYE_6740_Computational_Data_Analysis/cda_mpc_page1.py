import streamlit as st
from .cda_states import Token

def apply_custom_css():
    custom_css = """
    <style>
        .question-style {
            font-size: 20px; /* Customize the font size as needed */
            font-weight: bold; /* Optional: Make the question bold */
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def question_generator(label, options, question_key):
    question = st.radio(label='Please select the correct answer', options=options, key=question_key)
    return question

def sa_questions():
    apply_custom_css()

    # Initialize token and questions only once
    if 'token' not in st.session_state:
        st.session_state.token = None
        st.session_state.questions_initialized = False

    st.markdown("### Please select a topic to proceed:")
    
    # Updated lesson names based on the images and instructions
    initial_options = {
        "Lecture 1: Introduction": '1',
        "Lecture 2: Clustering, K-means": '2',
        "Lecture 3: Spectral Clustering": '3',
        "Lecture 4: PCA": '4',
        "Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)": '5',
        "Lecture 6: Density Estimation": '6',
        "Lecture 7: Gaussian Mixture Models": '7',
        "Lecture 8: Basic Optimization": '8',
        "Lecture 9: Classification": '9',
        "Lecture 10: SVM": '10',
        "Lecture 11: Neural Networks": '11',
        "Lecture 12: Feature Selection": '12',
        "Lecture 13: Anomaly Detection": '13',
        "Lecture 14: Boosting": '14',
        "Lecture 15: Random Forest": '15',
        "Lecture 16: Bias-Variance Tradeoff": '16',
        "Lecture 17: Kernel Methods": '17',
        "Lecture 18: Introduction to Reinforcement Learning": '18',
        "Lecture 19: Final Review": '19'
    }
    
    initial_options = {
        "Lecture 1: Introduction": '1',
        "Lecture 2: Clustering, K-means": '2',
        "Lecture 3: Spectral Clustering": '3',
        "Lecture 4: PCA": '4',
        "Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)": '5',
    }
    
    selected_option = st.radio(label='', options=list(initial_options.keys()))

    if st.button("Proceed") or st.session_state.questions_initialized:
        if not st.session_state.questions_initialized:
            st.session_state.STATE = initial_options[selected_option]
            st.session_state.token = Token(STATE=st.session_state.STATE)
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
            
            # If the correct answer is a single letter ('A', 'B', 'C', or 'D'), convert it to the corresponding option
            elif correct_answer[0] in ['A', 'B', 'C', 'D'] and len(correct_answer) == 1:
                correct_answer_letter = correct_answer
                correct_answer = options[ord(correct_answer_letter) - ord('A')]
            question_key = f"question_{i}"
            explanation = q['explanation']

            st.markdown('-------------------------------')
            # Directly use st.markdown for the question text, allowing LaTeX to render
            st.markdown(f"**{label}**")

            question = question_generator(label, options, question_key)

            if st.button('Submit', key=f"submit_{i}"):
                if question == correct_answer:
                    st.success('Great work!')
                    st.info(f'Explanation: \n\n{explanation}')
                else:
                    st.error(f"The correct answer was {correct_answer}")
                    st.info(f'Explanation: \n\n{explanation}')

                if 'chapter_information' in q:
                    st.write(f"You can review {q['chapter_information']}")


if __name__ == "__main__":
    sa_questions()
