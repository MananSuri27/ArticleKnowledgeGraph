import json
import os

import graphviz
import openai

from Article.article_stripped import Article

openai.api_key = os.getenv("OPENAI_API_KEY")


def parse_article(url: str) -> Article:
    """
    Uses the Article class to parse a web article.

    Args:
        url (str): URL of a web article.

    Returns:
        article (Article): An Article object which has the parsed information.
    """
    article = Article(url)
    return article


def kg_from_gpt4(
    article_text: str, max_edge_density: int, num_nodes: int, num_tokens: int
) -> dict:
    """
    Generate a Knowledge Graph that explains the article text given certain constraints.

    Args:
        article_text (str): The text of the article.
        max_edge_density (int): Maximum number of edges per node in the graph.
        num_nodes (int): Maximum number of nodes in the graph.
        num_tokens (int): Maximum number of tokens to consider from the article text.

    Returns:
        dict: A dictionary containing the knowledge graph data with keys "edges" and "nodes".

    Example:
        article_text = "This is an example article."
        max_edge_density = 3
        num_nodes = 10
        num_tokens = 1000
        kg_data = kg_from_gpt4(article_text, max_edge_density, num_nodes, num_tokens)
    """

    num_chars = min(len(article_text), 4 * num_tokens)

    article_text = article_text[:num_chars]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": f'Generate a Knowledge Graph that explains the article text given, explains meaningful relationships and simplifies while adding context the article, given the constraints. The node and edge are described as dictionaries below:\nNode = {{\nid: (1/2/3...)\nlabel:(text label)\ncolor: HEX Code of light pastel color unique to the node that goes well with black text and line\n}}\nEdge = {{\nsrc: id of source node\ndst: id of dest node\nlabel: text label of edge\n}}\nReturn a compressed JSON object:\n{{ "edges": [list of edges],\n"nodes": [list of nodes]\n}}\nConstraints: \nMax edge density: number of edges per node = {max_edge_density}\nMax number of nodes = {num_nodes}. Think carefully about what would be src and dst node in an edge according to the label used to describe the edge/relation.',
            },
            {"role": "user", "content": f"Article: {article_text}"},
        ],
        temperature=0.4,
        max_tokens=3925,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    data = response["choices"][0]["message"]["content"]

    json_data = json.loads(data)

    return json_data


def generate_graph(
    graph_name: str, graph_json: dict, directory: str, format: str = "png"
):
    """
    Create and render a graph using Graphviz based on the provided JSON data.

    Args:
        graph_name (str): The name of the graph.
        graph_json (Dict): A dictionary containing the graph data with keys "nodes" and "edges."
        directory (str): The directory where the graph will be saved.
        format (str, optional): The format in which to render the graph (e.g., "png", "svg"). Default is "png".

    Returns:
        None

    Example:
        graph_data = {
            "nodes": [
                {"id": 1, "label": "Node 1", "color": "lightblue"},
                {"id": 2, "label": "Node 2", "color": "lightgreen"},
            ],
            "edges": [
                {"src": 1, "dst": 2, "label": "Edge 1-2"},
            ],
        }
        generate_graph("MyGraph", graph_data, "/path/to/save", format="png")
    """
    knowledge_graph = graphviz.Digraph(graph_name, format=format)

    # Add nodes to the graph
    for node in graph_json["nodes"]:
        knowledge_graph.node(
            str(node["id"]), label=node["label"], color=node["color"], style="filled"
        )

    # Add edges to the graph
    for edge in graph_json["edges"]:
        knowledge_graph.edge(str(edge["src"]), str(edge["dst"]), label=edge["label"])

    knowledge_graph.render(graph_name, directory=directory, view=True)
