import streamlit as st
from CS_7280_Network_Science.ns_module import ns_mpc_big_review, ns_mpc_page1, ns_states

def intro():
    st.write("# CS 7280 Network Science Review App")
    st.sidebar.success("Select a review category to begin.")

    st.markdown("""
The app features GPT-generated multiple-choice questions based on course content, lectures, and my personal notes, along with relevant questions from the course itself and similar classes from other institutions.
 I began creating tools like this because I believe that actively recalling information is a more effective way to learn than simply reviewing course material.

1. **Chapter Review**: Select specific chapters to review and answer questions related to those chapters.
2. **Big Review**: Select multiple chapters for a comprehensive review session.

### Additional Resources:
- [Yi Xiang Low's Course Notes](https://lowyx.com/posts/gt-networkscience-notes/)
- [Course Book: A-L. Barabási, Network Science, 2015](https://networksciencebook.com/)
- [Official Course Website](https://omscs.gatech.edu/cs-7280-network-science)

If you find this app useful, please consider giving it a star on GitHub: [CS7280_Review_Helper](https://github.com/gderiddershanghai/CS7280_Review_Helper). 

Or check out my other review apps for:
- [ISYE 6501 Introduction to Analytics Modeling](https://isye6501test-prep.streamlit.app/)
- [MGT 6203 Analytics for Business](https://mgt-6203-mt-study-aid.streamlit.app/)
- [ISYE 6740 Computational Data Analytics](https://cda-review-app.streamlit.app/) (not updated)
- [CS 7643 Deep Learning](https://deep-learning-practice.streamlit.app/) 
- [CS 7280 Network Science Review App](https://network-science-review.streamlit.app/) (not updated)
- [ISYE 6644 & 6739 Sim and Prob/Stats Review App](https://gt-sim-prob-prep.streamlit.app/) 
    """)

def chapter_review():
    st.markdown("# Chapter Review")
    st.write('Select chapters to review and answer questions.')
    ns_mpc_page1.sa_questions()

def big_review():
    st.markdown("# Big Review")
    st.write('Comprehensive review with selectable chapters.')
    ns_mpc_big_review.big_review()

def reset_or_initialize_state():
    keys_to_delete = ['token', 'chapter_review_state', 'big_review_state']
    for key in keys_to_delete:
        if key in st.session_state:
            del st.session_state[key]

page_names_to_funcs = {
    "—": intro,
    "Chapter Review": chapter_review,
    "Big Review": big_review
}

if 'current_demo' not in st.session_state:
    st.session_state['current_demo'] = None

# Sidebar selection box
demo_name = st.sidebar.selectbox("Choose Review Type", list(page_names_to_funcs.keys()), index=0)

# Check if the demo has changed
if st.session_state['current_demo'] != demo_name:
    st.session_state['current_demo'] = demo_name  # Update the current demo
    reset_or_initialize_state()  # Reset or initialize state based on new demo

# Dynamically call the selected demo function
if demo_name in page_names_to_funcs:
    page_names_to_funcs[demo_name]()
