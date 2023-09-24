# 🪢 ArticleKnowledgeGraph
When it comes to understanding complex topics or diving deep into news articles, traditional reading methods might not always suffice. KnowledgeGraphArticle addresses this challenge by transforming the textual content of articles into visually engaging knowledge graphs. These graphs provide a structured representation of the article's content, allowing you to explore relationships between concepts and grasp the key points more effectively.

KnowledgeGraphArticle is a fascinating tool that offers a visual way to read online articles by leveraging the power of technology. It seamlessly combines the parsing capabilities of [`Article`](https://github.com/MananSuri27/Article) to process online news articles, `GPT-4` to create knowledge graphs, and `graphviz` to render these graphs for easy comprehension, all served on a simple frontend for demos.

<img width="556" alt="image" src="https://github.com/MananSuri27/ArticleKnowledgeGraph/assets/84636031/7202e592-16b0-468d-8623-e7b950ed08ab">

## 🧫 Examples
[Abbott India warns of laxatives shortage in tussle with Goa regulator](https://www.reuters.com/business/healthcare-pharmaceuticals/abbott-india-warns-laxatives-shortage-tussle-with-goa-regulator-2023-09-22/)
<br>
<img width="457" alt="image" src="https://github.com/MananSuri27/ArticleKnowledgeGraph/assets/84636031/1c3fb2e7-0f53-4bbf-9b29-d3eacb8e3e14">

[California governor vetoes bill banning robotrucks without safety drivers](https://www.reuters.com/business/autos-transportation/california-governor-vetoes-bill-banning-robotrucks-without-safety-drivers-2023-09-23/)
<br>
<img width="1147" alt="image" src="https://github.com/MananSuri27/ArticleKnowledgeGraph/assets/84636031/5a743c5b-f21e-4f70-a319-176f0c3111ea">

[NASA's first asteroid sample parachutes into Utah desert](https://www.reuters.com/science/nasas-first-asteroid-sample-parachutes-into-utah-desert-2023-09-24/)
<br>
<img width="407" alt="image" src="https://github.com/MananSuri27/ArticleKnowledgeGraph/assets/84636031/341632a1-b78c-4b29-8c8b-b5416bfc3117">

## 🗜️ Setup

To get started with KnowledgeGraphArticle, follow these simple steps:

1. **Set-up the repository**
   ```bash
   git clone --recursive https://github.com/MananSuri27/ArticleKnowledgeGraph
   cd ArticleKnowledgeGraph
   ```
3. **Create a Conda Environment:** We recommend setting up a dedicated Conda environment to manage dependencies for this project. You can create a new environment and set up dependencies with the following command:
   ```bash
   conda create --name kg-article-env
   conda activate kg-article-env
   pip install -r requirments.txt
   ```
If you encounter any import errors related to Graphviz during the setup, you can try using Conda to install python-graphviz:
  ```bash
  conda install python-graphviz
  ```

3. **Set Up OpenAI API Key:**
To use the GPT-4 functionality in KnowledgeGraphArticle, you'll need to set your OpenAI API key as an environment variable. On Linux and macOS, you can do this by opening a terminal and running the following command:
```bash
export OPENAI_API_KEY="your-api-key-here"
```
Replace "your-api-key-here" with your actual OpenAI API key. 

## 🏌️‍♀️ Usage

Now that you have set up your environment and added your OpenAI API key, you can start using KnowledgeGraphArticle:

1. **Run the Application:** Launch the KnowledgeGraphArticle application using Streamlit by running the following command from the project's root directory:

   ```bash
   streamlit run app.py
   ```

2. Use the streamlit application served on `http://localhost:8501/` by default.
- Input Article URL: In the Streamlit web interface, paste the URL of the online article you want to analyze.
- Max Edge Density: Control the density of edges in the graph by adjusting this parameter.
- Max Number of Nodes: Set the maximum number of nodes to include in the graph.
- Context Window (in terms of tokens): Define the context window size in terms of tokens.

3. Explore the Knowledge Graph: Once you've entered the URL and adjusted the parameters to your liking, submit. KnowledgeGraphArticle will process the article, generate a knowledge graph, and display it for your exploration.

## 📇 Contact
Contact me on [Linkedin](https://www.linkedin.com/in/manansuri27/), drop an [email](mailto:manansuri27@gmail.com), or check me out on my website [manansuri.com](https://manansuri.com/).
