# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:37:45 2020

@author: kisch
"""

from triangle_maximum import TriangleMaximum as TM


problem_number = 67


print("Calculation started")


tm = TM()
tm.import_triangle("the_triangle_67.txt")

answers = []

for depth in range(1,20):
    val = tm.find_triangle_maximum(depth=depth)
    answers.append(val)
    print("Depth = ", depth, "\tSum = ", val)


the_answer = max(answers)

print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)


