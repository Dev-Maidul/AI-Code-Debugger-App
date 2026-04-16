import streamlit as st
from PIL import Image
from api import error_explanator
from api import hints_solutions

# Page Config
st.set_page_config(
    page_title="AI Code Debugger",
    page_icon="🐞",
    layout="wide"
)

# Header Section
st.markdown("## 🧠 AI Code Debugger Assistance")
st.markdown("Upload your **code error screenshot** and get instant debugging help 🚀")
st.divider()

# Sidebar Section
with st.sidebar:
    st.markdown("## ⚙️ Control Panel")

    # Upload Images
    images = st.file_uploader(
        "📤 Upload your screenshots",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True
    )

    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images) > 3:
            st.error("⚠️ You can't upload more than 3 images")
        else:
            st.markdown("### 🖼️ Preview")
            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img, use_container_width=True)

    # Option Selection
    st.markdown("### 🎯 Select Mode")
    selected_option = st.selectbox(
        "Choose debugging type:",
        ("Hints", "Solution with code"),
        index=None
    )

    if selected_option:
        st.success(f"✅ Selected: **{selected_option}**")

    # Button
    is_clicked = st.button("🐞 Debug Code", use_container_width=True)

# Body Section
if is_clicked:
    if not images:
        st.error("⚠️ Please upload at least one image!")
    if not selected_option:
        st.error("⚠️ Please select a debugging option!")

    if images and selected_option:
        # Error Explanation
            with st.container(border=True):
                st.markdown("### 🚨 Error Explanation")
                with st.spinner("🔍 Analyzing your code..."):
                    errors = error_explanator(pil_images)
                    st.markdown(errors)

        # Hints / Solution
            with st.container(border=True):
                st.markdown(f"### 💡 {selected_option}")
                with st.spinner(f"⚡ Generating {selected_option}..."):
                    response = hints_solutions(pil_images, selected_option)
                    st.markdown(response)