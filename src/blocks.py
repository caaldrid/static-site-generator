import re
import types


class block_types:
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    olist = "ordered_list"
    ulist = "unordered_list"


def markdown_to_blocks(markdown: str):
    # assuming that each block is seperated by a blank lines
    lines = markdown.split("\n\n")

    blocks = map(lambda line: line.strip(), lines)

    return list(filter(lambda block: block != "", list(blocks)))


def block_to_block_type(block_text: str):

    if re.fullmatch(r"(?<!.)`{3}(?:\n)?(?:.*\n)+`{3}", block_text) != None:
        return block_types.code

    lines = block_text.splitlines()

    if len(lines) == 1 and re.match(r"(?<!.)\#{1,6}\s.+", block_text) != None:

        return block_types.heading

    for line in lines:
        if re.match(r"(?<!.)\>\s.+", line) != None:
            return block_types.quote

        if re.match(r"(?<!.)[\*\-]\s.+", line) != None:
            return block_types.ulist

        if re.match(r"(?<!.)\d\.\s.+", line) != None:
            return block_types.olist

    return block_types.paragraph
