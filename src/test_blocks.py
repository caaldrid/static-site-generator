import unittest

from blocks import markdown_to_blocks


class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        expecting = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]

        self.assertEqual(
            expecting,
            markdown_to_blocks(
                """# This is a heading


 This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
            ),
        )
