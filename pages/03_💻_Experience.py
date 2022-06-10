import streamlit as st

from PIL import Image

if st.session_state.vers == 'française':
    version = "française"
elif st.session_state.vers == 'english':
    version = "english"

if version == "française":
    image = Image.open('Experience.PNG')
    st.sidebar.markdown("# Expérience professionnelle")
    st.image(image)

else:
    image = Image.open('Experience.eng.PNG')
    st.sidebar.markdown("# Experience")
    st.image(image)

