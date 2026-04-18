from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue 
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)" ,text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        extracted = extract_markdown_images(old_node.text)
        if len(extracted) == 0:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        old_node_text = old_node.text
        for i in range(len(extracted)):
            section = old_node_text.split(f"![{extracted[i][0]}]({extracted[i][1]})")
            if section[0] != "":
                split_nodes.append(TextNode(section[0],TextType.TEXT))
            split_nodes.append(TextNode(extracted[i][0], TextType.IMAGE, extracted[i][1]))
            old_node_text = section[1]
        if old_node_text != "": 
            split_nodes.append(TextNode(old_node_text,TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        extracted = extract_markdown_links(old_node.text)
        if len(extracted) == 0:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        old_node_text = old_node.text
        for i in range(len(extracted)):
            section = old_node_text.split(f"[{extracted[i][0]}]({extracted[i][1]})")
            if section[0] != "":
                split_nodes.append(TextNode(section[0],TextType.TEXT))
            split_nodes.append(TextNode(extracted[i][0], TextType.LINK, extracted[i][1]))
            old_node_text = section[1]
        if old_node_text != "": 
            split_nodes.append(TextNode(old_node_text,TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text,TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)
    nodes = split_nodes_delimiter(nodes,"**",TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_",TextType.ITALIC)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes
    


