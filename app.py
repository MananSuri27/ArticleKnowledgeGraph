import base64
import os
from io import BytesIO

import requests
import streamlit as st
from PIL import Image

from utils import generate_graph, kg_from_gpt4, parse_article

graphs_dir = "./graphs"
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
        article = parse_article(url)
        graph_json = kg_from_gpt4(article.text, max_edge_density, node_count, context_window)
        graph_name = "_".join(article.title.split(" "))
        generate_graph(graph_name, graph_json, graphs_dir)
        path = os.path.join(graphs_dir, graph_name+".png")
        kg = Image.open(path)
        st.image(kg, caption="Processed Image", use_column_width=True)
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
