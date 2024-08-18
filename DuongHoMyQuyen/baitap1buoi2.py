# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:18:52 2024

@author: Student
"""

distance = float(input("Thong bao ket qua xep hang hoc luc:"))
if distance < 3.5:
    print("Hoc luc kem")
elif distance >=3.5 and distance < 5.0 :
    print("Hoc luc yeu")
elif distance >=5.0 and distance < 7.0 :
    print("Hoc luc trung binh")
elif distance >=7.0 and distance < 8.0:
    print("Hoc luc kha")
elif distance >= 8.0 and distance < 9.0:
    print("Hoc luc gioi")
elif distance >= 9.0 and distance <= 10.0:
    print("Hoc luc xuat sac")
                