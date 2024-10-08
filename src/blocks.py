import re


def markdown_to_blocks(markdown: str):
    # assuming that each block is seperated by a blank lines
    lines = markdown.split("\n\n")

    blocks = map(lambda line: line.strip(), lines)

    return list(blocks)


def block_to_block_type(block_text: str):

    if re.fullmatch(r"(?<!.)`{3}(?:\n)?(?:.*\n)+`{3}", block_text) != None:
        return "code"

    lines = block_text.splitlines()

    if len(lines) == 1 and re.match(r"(?<!.)\#{1,6}\s.+", block_text) != None:

        return "heading"

    for line in lines:
        if re.match(r"(?<!.)\>\s.+", line) != None:
            return "quote"

        if re.match(r"(?<!.)[\*\-]\s.+", line) != None:
            return "unordered_list"

        if re.match(r"(?<!.)\d\.\s.+", line) != None:
            return "ordered_list"

    return "paragraph"
