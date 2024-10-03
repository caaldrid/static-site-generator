def markdown_to_blocks(markdown: str):
    # assuming that each block is seperated by a blank lines
    lines = markdown.split("\n\n")

    blocks = map(lambda line: line.strip(), lines)

    return list(blocks)
