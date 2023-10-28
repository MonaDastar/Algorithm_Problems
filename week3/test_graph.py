import unittest

from graph import Graph


class TestGraph(unittest.TestCase):
    
    def test_add_node(self):    
        g = Graph()
        g.add_node("a", True)
        self.assertIn("a", g.get_all())

if __name__ == '__main__':
    unittest.main()