import streamlit as st

st.set_page_config(page_title="Mentorship Survey")

# ---------------- STATE ---------------- #

if "step" not in st.session_state:
    st.session_state.step = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

# ---------------- QUESTIONS ---------------- #

questions = [
    "How often do you approach lecturers for clarification after class?",
    "How comfortable are you asking seniors for academic advice?",
    "How frequently do you seek feedback on your assignments?",
    "Do you actively look for mentors in your field of study?",
    "How often do you participate in academic discussions with peers?",
    "How confident are you in reaching out for help when struggling?",
    "How often do you attend academic support sessions or workshops?",
    "Do you follow up on advice given by mentors?",
    "How satisfied are you with the guidance provided by lecturers?",
    "How useful do you find advice from fellow students?",
    "How often do you receive constructive feedback on your work?",
    "How supported do you feel in your academic journey?",
    "How often do you independently search for academic guidance resources?",
    "Do you feel your mentors understand your academic needs?",
    "How likely are you to recommend your mentor to others?"
]

options = {
    "Always": 0,
    "Often": 1,
    "Sometimes": 2,
    "Rarely": 3,
    "Never": 4
}

# ---------------- STEP 1 ---------------- #

if st.session_state.step == 1:
    st.title("Mentorship Survey")

    name = st.text_input("Full Name")
    dob = st.text_input("Date of Birth (DD/MM/YYYY)")
    student_id = st.text_input("Student ID")

    if st.button("Next"):
        if not name or not dob or not student_id:
            st.error("Please fill all fields")
        else:
            st.session_state.name = name
            st.session_state.dob = dob
            st.session_state.student_id = student_id
            st.session_state.step = 2

# ---------------- STEP 2 ---------------- #

elif st.session_state.step == 2:
    st.title("Survey Questions")

    answers = []

    for i, q in enumerate(questions):
        answer = st.radio(f"Q{i+1}. {q}", list(options.keys()), key=i)
        answers.append(options[answer])

    if st.button("Submit"):
        st.session_state.score = sum(answers)
        st.session_state.step = 3

# ---------------- STEP 3 ---------------- #

elif st.session_state.step == 3:
    score = st.session_state.score

    if score <= 12:
        result = "Very High Mentorship Engagement"
    elif score <= 24:
        result = "High Mentorship Engagement"
    elif score <= 36:
        result = "Moderate Engagement"
    elif score <= 48:
        result = "Low Engagement"
    else:
        result = "Very Low Engagement"

    st.title("Result")
    st.write("Score:", score)
    st.write("Category:", result)

    if st.button("Restart"):
        st.session_state.step = 1
