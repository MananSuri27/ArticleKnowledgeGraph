import base64
from io import BytesIO

import requests
import streamlit as st
from PIL import Image


# Define the Streamlit app
def main():
    st.title("Knowledge Graph from Articles")

    # Input URL for the image
    url = st.text_input("Input URL of the article:")

    # Input max edge density and node count
    max_edge_density = st.slider("Select max edge density:", 2, 6, 3)
    node_count = st.slider("Select node count:", 2, 15, 5)
    context_window = st.slider(
        "Select number of tokens as context", 512, 4096, 2048, 512
    )

    if st.button("Generate Knowledge Graph"):
        #  TO DO: add logic here

        st.image(kg, caption="Processed Image", use_column_width=True)

        # Create a custom download button

        download_button(kg, "Download Processed Image")


# Function to create a custom download button for the image
def download_button(object_to_download, download_button_text):
    # Save the image to a BytesIO object
    buffer = BytesIO()
    object_to_download.save(buffer, format="PNG")
    buffer.seek(0)

    # Generate a download button
    b64 = base64.b64encode(buffer.read()).decode()
    st.download_button(label=download_button_text, data=buffer, key="processed_image")


if __name__ == "__main__":
    main()
