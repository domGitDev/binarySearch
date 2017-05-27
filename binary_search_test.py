import pytest
from binary_search import binary_search


class TestBinarySearch:
    def setup(self):
        self.data = (2, 3, 5, 7, 11, 13, 17,
                19, 23, 29, 31, 37, 41,
                43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97)
    
    def test_binary_search(self):
        index = binary_search(self.data, 73) 
        print '\n[{}]={}'.format(index, self.data[index])
        assert 20 == index
        assert self.data[20] == self.data[index]
        
    def test_binary_search_not_found(self):
        index = binary_search(self.data, 10)
        print '\n', index
        assert -1 == index
        
        index = binary_search(self.data, 200)
        print '\n', index
        assert -1 == index
        


if __name__ == '__main__':
    pytest.main('-s')
    
