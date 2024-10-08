import unittest

from blocks import block_to_block_type, markdown_to_blocks


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

    def test_block_to_block_type(self):
        test_md = """# This is a heading

## A subsetting

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

- foo
- bar
- baz

1. fasd
1. basr
1. dasdaf

```
print("Hello, world!")
for i in range(10):
    print(i)
```

> I am quoting
> as
> book"""

        expecting = [
            "heading",
            "heading",
            "paragraph",
            "unordered_list",
            "unordered_list",
            "ordered_list",
            "code",
            "quote",
        ]

        blocks = markdown_to_blocks(test_md)
        got = list(map(lambda block: block_to_block_type(block), blocks))

        self.assertEqual(got, expecting)


if __name__ == "__main__":
    unittest.main()
