# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:08:26 2024

@author: Student
"""

distance = float(input("Nhap do dai doan duong den truong(m):"))
if distance < 300:
    print("Duong den truong qua gan. Thoi! Di bo")
elif distance > 1200:
    print("Duong de truong qua xa. Thoi! Di xe may")
elif distance >=300 and distance <= 700:
    print("Duong den truong khong xa. Thoi! Di xe dap")
else:
    print("Khong xac dinh")
