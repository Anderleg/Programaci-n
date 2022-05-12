# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:56:30 2022

@author: ANDERSON
"""

acl=int(input("Ingrese el # de CL"))
if acl >=1 and acl <=99:
    print("ACL ES ESTANDAR")
elif acl >=100 and acl <=199:
    print("ACL ES ESTANDAR") 
else:
    print("El dato ingresado no es un ACL")
    