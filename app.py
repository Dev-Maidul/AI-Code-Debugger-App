import streamlit as st

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
