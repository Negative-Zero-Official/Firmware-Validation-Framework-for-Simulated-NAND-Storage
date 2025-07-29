class NANDSimulator:
    def __init__(self, num_blocks=16, pages_per_block=4):
        self.num_blocks = num_blocks
        self.pages_per_block = pages_per_block
        self.memory = {}
        self.bad_blocks = set()
    
    def _check_block_bounds(self, block):
        if block < 0 or block >= self.num_blocks:
            raise IndexError("Block index out of range.")

    def _check_bounds(self, block, page):
        self._check_block_bounds(block)
        if page < 0 or page >= self.pages_per_block:
            raise IndexError("Page index out of range.")

    def write_page(self, block, page, data):
        self._check_bounds(block, page)
        
        if block in self.bad_blocks:
            raise Exception(f"Write failed: Block {block} is marked as bad.")
        
        if (block, page) in self.memory:
            raise Exception("Cannot overwrite: Page already written. Must erase block first.")
        
        self.memory[(block, page)] = data
    
    def read_page(self, block, page):
        self._check_block_bounds(block)
        return self.memory.get((block, page), None)
    
    def erase_block(self, block):
        self._check_block_bounds(block)
        keys_to_erase = [key for key in self.memory if key[0] == block]
        for key in keys_to_erase:
            del self.memory[key]
    
    def inject_bad_block(self, block):
        self._check_block_bounds(block)
        self.bad_blocks.add(block)