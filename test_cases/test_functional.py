import unittest
from nand_simulator import NANDSimulator
import logging

logger = logging.getLogger(__name__)

class TestFunctional(unittest.TestCase):
    def setUp(self):
        self.nand = NANDSimulator()
        logger.info("Initialized NANDSimulator for functional test.")
    
    def test_basic_write_read(self):
        logger.info("Running test_basic_read_write...")
        self.nand.write_page(0, 0, "Hello")
        data = self.nand.read_page(0, 0)
        self.assertEqual(data, "Hello")
        logger.info("test_basic_write_read passed.")
    
    def test_read_unwritten_page(self):
        logger.info("Running read_unwritten_page...")
        data = self.nand.read_page(1, 1)
        self.assertIsNone(data)
        logger.info("test_read_unwritten_page passed.")
    
    def test_erase_block(self):
        logger.info("Running test_erase_block...")
        self.nand.write_page(2, 2, "Data")
        self.nand.erase_block(2)
        self.assertIsNone(self.nand.read_page(2, 2))
        logger.info("test_erase_block passed.")

if __name__ == "__main__":
    unittest.main()