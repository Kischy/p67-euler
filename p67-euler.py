# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:16:13 2019

@author: kisch
"""

from triangle_maximum import TriangleMaximum as TM


problem_number = 67


print("Calculation started")


tm = TM()
tm.import_triangle("the_triangle.txt")

answers = []

for depth in range(1,16):
    val = tm.find_triangle_maximum(depth=depth)
    answers.append(val)
    print("Depth = ", depth, "\tSum = ", val)


the_answer = max(answers)

print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)


