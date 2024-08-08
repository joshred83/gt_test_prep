import streamlit as st
from .ns_states import Token

# Define the list of chapters 
chapters = [
    'L1 - What is Network Science?',
    'L2 - Relevant Concepts from Graph Theory',
    'L3 - Degree Distribution and The “Friendship Paradox”',
    'L4 - Random vs. Real Graphs and Power-Law Networks',
    'L5 - Network Paths, Clustering and The “Small World” Property',
    'L6 - Centrality and Network-core Metrics and Algorithms',
    'L7 - Modularity and Community Detection',
    'L8 - Advanced Topics in Community Detection',
    'L9 - Spreading Phenomena on Networks and Epidemics',
    'L10 - Social Influence and Other Network Contagion Phenomena',
    'L11 - Other Network Dynamic Processes',
    'L12 - Network Modeling',
    'L13 - Statistical Analysis of Network Data',
    'L14 - Machine Learning in Network'
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

# Function to create checkboxes for chapters
def create_checkboxes(chapters, columns=2, preselected=None):
    if preselected is None:
        preselected = []
    selected_chapters = []
    cols = st.columns(columns)
    for index, chapter in enumerate(chapters):
        col = cols[index % columns]
        # Preselect specified chapters by setting the value parameter to True if the chapter is in the preselected list
        is_selected = col.checkbox(chapter, key=chapter, value=chapter in preselected)
        if is_selected:
            selected_chapters.append(index)  # Add zero-based index
    return selected_chapters

def big_review():
    # Ensure the token is initialized with state 'all'
    if 'token' not in st.session_state:
        st.session_state.token = Token(STATE='all')
        st.session_state.questions_initialized = False

    # Display chapters for review with checkboxes
    st.title("Select Chapters for Review")
    preselected_chapters = []  # List any chapters you want to preselect if needed
    selected_chapters = create_checkboxes(chapters, preselected=preselected_chapters)

    if st.button('Submit Chapters') or st.session_state.questions_initialized:
        if not st.session_state.questions_initialized:
            st.session_state.token.chapters_to_review = [index for index in selected_chapters]
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
