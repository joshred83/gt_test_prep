import streamlit as st
from .rl_states import Token

# Define the list of lessons as per the image
lessons = [
    'Lesson 1: Linear Classifiers and Gradient Descent',
    'Lesson 2: Neural Networks',
    'Lesson 3: Optimization of Deep Neural Networks',
    'Lesson 4: Data Wrangling',
    'Lesson 5: Convolution and Pooling Layers',
    'Lesson 6: Convolutional Neural Networks',
    'Lesson 7: Visualization',
    'Lesson 8: Scalable Training',
    'Lesson 9: Advanced Computer Vision Applications',
    'Lesson 10: Responsible AI and Bias and Fairness',
    'Lesson 11: Introduction to Structured Data',
    'Lesson 12: Language Models',
    'Lesson 13: Embeddings',
    'Lesson 14: Neural Attention Models',
    'Lesson 15: Neural Machine Translation',
    'Lesson 16: Advanced Topics: Translation',
    'Lesson 17: Deep Reinforcement Learning',
    'Lesson 18: Unsupervised and Semi-Supervised Learning',
    'Lesson 19: Generative Models'
]

lessons = [
    'Lesson 1: Linear Classifiers and Gradient Descent',
    'Lesson 2: Neural Networks',
]

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

# Function to create checkboxes for lessons
def create_checkboxes(lessons, columns=2, preselected=None):
    if preselected is None:
        preselected = []
    selected_lessons = []
    cols = st.columns(columns)
    for index, lesson in enumerate(lessons):
        col = cols[index % columns]
        # Preselect specified lessons by setting the value parameter to True if the lesson is in the preselected list
        is_selected = col.checkbox(lesson, key=lesson, value=lesson in preselected)
        if is_selected:
            selected_lessons.append(index)  # Add zero-based index
    return selected_lessons

def big_review():
    # Ensure the token is initialized with state 'all'
    if 'token' not in st.session_state:
        st.session_state.token = Token(STATE='all')
        st.session_state.questions_initialized = False

    # Display lessons for review with checkboxes
    st.title("Select Lessons for Review")
    preselected_lessons = []  # List any lessons you want to preselect if needed
    selected_lessons = create_checkboxes(lessons, preselected=preselected_lessons)

    if st.button('Submit Lessons') or st.session_state.questions_initialized:
        if not st.session_state.questions_initialized:
            st.session_state.token.chapters_to_review = [index for index in selected_lessons]
            st.session_state.token.initialize_mpc_questions()
            st.session_state.questions = st.session_state.token.mpc_questions
            st.session_state.questions_initialized = True

        questions = st.session_state.questions

        for i, q in enumerate(questions, start=0):
            label = q['question']
            options = q['options_list']
            correct_answer = q['correct_answer']
            question_key = f"question_{i}"
            explanation = q['explanation']

            st.markdown('-------------------------------')
            st.markdown(f'<div class="question-style">{label}</div>', unsafe_allow_html=True)

            question = question_generator(label, options, question_key)

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
