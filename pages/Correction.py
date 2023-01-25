import streamlit as st
from PIL import Image

st.sidebar.success("Please do select an option to do your customized analysis.")

st.title("X - Ray - Retraining")






st.sidebar.title('Developers Contact')
st.sidebar.markdown('[![Chethan-Reddy]'
                    '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                    '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)')




def load_image(image_file):
	img = Image.open(image_file)
	return img

image_file = st.file_uploader("Uploaded the images to re-train", type=["png","jpg","jpeg"])

if image_file is not None:
    file_details = {"filename":image_file.name, "filetype":image_file.type,
        "filesize":image_file.size}
    st.caption("File Details: ")
    st.write(file_details)
    st.image(load_image(image_file),width=350)



with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.selectbox("Form slider", ["Chest" , "Abdominal" , "Kidney" , "Ureter and Bladder" ,  "X-Ray",  "Neck" , "Hand", "Joint", "Skull"])

   

   checkbox_val = st.checkbox("Re-train the Algorithm")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Data Vill be Validated Soon...")