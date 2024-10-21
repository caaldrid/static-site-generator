import unittest

from markdown_to_html import extract_title, markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
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
> a
> book"""
        expected = '<div><h1>This is a heading</h1><h2>A subsetting</h2><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul><ul><li>foo</li><li>bar</li><li>baz</li></ul><ol><li>fasd</li><li>basr</li><li>dasdaf</li></ol><pre><code>print("Hello, world!")\nfor i in range(10):\n    print(i)</code></pre><blockquote>I am quoting a book</blockquote></div>'
        got = markdown_to_html_node(test_md).to_html()

        self.assertEqual(got, expected)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_extract_title(self):
        header = extract_title("# Hello")
        self.assertEqual("Hello", header)

    def test_extract_title_2(self):
        md = """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"""
        self.assertEqual("Tolkien Fan Club", extract_title(md))


if __name__ == "__main__":
    unittest.main()
