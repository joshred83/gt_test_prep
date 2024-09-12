import streamlit as st
from ISYE_6740_Computational_Data_Analysis import cda_mpc_big_review, cda_mpc_page1, cda_states

def intro():
    st.write("# ISYE 6740 Computational Data Analytics Review App")
    st.sidebar.success("Select a review category to begin.")

    st.markdown("""
The app features GPT-generated multiple-choice questions based on course content, lectures, and my personal notes, along with relevant questions from the course itself and similar classes from other institutions.
I began creating tools like this because I believe that actively recalling information is a more effective way to learn than simply reviewing course material.

1. **Chapter Review**: Select specific chapters to review and answer questions related to those chapters.
2. **Big Review**: Select multiple chapters for a comprehensive review session.

### Additional Resources:
- [The Elements of Statistical Learning](https://hastie.su.domains/Papers/ESLII.pdf)
- [Bishop - Pattern recognition and Machine learning](https://www.academia.edu/44025931/Pattern_recognition_and_Machine_learning)
- [Cornell Machine Learning Lectures - YouTube](https://www.youtube.com/watch?v=MrLPzBxG95I&list=PLl8OlHZGYOQ7bkVbuRthEsaLr7bONzbXS)
- [Lecture Transcripts](https://docs.google.com/document/d/1gwVNENEzxL45mlCm2Oy_p61ElFqfiqQB/edit#heading=h.2v13rmc85j9c)

Check out my other review apps for:
- [ISYE 6501 Introduction to Analytics Modeling](https://isye6501test-prep.streamlit.app/)
- [MGT 6203 Analytics for Business](https://mgt-6203-mt-study-aid.streamlit.app/)
- [ISYE 6740 Computational Data Analytics](https://cda-review-app.streamlit.app/)
- [CS 7643 Deep Learning](https://deep-learning-practice.streamlit.app/)
- [CS 7280 Network Science Review App](https://network-science-review.streamlit.app/)
    """)

def chapter_review():
    st.markdown("# Chapter Review")
    st.write('Select chapters to review and answer questions. Refresh Page to load new questions.')
    cda_mpc_page1.sa_questions()

def big_review():
    st.markdown("# Big Review")
    st.write('Comprehensive review with selectable chapters. Refresh Page to load new questions.')
    cda_mpc_big_review.big_review()

def reset_or_initialize_state():
    # Reset any specific state variables related to the review types
    keys_to_delete = ['token', 'chapter_review_state', 'big_review_state']
    for key in keys_to_delete:
        if key in st.session_state:
            del st.session_state[key]

page_names_to_funcs = {
    "—": intro,
    "Lesson Review": chapter_review,
    "Big Review": big_review
}

# Initialize session state for selected demo
if 'current_demo' not in st.session_state:
    st.session_state['current_demo'] = None

# Sidebar selection box
demo_name = st.sidebar.selectbox("Choose Review Type", list(page_names_to_funcs.keys()), index=0)

# Check if the demo selection has changed
if st.session_state['current_demo'] != demo_name:
    st.session_state['current_demo'] = demo_name  # Update the current demo
    reset_or_initialize_state()  # Reset or initialize state based on new selection

# Dynamically call the selected demo function
if demo_name in page_names_to_funcs:
    page_names_to_funcs[demo_name]()
