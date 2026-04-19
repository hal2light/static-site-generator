import unittest
from generate_page import extract_title

class TestGenContent(unittest.TestCase):
    def test_title(self):
        md = """
# This is a heading    

And this is some paragraph.
- some list items
- items
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a heading"
        )
    def test_whitespace(self):
        md = """
#       This is a heading   

And this is some paragraph.
- some list items
- items
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a heading"
        )







if __name__ == "__main__":
    unittest.main()
