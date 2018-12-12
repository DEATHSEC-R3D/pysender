#!/usr/bin/python
# -*- coding: utf-8 -*-
#giorgi zirakashvili
import imp_moduls
while True:
    filename = input("File: ")
    if imp_moduls.imp_funcs.os.path.exists(filename):
        print("faili arsebobs!")
        imp_moduls.send_mail_py(filename)
        print("Maili gaigzavna warmatebit :) ")
    else:
        print("faili ar arsebobs!")
        imp_moduls.send_mail_py()
        print("Maili gaigzavna warmatebit :) ")
