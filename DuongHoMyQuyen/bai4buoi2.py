# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:37:15 2024

@author: Student
"""


a = float(input("Quang duong di"))
if a<=1:
    print("so tien:", 20*a)
elif a<=3:
    print("so tien:", a*13)
elif a>= 4 and a<= 8:
    print("so tien:", 3*13 +(a-3)*12)
else:
    x= 3*13 + 5*12+(a-8)*10
    if x>100:
        print("so tien:", x*0.92)
    else:
        print("so tien:"(3*13 + 5*12+(a-8)*10))