import streamlit as st

from PIL import Image

st.set_page_config(
    page_title="CV Joseph Ralaizanaka",
    page_icon="📄",
    layout="wide",
)

if "vers" not in st.session_state:
    st.session_state.vers = 'française'

st.session_state.vers = st.sidebar.radio(
    "Version",
    ('française', 'english'), horizontal=True)

if st.session_state.vers == 'française':
    version = "française"
elif st.session_state.vers == 'english':
    version = "english"

if version == "française":
    image = Image.open('Capture.PNG')
    st.image(image)

    image2 = Image.open('Mon-profil.PNG')
    st.image(image2)

    with open("Ralaizanaka_Joseph.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Télécharger le CV",
                       data=PDFbyte,
                       file_name="Ralaizanaka Joseph.pdf",
                       mime='application/octet-stream')


else:
    image = Image.open('Capture.eng.PNG')
    st.image(image)

    image2 = Image.open('Mon-profil.eng.PNG')
    st.image(image2)


    with open("Ralaizanaka_Joseph_eng.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Download resume",
                        data=PDFbyte,
                        file_name="Ralaizanaka Joseph.pdf",
                        mime='application/octet-stream')

