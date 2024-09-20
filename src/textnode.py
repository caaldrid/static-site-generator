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


def split_node_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextNode.text_type_text:
            new_nodes.append(node)
            continue

        markdown_links = extract_markdown_links(node.text)

        if len(markdown_links) != 0:
            text = node.text
            for link in markdown_links:
                link_text = link[0]
                link_url = link[1]

                sections = text.split(f"[{link_text}]({link_url})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")

                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextNode.text_type_text))

                new_nodes.append(TextNode(link_text, TextNode.text_type_link, link_url))
                text = sections[1]
        else:
            if node.text != "":
                new_nodes.append(node)

    return new_nodes


def split_node_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextNode.text_type_text:
            new_nodes.append(node)
            continue

        markdown_images = extract_markdown_images(node.text)

        if len(markdown_images) != 0:
            text = node.text
            for image in markdown_images:
                alt_text = image[0]
                url = image[1]

                sections = text.split(f"![{alt_text}]({url})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")

                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextNode.text_type_text))

                new_nodes.append(TextNode(alt_text, TextNode.text_type_image, url))
                text = sections[1]
        else:
            if node.text != "":
                new_nodes.append(node)

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
