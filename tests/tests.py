# Test Cases for the back end of the site

import unittest


class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass


    # Tests the "get-tweet" API call; will contain an blockquote element
    def testGetTweet(self):
        result = self.app.get('/api/get-tweet/')
        decoded = result.decode('utf-8')

        self.assertTrue(decoded.find('blockquote'))



def main():
    unittest.main()

if __name__ == '__main__':
    main()
