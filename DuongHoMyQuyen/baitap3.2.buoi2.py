# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:47:39 2024

@author: Student
"""

a= float(input("Nhap a="))
b= float(input("Nhap b="))
c= float(input("Nhap c="))
if a+b>c and a+c>b and b+c>c:
    print("la ba canh tam giac")
    if a==b ==c:
        print("Tam giac deu")
    elif a==b or b==c or c==a:
        print("Tam giac can")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
        print("Tam giac vuong")
else:
    print("a, b, c khong phai la ba canh tam giac")
    