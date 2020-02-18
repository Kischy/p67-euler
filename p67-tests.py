# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:37:45 2020

@author: kisch
"""


import unittest

from triangle_maximum import TriangleMaximum as TM


class TestTriangleMaximum(unittest.TestCase):
    
    def setUp(self):
        self.tm = TM()
        self.tm.import_triangle("test_triangle.txt")

        
    def test_import_triangle_data(self):
        ex = [[3],
              [7,4],
              [2,4,6],
              [8,5,9,3]]
        

        self.assertEqual(ex, self.tm.__tr_data__)
        
    def test_find_triagnle_maximum(self):        
        ex = 23
        self.assertEqual(ex, self.tm.find_triangle_maximum(3))
        
    def test_find_triagnle_maximum_p18(self):        
        self.tm.import_triangle("the_triangle_18.txt")
        ex = 1074
        self.assertEqual(ex, self.tm.find_triangle_maximum(3))
        
    def test_get_all_sums(self):
        ex = [20, 17, 19, 23, 16, 20, 22, 16]
        sums = []
        self.tm.__add_poss_sums__(sums,0,0,4)
        self.assertEqual(ex, sums)
        
        
    




if __name__ == '__main__':
    unittest.main(verbosity=0)
