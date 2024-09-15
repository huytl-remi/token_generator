import streamlit as st
import os
from PIL import Image
import io
from src.token_generator import generate_tokens
from src.image_generator import generate_image
from src.trend_analyzer import get_trends
from utils.helpers import sanitize_input

def main():
    st.set_page_config(page_title="Token Generator", layout="wide")

    st.title("Token Generator")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Create Your Token")

        # Text input
        text_input = st.text_area("Describe your desired token:", height=100)

        # Image upload
        uploaded_file = st.file_uploader("Upload an inspiration image (optional):", type=["png", "jpg", "jpeg"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Tokens"):
            if text_input or uploaded_file:
                with st.spinner("Generating tokens..."):
                    sanitized_input = sanitize_input(text_input)
                    tokens = generate_tokens(sanitized_input, uploaded_file)

                    if tokens:
                        st.success("Tokens generated successfully!")
                        display_tokens(tokens)
                    else:
                        st.error("Failed to generate tokens. Please try again.")
            else:
                st.warning("Please provide a text description or upload an image.")

    with col2:
        st.header("Trending Topics")
        trends = get_trends()
        for trend in trends:
            st.write(f"**{trend['name']}**")
            st.write(trend['relevance'])
            st.write("---")

def display_tokens(tokens):
    for i, token in enumerate(tokens, 1):
        st.subheader(f"Token Option {i}")

        col1, col2 = st.columns([1, 2])

        with col1:
            image_url = generate_image(token)
            if image_url:
                st.image(image_url, caption="Generated Token Image", use_column_width=True)
            else:
                st.error("Failed to generate image for this token.")

        with col2:
            st.write(f"**Name:** {token['name']}")
            st.write(f"**Ticker:** {token['ticker']}")
            st.write(f"**Description:** {token['description']}")
            st.write("**Visual Elements:**")
            for element in token['visual_elements']:
                st.write(f"- {element}")

        st.write("---")

if __name__ == "__main__":
    main()
