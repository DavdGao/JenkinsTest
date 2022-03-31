# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest
import os

class MFTest(unittest.TestCase):
    def setUp(self):
        print(('Testing %s.%s' % (type(self).__name__, self._testMethodName)))
       

    def test_mf_standalone(self):
        print('!!!!!')
        print('!!!!!')
        self.assertTrue(os.path.exist('tests/test_abc.py'))


if __name__ == '__main__':
    unittest.main()
