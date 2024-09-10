import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "this is an image HTML node",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            " href=https://www.google.com target=_blank", node.props_to_html()
        )

    def test_props_to_html2(self):
        node = HTMLNode("p", "this is a paragraph")
        self.assertEqual("", node.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "a",
            "this is an image HTML node",
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            "HTMLNode(tag='a', value='this is an image HTML node', children='None', props=' href=https://www.google.com target=_blank')",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
