import streamlit as st
from .cda_states import Token

# Define the list of chapters based on the provided topics
chapters = [
    'Week 1: Introduction and Overview, Clustering and k-means',
    'Week 2: Spectral Clustering',
    'Week 3: Dimensionality Reduction and PCA',
    'Week 4: Nonlinear Dimensionality Reduction',
    'Week 5: Density Estimation',
    'Week 6: Gaussian Mixture Model and EM Algorithm',
    'Week 7: Basic of Optimization Theory',
    'Week 8: Classification Naïve Bayes and Logistic Regression',
    'Week 9: Support Vector Machine (SVM), Neural Networks',
    'Week 10: Feature Selection and Anomaly Detection',
    'Week 11: Boosting Algorithms and AdaBoost',
    'Week 12: Random Forest',
    'Week 13: Bias-Variance Tradeoff and Cross-Validation'
]

# Mapping weeks to their respective chapter indices
week_to_chapter_indices = {
    'Week 1': [0, 1],  # Week 1 corresponds to chapters at indices 1 & 2
    'Week 2': [2],     # Week 2 corresponds to chapter at index 3
    'Week 3': [3],     # Week 3 corresponds to chapter at index 4
    'Week 4': [4]      # Week 4 corresponds to chapter at index 5
}

# Custom CSS to inject into the Streamlit app for styling
st.markdown(
    """
    <style>
    .chapter {
        color: blue;
    }
    /* Add other CSS styles as needed */
    </style>
    """,
    unsafe_allow_html=True
)

def question_generator(label, options, question_key):
    question = st.radio(label='Please select the correct answer', options=options, key=question_key)
    return question

# Function to create checkboxes for chapters
def create_checkboxes(week_to_chapter_indices, chapters, columns=2, preselected=None):
    if preselected is None:
        preselected = []
    selected_chapters = []
    cols = st.columns(columns)
    
    # Loop over each week and its corresponding chapter indices
    for week, chapter_indices in week_to_chapter_indices.items():
        col = cols[list(week_to_chapter_indices.keys()).index(week) % columns]
        is_selected = col.checkbox(week, key=week, value=week in preselected)
        if is_selected:
            # Append all the chapters corresponding to the selected week
            selected_chapters.extend(chapter_indices)
    return selected_chapters

def big_review():
    # Ensure the token is initialized with state 'all'
    if 'token' not in st.session_state:
        st.session_state.token = Token(STATE='all')
        st.session_state.questions_initialized = False

    # Display chapters for review with checkboxes
    st.title("Select Weeks for Review")
    preselected_weeks = []  # List any weeks you want to preselect if needed
    selected_chapter_indices = create_checkboxes(week_to_chapter_indices, chapters, preselected=preselected_weeks)

    if st.button('Submit Chapters') or st.session_state.questions_initialized:
        if not st.session_state.questions_initialized:
            st.session_state.token.chapters_to_review = [index for index in selected_chapter_indices]
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
            # Use st.markdown to render the question, allowing LaTeX and markdown formatting
            st.markdown(f"**{label}**")

            question = question_generator(label, options, question_key)

            # Store submitted answers in session state
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
