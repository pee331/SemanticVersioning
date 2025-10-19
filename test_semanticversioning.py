# test_semanticversioning.py
"""
Tests for SemanticVersioning module.
"""

import unittest
from semanticversioning import SemanticVersioning

class TestSemanticVersioning(unittest.TestCase):
    """Test cases for SemanticVersioning class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SemanticVersioning()
        self.assertIsInstance(instance, SemanticVersioning)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SemanticVersioning()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
