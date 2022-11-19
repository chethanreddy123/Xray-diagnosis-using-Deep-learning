import streamlit as st


st.sidebar.title('Developers Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                    '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                    '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)')
st.sidebar.markdown('[![Chethan-Reddy]'
                    '(https://img.shields.io/badge/Author-Leela%20Reddy-brightgreen)]'
                    '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 

st.title("Analysis of Other Type of X-Rays")
import paginator

images = ['img1.jpg', 'img2.png', 'img3.webp' , 'img4.webp']
st.image(images, use_column_width=True, caption=["Abdominal" , "Kidney" , "Nech" , " Hand"]  )


 