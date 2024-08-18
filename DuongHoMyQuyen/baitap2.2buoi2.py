# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:07:22 2024

@author: Student
"""
import math 
a= float(input("Nhap a="))
b= float(input("Nhap b="))
c= float(input("Nhap c="))
if a == 0:
        if b==0:
            if c==0:
                print("Phuong trinh vo so nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
          if c==0:
              print("Phuong trinh co 1 nghiem x =0")
          else:
              print("Phuong trinh co 1 nghiem x=", -c/b)
else:
    delta = b ** 2-4*a*c
if delta<0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co nghiem kep: x1=x2= ", -(b/(2*a)))
elif delta> 0:
    print("Phuong trinh co hai nghiem phan biet:")
    print("x1=", (-(b)+ math.sqrt(delta))/(2*a))
    print("x2=", (-(b)- math.sqrt(delta))/(2*a))