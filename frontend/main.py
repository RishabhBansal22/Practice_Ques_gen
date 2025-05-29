import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from app.generator import generate_response


st.title("Generate Practice Questions")

with st.form("input form"):
    Context = st.text_area("Define Your Purpose", placeholder="Computer Science")
    topic = st.text_area("Enter Topic", placeholder= "Linear Algebra")
    subtopic = st.text_area("Enter Subtopics", placeholder="Please Enter subtopics (comma-seprated)".capitalize())
    Num_questions = st.number_input("No. Of Questions", min_value=1, max_value=20,)
    difficulty = st.selectbox("Select Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
    submit = st.form_submit_button("Generate Questions")

subtopic_list = [t.strip() for t in subtopic.split(",")]

prompt = F'''Generate {Num_questions} practice questions on the topic "{topic}".
Subtopics: {', '.join(subtopic_list)}
Context: {Context}
Difficulty level: {difficulty}

Guidelines:
- Questions must be relevant to the topic and subtopics.
- Ensure the questions comprehensively test the user's understanding across the subject and subtopics.
- Match the specified difficulty level.
- Use the context to tailor the questions.
- Format the output as a numbered list.
- Do not repeat questions.'''

if submit:
    if topic and Num_questions:
        ai_response = generate_response(prompt)
    else:
        st.markdown("Please Enter Topic and Number of Questions")

    st.markdown("### Generated Practice Questions")
    st.write(ai_response)







