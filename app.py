import streamlit as st
from PIL import Image
from api import error_explanator
# Header Section
st.title("AI Code Debugger Assistance",anchor=False)
st.markdown("Upload your Code snippent to get solutions !")
st.divider()

# Sidebar Section
with st.sidebar:
    st.header("Controls")
    #! Uploading Images
    images=st.file_uploader(
        "Upload your Images here:",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True
    )
    pil_images=[]
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)
    if images:
        if len(images)>3:
            st.error("You can't upload more than 3 images")
        else:
            st.subheader("Uploaded images")
            col=st.columns(len(images))
            
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    #! Selected Options
    selected_option=st.selectbox("Choose you options:",("Hints","Solution with code"),index=None)
    if selected_option:
        st.markdown(f"Your have selected **{selected_option}**")
    
    #! Button
    is_clicked=st.button("Debug Code",type="primary")

# Body logic from here
if is_clicked:
    if not images:
        st.error("You didn't upload images!")
    if not selected_option:
        st.error("You did't select any option!")
    
    if images and selected_option:
        #! error explanation
        with st.container(border=True):
            st.subheader("Error Explanations",anchor=False)
            with st.spinner("AI is debugging,Please Wait"):
                errors=error_explanator(pil_images)
                st.markdown(errors)
        #! Hints/Solution