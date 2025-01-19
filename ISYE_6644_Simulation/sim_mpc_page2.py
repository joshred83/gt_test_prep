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

def sim_questions():
    # st.write('Comimg Soon!')
    apply_custom_css()

    if 'token' not in st.session_state:
        st.session_state.token = Token()
        st.session_state.questions_initialized = False

    st.markdown("### Please select a Simulation Module to proceed:")

    module_mapping = {
        "Module 1: Whirlwind Tour of Simulation": 'SIM_1',
        "Module 2: Bootcamps": 'SIM_2',
        "Module 3: Hand Simulations": 'SIM_3',
        # "Module 4: General Simulation Principles": 'SIM_4',
        # "Module 5: The Arena Simulation Language": 'SIM_5',
        # "Module 6: Random Number Generation": 'SIM_6',
        # "Module 7: Random Variate Generation": 'SIM_7',
        # "Module 8: Input Analysis": 'SIM_8',
        # "Module 9: Output Analysis": 'SIM_9',
        # "Module 10: Comparing Systems": 'SIM_10'
    }

    selected_module = st.radio(label=' ', options=list(module_mapping.keys()), label_visibility="collapsed")

    if st.button("Proceed"):
        try:
            st.session_state.STATE = module_mapping[selected_module]
            st.session_state.token = Token(STATE=st.session_state.STATE)
            st.session_state.token.initialize_mpc_questions()
            st.session_state.questions = st.session_state.token.mpc_questions
            st.session_state.questions_initialized = True
        except ValueError as e:
            st.error(f"Error: {e}")
            return

    if st.session_state.questions_initialized:
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
    sim_questions()
