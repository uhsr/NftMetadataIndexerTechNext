# test_nftmetadataindexertechnext.py
"""
Tests for NftMetadataIndexerTechNext module.
"""

import unittest
from nftmetadataindexertechnext import NftMetadataIndexerTechNext

class TestNftMetadataIndexerTechNext(unittest.TestCase):
    """Test cases for NftMetadataIndexerTechNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerTechNext()
        self.assertIsInstance(instance, NftMetadataIndexerTechNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerTechNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
