import streamlit as st

st.title('CampusX An Online Learning Platform')

st.header('Courses offered')
st.subheader('Data Science and Machine Learning')
st.subheader('Data Analysis')
st.subheader('SQL')
st.subheader('ML')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Log in
""")
st.sidebar.selectbox('Select one' ,['teacher','student'])
st.sidebar.button('select')

st.title('hello teacher')