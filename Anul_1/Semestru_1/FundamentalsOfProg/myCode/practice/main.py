"""
Created on 29/01/2017
@author Stefan
"""

if __name__ == '__main__':
    def f1(l, n):
        l = l+[n]
    def g1(l):
        l *= 2
    def h1(l,n):
        l.extend([n])

    def m1():
        l=[1,2]
        n=3
        f1(l,n)
        print(l)
        g1(l)
        print(l)
        h1(l, 3)
        print(l)

m1()
