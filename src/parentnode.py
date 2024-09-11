from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Parent Node has no tag")
        if self.children == None:
            raise ValueError("Parent Node has no children, this will lead to a blank HTML file")

        return f'<{self.tag}{self.props_to_html()}>{"".join(map(lambda child: child.to_html(), self.children))}</{self.tag}>'
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
