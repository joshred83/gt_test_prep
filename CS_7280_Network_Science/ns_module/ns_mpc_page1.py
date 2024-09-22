import streamlit as st
from .ns_states import Token

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
    initial_options = {"L1 - What is Network Science?": '1', 
                       "L2 - Relevant Concepts from Graph Theory": '2',
                        "L3 - Degree Distribution and The “Friendship Paradox”": '3',
                        "L4 - Random vs. Real Graphs and Power-Law Networks": '4',
                        "L5 - Network Paths, Clustering and The “Small World” Property": '5',}
    
    topics = {
    "L1 - What is Network Science?": '1',
    "L2 - Relevant Concepts from Graph Theory": '2',
    "L3 - Degree Distribution and The “Friendship Paradox”": '3',
    "L4 - Random vs. Real Graphs and Power-Law Networks": '4',
    "L5 - Network Paths, Clustering and The “Small World” Property": '5',
    "L6 - Centrality and Network-core Metrics and Algorithms": '6',
    "L7 - Modularity and Community Detection": '7',
    "L8 - Advanced Topics in Community Detection": '8',
    "L9 - Spreading Phenomena on Networks and Epidemics": '9',
    "L10 - Social Influence and Other Network Contagion Phenomena": '10',
    "L11 - Other Network Dynamic Processes": '11',
    "L12 - Network Modeling": '12',
    "L13 - Statistical Analysis of Network Data": '13',
    "L14 - Machine Learning in Network": '14'
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
            if q['correct_answer'] in ['True', 'False']:
                correct_answer = q['correct_answer']
            if q['correct_answer'] not in ['True', 'False']:
                correct_answer_letter = q['correct_answer']  
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
