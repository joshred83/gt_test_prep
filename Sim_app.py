import streamlit as st
from ISYE_6644_Simulation.sim_mpc_big_review import big_review
from ISYE_6644_Simulation.sim_mpc_page1 import review_questions
from ISYE_6644_Simulation.sim_mpc_page2 import sim_questions

def intro():
    st.write("# ISYE 6644 Simulation and Modeling Review App")
    st.sidebar.success("Select a review category to begin.")

    st.markdown("""
The app features multiple-choice questions based on course content, lectures, and personal notes from ISYE 6644: Simulation and Modeling for Engineering and Science.
I created this tool because active recall is an effective learning strategy.

1. **ISYE 6739 Prob Review**: Review key probability concepts from ISYE 6739.
2. **ISYE 6644 Module Review**: Review modules from ISYE 6644 Simulation and Modeling.
3. **Midterm Practice**: Comprehensive review covering multiple modules.

### Additional Resources:
- [Harvard Stat 110 Problems](https://projects.iq.harvard.edu/stat110/strategic-practice-problems)
- [Goldsman ISYE 6739 - Probability and Statistics](https://www2.isye.gatech.edu/~sman/courses/6739/)
- [ISYE 6739 Lectures](https://www.kaltura.com/index.php/extwidget/preview/partner_id/2019031/uiconf_id/43497241/embed/iframe?flashvars[playlistAPI.kpl0Id]=1_g5xwvbde)
- [Harvard Stat 110 Lectures](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo)
- [MIT Probability Lectures](https://www.youtube.com/watch?v=1uW3qMFA9Ho&list=PLUl4u3cNGP60hI9ATjSFgLZpbNJ7myAg6)
- [MIT Probability Course on edX](https://www.edx.org/learn/probability/massachusetts-institute-of-technology-probability-the-science-of-uncertainty-and-data)

Check out other review apps for related courses:
- [ISYE 6501 Introduction to Analytics Modeling](https://isye6501test-prep.streamlit.app/)
- [MGT 6203 Analytics for Business](https://mgt-6203-mt-study-aid.streamlit.app/)
- [ISYE 6740 Computational Data Analytics](https://cda-review-app.streamlit.app/)
- [CS 7643 Deep Learning](https://deep-learning-practice.streamlit.app/)
- [CS 7280 Network Science Review App](https://network-science-review.streamlit.app/)
    """)

def chapter_review():
    st.markdown("# ISYE 6739 Probability Module Review")
    st.write('Remember, the set of good songs and the set of Justin Bieber songs are disjoint.')
    review_questions()

def module_review():
    st.markdown("# ISYE 6644 Simulation Module Review")
    st.write('Reload App for new Questions')
    sim_questions()

def comprehensive_review():
    st.markdown("# Exam Prep")
    st.write('Reload App for new Questions')
    big_review()

def reset_or_initialize_state():
    keys_to_delete = ['token', 'chapter_review_state', 'comprehensive_review_state']
    for key in keys_to_delete:
        if key in st.session_state:
            del st.session_state[key]

page_names_to_funcs = {
    "—": intro,
    "ISYE 6739 Prob Module Review": chapter_review,
    "ISYE 6644 Module Review": module_review,
    "Exam Practice (6739 & 6644)": comprehensive_review
}

if 'current_demo' not in st.session_state:
    st.session_state['current_demo'] = None

demo_name = st.sidebar.selectbox("Choose Review Type", list(page_names_to_funcs.keys()), index=0)

if st.session_state['current_demo'] != demo_name:
    st.session_state['current_demo'] = demo_name
    reset_or_initialize_state()

if demo_name in page_names_to_funcs:
    page_names_to_funcs[demo_name]()
