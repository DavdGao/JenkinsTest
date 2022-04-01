# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest
import os

class MFTest(unittest.TestCase):
    def setUp(self):
        print(('Testing %s.%s' % (type(self).__name__, self._testMethodName)))

    def test_dir(self):
        self.assertTrue(os.path.exists('tests/test_abc.py'))



if __name__ == '__main__':
    unittest.main()
