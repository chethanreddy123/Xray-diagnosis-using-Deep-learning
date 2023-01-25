import streamlit as st
from PIL import Image   
from MedicalImage import create_model as cm


def intro():
    import streamlit as st

    st.write("# AnX-Ray By AIOverflow 🚀🚀🚀")
    st.sidebar.success("Please do select an option to do your customized analysis.")

    st.sidebar.title('Developers Contact')
    st.sidebar.markdown('[![Chethan-Reddy]'
                        '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                        '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)')


    image = Image.open('MainImg.webp')
    st.image(image, caption='All Kinds of X-Ray Analysis')



    st.markdown(
        """
        #### AnXray is an application which helps you to analyze any kind of x ray in seconds to get the most accurate insights of it.



        
    """
    )

intro()