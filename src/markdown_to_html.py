import re

from blocks import block_to_block_type, block_types, markdown_to_blocks
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import text_node_to_html_node, text_to_textnodes


def markdown_to_html_node(markdown):
    def create_list_html(txt: str):
        list_items = txt.splitlines()
        html_list = []

        for item in list_items:
            regexp = re.compile(r"^(\*|\-|(?:\d.))")

            list_txt = regexp.sub("", item).strip()
            inline_nodes = text_to_textnodes(list_txt)
            if len(inline_nodes) == 0:
                html_list.append(LeafNode("li", list_txt))
            else:
                html_list.append(
                    ParentNode(
                        "li",
                        list(
                            map(lambda node: text_node_to_html_node(node), inline_nodes)
                        ),
                    )
                )

        return html_list

    blocks = markdown_to_blocks(markdown)

    html_root = ParentNode("div", [])

    if html_root.children is None:
        raise Exception("Why?")

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case block_types.heading:
                heading_level = block.count("#")
                heading_text = block.lstrip("#").strip()
                html_root.children.append(LeafNode(f"h{heading_level}", heading_text))
            case block_types.paragraph:
                lines = block.split("\n")
                paragraph = " ".join(lines)
                inline_nodes = text_to_textnodes(paragraph)
                html_root.children.append(
                    ParentNode(
                        "p",
                        list(
                            map(lambda node: text_node_to_html_node(node), inline_nodes)
                        ),
                    )
                )
            case block_types.code:
                code_text = block.strip("```").strip()
                html_root.children.append(
                    ParentNode("pre", [LeafNode("code", code_text)])
                )
            case block_types.quote:
                quote_text = " ".join(
                    list(
                        map(
                            lambda quote_line: quote_line.lstrip(">").strip(),
                            block.splitlines(),
                        )
                    )
                )
                html_root.children.append(LeafNode("blockquote", quote_text))
            case block_types.ulist:
                html_root.children.append(ParentNode("ul", create_list_html(block)))
            case block_types.olist:
                html_root.children.append(ParentNode("ol", create_list_html(block)))
            case _:
                raise ValueError("Invalid block type")

    return html_root


def extract_title(markdown):
    lines = markdown.splitlines()

    for line in lines:
        if line.startswith("#"):
            header_level = line.count("#")
            if header_level == 1:
                return line.split("#")[1].strip()

    raise Exception("Given markdow string is not a h1 header")
