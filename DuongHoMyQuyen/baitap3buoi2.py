# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:54:27 2024

@author: Student
"""

a= float(input("Nhap a="))
b= float(input("Nhap b="))
c= float(input("Nhap c="))
if a+b>c and a+c>b and b+c>a:
    print("a, b, c la ba canh tam giac")
else:
    print("a, b, c khong phai la ba canh tam giac")