class TestMathOperations:
    
    def add(self, x, y):
        return x + y
    
    def test_add(self):
        assert self.add(2, 3) == 5
        assert self.add(-1, 1) == 0