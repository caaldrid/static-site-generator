import unittest

from textnode import TextNode, split_nodes_delimiter, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextNode.text_type_text)
        node2 = TextNode("This is a text node", TextNode.text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextNode.text_type_text)
        node2 = TextNode("This is a text node2", TextNode.text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode(
            "This is a text node", TextNode.text_type_italic, "https://www.boot.dev"
        )
        node2 = TextNode(
            "This is a text node", TextNode.text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode(
            "This is a text node", TextNode.text_type_text, "https://www.boot.dev"
        )
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html_node_url(self):
        node = TextNode(
            "This is a url node", TextNode.text_type_link, "https://www.boot.dev"
        )

        html = text_node_to_html_node(node)

        self.assertEqual(
            '<a href="https://www.boot.dev">This is a url node</a>', html.to_html()
        )

    def test_text_node_to_html_node_img(self):
        node = TextNode(
            "This is a image node",
            TextNode.text_type_image,
            "https://www.boot.dev/pic.png",
        )

        html = text_node_to_html_node(node)

        self.assertEqual(
            '<img src="https://www.boot.dev/pic.png" alt="This is a image node"></img>',
            html.to_html(),
        )

    def test_split_nodes_delimeter(self):
        node = TextNode(
            "This is text with a `code block` word", TextNode.text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("code block", TextNode.text_type_code),
                TextNode(" word", TextNode.text_type_text),
            ],
        )

    def test_split_nodes_delimeter2(self):
        node = TextNode(
            "This is text with a **bolded phrase** in the middle",
            TextNode.text_type_text,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded phrase", TextNode.text_type_bold),
                TextNode(" in the middle", TextNode.text_type_text),
            ],
        )

    def test_split_nodes_delimeter3(self):
        node = TextNode(
            "This is text with a **bolded phrase** in the middle",
            TextNode.text_type_text,
        )

        node1 = TextNode("Another plain text node", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node, node1], "**", TextNode.text_type_bold)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextNode.text_type_text),
                TextNode("bolded phrase", TextNode.text_type_bold),
                TextNode(" in the middle", TextNode.text_type_text),
                node1,
            ],
        )


if __name__ == "__main__":
    unittest.main()
