import unittest
from nand_simulator import NANDSimulator
from random import randint
import logging

logger = logging.getLogger(__name__)

class TestStress(unittest.TestCase):
    def setUp(self):
        self.nand = NANDSimulator()
        logger.info("Initialized NANDSimulator for stress test.")
    
    def test_full_write_read_cycle(self):
        logger.info("Running test_full_write_read_cycle...")
        failed_writes = 0
        
        for block in range(self.nand.num_blocks):
            if randint(0, 5) == 0: # 1 in 5 chance that a block is bad
                self.nand.inject_bad_block(block)
                continue
            for page in range(self.nand.pages_per_block):
                try:
                    data = f"Block{block}_Page{page}"
                    self.nand.write_page(block, page, data)
                except Exception as e:
                    logger.warning(f"Failed to write to block {block}, page {page}: {e}")
                    failed_writes += 1
        
        try:
            for block in range(self.nand.num_blocks):
                if block in self.nand.bad_blocks:
                    continue
                for page in range(self.nand.pages_per_block):
                    expectation = f"Block{block}_Page{page}"
                    actual = self.nand.read_page(block, page)
                    self.assertEqual(expectation, actual)
            logger.info("test_full_write_read_cycle passed.")
        except AssertionError as e:
            logger.error(f"FAILED: Mismatch in read-back data: {e}")
            raise
    
    def test_mass_erase(self):
        logger.info("Running test_mass_erase...")
        for block in range(self.nand.num_blocks):
            for page in range(self.nand.pages_per_block):
                try:
                    self.nand.write_page(block, page, "test")
                except:
                    continue
        
        try:
            for block in range(self.nand.num_blocks):
                self.nand.erase_block(block)
                for page in range(self.nand.pages_per_block):
                    self.assertIsNone(self.nand.read_page(block, page))
            logger.info("test_mass_erase passed.")
        except AssertionError as e:
            logger.error(f"FAILED: Erased block still has data: {e}")
            raise

if __name__ == "__main__":
    unittest.main()