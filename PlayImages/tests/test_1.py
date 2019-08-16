import os
import sys
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.cmd_list = [
            'python -m plyimg -h',
            'python -m plyimg --video TestVideo/video.MP4 --step',
            'python -m plyimg --video TestVideo/video.MP4 --ri TestImages',
            'python -m plyimg --images TestImages --step',
            'python -m plyimg --images TestImages --fps -r',
            'python -m plyimg --images TestImages --step -t',
            'python -m plyimg --fps -r',
            ]

    def test_commands(self):
        for cmd in self.cmd_list:
            res = os.system(cmd)
            self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
