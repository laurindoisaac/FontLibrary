# test_fontlibrary.py
"""
Tests for FontLibrary module.
"""

import unittest
from fontlibrary import FontLibrary

class TestFontLibrary(unittest.TestCase):
    """Test cases for FontLibrary class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FontLibrary()
        self.assertIsInstance(instance, FontLibrary)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FontLibrary()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
