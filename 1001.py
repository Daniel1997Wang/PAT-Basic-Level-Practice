#!/usr/bin/env python
# -*- coding: utf-8 -*-

def PAT_count(num):
    count = 0
    while(num != 1):
        if(num % 2 == 0):
            num = num / 2
        else:
            num = (3 * num + 1) / 2
        count = count + 1
    return count

def main():
    x = input("")
    num = int(x)
    print(PAT_count(num))

if __name__ == '__main__':
    main()
