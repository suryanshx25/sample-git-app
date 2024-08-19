import streamlit as st

st.title('CampusX')

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
option = st.sidebar.selectbox('Select one', ['teacher', 'student'])
btn = st.sidebar.button('select')

 if btn:
     st.title("hello " + option)