import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leafnode_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>', node.to_html()
        )

    def test_leafnode_without_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_leafnode_without_tag(self):
        value = "This is just test"
        node = LeafNode(None, value)
        self.assertEqual(value, node.to_html())


if __name__ == "__main__":
    unittest.main()
