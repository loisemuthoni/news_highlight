import unittest
from app.models import Sources
# Sources = sources.Sources

class TestSources(unittest.TestCase):
    '''
    Test class to test the behaviour of the sources class
    '''
    def setUp(self):
        '''
        Setup method that will run before every test
        '''
        self.new_sources = Sources('cbs-news', 'CBS News', 'CBS News: dedicated to providing the best in journalism under standards it pioneered at the dawn of radio and television and continue in the digital age.', 'http://www.cbsnews.com', 'general', 'en', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources, Sources))
        
        
if __name__ == '__main__':
    unittest.main()
        
        
