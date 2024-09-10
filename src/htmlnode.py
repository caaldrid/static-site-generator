class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # An HTMLNode without a tag will just render as raw text
        # An HTMLNode without a value will be assumed to have children
        # An HTMLNode without children will be assumed to have a value
        # An HTMLNode without props simply won't have any attributes
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_str = ""

        if self.props != None:
            for (
                k,
                v,
            ) in self.props.items():
                html_str += f' {k}="{v}"'

        return html_str

    def __repr__(self):
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children="{self.children}", props="{self.props_to_html()}")'
