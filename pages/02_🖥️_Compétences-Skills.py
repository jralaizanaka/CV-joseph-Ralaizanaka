import streamlit as st

from PIL import Image

st.set_page_config(
    page_title="CV Joseph Ralaizanaka",
    page_icon="📄",
    layout="wide",
)

if st.session_state.vers == 'française':
    version = "française"
elif st.session_state.vers == 'english':
    version = "english"

if version == "française":
    image = Image.open('skills.PNG')
    st.sidebar.markdown("# Compétences")
    st.image(image)

else:
    image = Image.open('skills.eng.PNG')
    st.sidebar.markdown("# Skills")
    st.image(image)

