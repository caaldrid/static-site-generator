import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown: str):
    # assuming that each block is seperated by a blank lines
    lines = markdown.split("\n\n")

    blocks = map(lambda line: line.strip(), lines)

    return list(blocks)


def block_to_block_type(block_text: str):

    if re.fullmatch(r"(?<!.)`{3}(?:\n)?(?:.*\n)+`{3}", block_text) != None:
        return block_type_code

    lines = block_text.splitlines()

    if len(lines) == 1 and re.match(r"(?<!.)\#{1,6}\s.+", block_text) != None:

        return block_type_heading

    for line in lines:
        if re.match(r"(?<!.)\>\s.+", line) != None:
            return block_type_quote

        if re.match(r"(?<!.)[\*\-]\s.+", line) != None:
            return block_type_ulist

        if re.match(r"(?<!.)\d\.\s.+", line) != None:
            return block_type_olist

    return block_type_paragraph
