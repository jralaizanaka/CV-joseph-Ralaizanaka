import streamlit as st

from PIL import Image

if st.session_state.vers == 'française':
    version = "française"
elif st.session_state.vers == 'english':
    version = "english"

if version == "française":
    image = Image.open('Education.PNG')
    st.sidebar.markdown("# Formation")
    st.image(image)

else:
    image = Image.open('Education.eng.PNG')
    st.sidebar.markdown("# Education")
    st.image(image)