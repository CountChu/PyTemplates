import os
import sys
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.cmd_list = [
            'python cmd_app.py -h',
            'python -m cmd_app -h',
            'python -m cmd_app README.md',
            'python -m cmd_app README.md -d images',
            'python -m cmd_app README.md -d images -o output',
            'python -m cmd_app README.md -d images -o output --log',
            'python -m cmd_app README.md -d images -o output --log --level info',
            'python -m cmd_app README.md --cfg',            
            ]

    def test_commands(self):
        for cmd in self.cmd_list:
            print('cmd = %s' % cmd)
            res = os.system(cmd)
            self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
