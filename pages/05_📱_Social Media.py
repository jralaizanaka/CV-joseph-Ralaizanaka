import streamlit as st

from PIL import Image

if st.session_state.vers == 'française':
    version = "française"
elif st.session_state.vers == 'english':
    version = "english"

if version == "française":
    image = Image.open('linkedin.png')
    image2 = Image.open('github.png')
    image3 = Image.open('streamlit.jpg')
    st.sidebar.markdown("# Réseaux Sociaux")
    st.image(image)
    st.markdown("""
                   [linkedin](https://www.linkedin.com/in/joseph-ralaizanaka/ )
                    """)
    st.image(image2)
    st.markdown("""
                       [github](https://github.com/jralaizanaka/Data-Science-Projects-Porfolio)
                        """)

    st.image(image3)
    st.markdown("""
                       [streamlit](https://bilandecompetencev1.herokuapp.com/)
                        """)




else:
    image = Image.open('linkedin.png')
    image2 = Image.open('github.png')
    image3 = Image.open('streamlit.jpg')
    st.sidebar.markdown("# Social Media")
    st.image(image)
    st.markdown("""
                   [linkedin](https://www.linkedin.com/in/joseph-ralaizanaka/ )
                    """)
    st.image(image2)
    st.markdown("""
                       [github](https://github.com/jralaizanaka/Data-Science-Projects-Porfolio)
                        """)

    st.image(image3)
    st.markdown("""
                       [streamlit](https://bilandecompetencev1.herokuapp.com/)
                        """)



