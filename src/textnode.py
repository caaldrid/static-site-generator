import re

from leafnode import LeafNode


class TextNode:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherTN):
        return (
            (self.text == otherTN.text)
            and (self.text_type == otherTN.text_type)
            and (self.url == otherTN.url)
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextNode.text_type_text:
            return LeafNode(None, text_node.text)
        case TextNode.text_type_bold:
            return LeafNode("b", text_node.text)
        case TextNode.text_type_italic:
            return LeafNode("i", text_node.text)
        case TextNode.text_type_code:
            return LeafNode("code", text_node.text)
        case TextNode.text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextNode.text_type_image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Unknown Text Type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if delimiter in node.text:

            split_node = node.text.split(delimiter)
            # Grab the inline formatted text
            inline = split_node[
                1::2
            ]  # the [1::2] is a slicing which extracts odd values

            for text in split_node:
                if text == "":
                    continue

                if text in inline:
                    new_nodes.append(TextNode(text, text_type))
                else:
                    new_nodes.append(TextNode(text, TextNode.text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes


def extract_markdown_images(text):
    regex_str = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex_str, text)

    return matches


def extract_markdown_links(text):
    regex_str = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(regex_str, text)

    return matches
