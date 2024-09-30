#!/usr/bin/env python3
#Author: Kushal Parmar
#File name: lab3d.py
#Date Created:30 Sept,2024

import os
import subprocess

def free_space():
    com = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(com, stdout=subprocess.PIPE, shell=True)
    output, error=process.communicate()

#p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    return output.decode('utf-8').strip()


print(free_space())
