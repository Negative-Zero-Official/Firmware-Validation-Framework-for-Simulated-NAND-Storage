import unittest
from nand_simulator import NANDSimulator
import logging

logger = logging.getLogger(__name__)

class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.nand = NANDSimulator()
        logger.info("Initialized NANDSimulator for edge cases test.")
    
    def test_write_to_bad_block(self):
        logger.info("Running test_write_to_bad_block...")
        self.nand.inject_bad_block(3)
        try:
            with self.assertRaises(Exception) as context:
                self.nand.write_page(3, 0, "Data")
            logger.info(f"Caught expected error: {context.exception}")
        except AssertionError as e:
            logger.error("FAILED: No error when writing to bad block.")
            raise
    
    def test_overwrite_without_erase(self):
        logger.info("Running test_overwrite_without_erase...")
        self.nand.write_page(2, 1, "Initial data")
        try:
            with self.assertRaises(Exception) as context:
                self.nand.write_page(2, 1, "Overwrite")
            logger.info(f"Caught expected error: {context.exception}")
        except AssertionError as e:
            logger.error("FAILED: No error on overwrite without erase.")
            raise
    
    def test_block_out_of_bounds(self):
        logger.info("Running test_block_out_of_bounds...")
        try:
            with self.assertRaises(Exception) as context:
                self.nand.write_page(100, 0, "Out of range")
            logger.info(f"Caught expected error: {context.exception}")
        except AssertionError as e:
            logger.error("FAILED: No error raised on out-of-bounds block.")
            raise
    
    def test_page_out_of_bounds(self):
        logger.info("Running test_page_out_of_bounds...")
        try:
            with self.assertRaises(Exception) as context:
                self.nand.write_page(0, 100, "Out of range")
            logger.info(f"Caught expected error: {context.exception}")
        except AssertionError as e:
            logger.error("FAILED: No error raised on out-of-bounds page.")
            raise

if __name__=="__main__":
    unittest.main()