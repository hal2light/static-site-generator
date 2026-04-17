import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "button",
            "Click me",
            None,
            {"type": "submit", "class": "btn"}
        )
        self.assertEqual(node.props_to_html(), ' type="submit" class="btn"')
    def test_empty_or_none_props(self):
        node = HTMLNode(
            "button",
            "Click me",
            None,
            None
        )
        self.assertEqual(node.props_to_html(), "")
    def test_repr(self):
        node = HTMLNode(
            "button",
            "Click me",
            None,
            {"type": "submit", "class": "btn"}
        )

        self.assertEqual(node.__repr__(), "HTMLNode(button, Click me, None, {'type': 'submit', 'class': 'btn'})")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello world!")
        self.assertEqual(node.to_html(), "<p>Hello world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )





if __name__ == "__main__":
    unittest.main()
