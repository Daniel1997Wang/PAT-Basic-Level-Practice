#!/usr/bin/env python
# -*- coding: utf-8 -*-

def PAT_sum(num):
    sum = 0
    for i in range(len(num)):
        sum = sum + int(num[i])
    return sum

def change(num):
    str_num = str(num)
    len_str_num = len(str_num)
    for i in range(len_str_num):
        PAT_print(int(str_num[i]))
        if i != (len_str_num - 1):
            print(" ", end="")

def PAT_print(num):
    GBK_num = ["ling","yi","er","san","si","wu","liu","qi","ba","jiu"]
    print(GBK_num[num],end = "")

def main():
    x = input("")
    change(PAT_sum(x))

if __name__ == '__main__':
    main()
