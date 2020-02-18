# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:37:45 2020

@author: kisch
"""

from copy import deepcopy 


class TriangleMaximum():
    

    def __init__(self):
        self.__tr_data__ = []
        
    def __add_numbers_to_data__(self,nums):
        ind = len(self.__tr_data__)-1
                
        for num in nums:
            if(len(num) > 0):
                self.__tr_data__[ind].append(int(num))
        
    def __read_tr_line__(self,line):
        self.__tr_data__.append([])
        
        if(line[-1] == "\n"):
            line = line[:-1]
            
        nums = line.split(" ")
        self.__add_numbers_to_data__(nums)        
        
    
    def import_triangle(self,filename):
        self.__tr_data__ = []
        
        with open(filename,"r") as file:
            lines = file.readlines()
            for line in lines:
                self.__read_tr_line__(line)            
    
        
    
    def __add_poss_sums__(self, sums, row, column, depth):
        if(depth == 0):
            return
        
        if(row >= len(self.__tr_data__)):
            return    
        
        if(len(sums) == 0):
            sums.append(self.__tr_data__[row][column])
            self.__add_poss_sums__(sums,row+1,column,depth-1)
        else:
            ind = len(sums)-1        
            top_sum = deepcopy(sums[ind])
            sums[ind] += self.__tr_data__[row][column] # add left value
            self.__add_poss_sums__(sums, row+1, column, depth-1) #go left down
            
            sums.append(top_sum + self.__tr_data__[row][column+1]) # add right value and append 
            self.__add_poss_sums__(sums, row+1, column+1, depth-1) # go right down
            
        
    def __get_max_sum__(self, row, column, depth):
        sums = []
        self.__add_poss_sums__(sums, row, column, depth)        
        
        return max(sums)

    def __get_sec_index_with_max_sum__(self,row, column, depth):
        left_sum = self.__get_max_sum__(row, column, depth)             
        right_sum = self.__get_max_sum__(row, column+1, depth)    
        
        if(left_sum >= right_sum):
            return column
        else:
            return column+1               
         
    
    def find_triangle_maximum(self, depth):
        the_sum = 0
        sec_i = 0
        
        for i in range(len(self.__tr_data__)-1):
            the_sum += self.__tr_data__[i][sec_i]            
            sec_i = self.__get_sec_index_with_max_sum__(i+1,sec_i,depth)
            
            
        the_sum += self.__tr_data__[len(self.__tr_data__)-1][sec_i]            
        
        return the_sum
    
    
    
    