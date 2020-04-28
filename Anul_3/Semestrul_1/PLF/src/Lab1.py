"""
Created on 11/10/2018
@author Stefan
"""
'''
Problem 3
a.  isSet(List, Found)

true, if n == 0
isSet(T, Found + H),if H not in Found
false, if H is in Found

b.  numOfDist(List, Found)

0, if n == 0
numOfDist(T, Found), if H is is Found
1 + numOfDist(T, Found + H), if H not in Found

'''



class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None

class Lista:
    def __init__(self):
        self.prim = None


'''
crearea unei liste din valori citite pana la 0
'''
def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista

def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod

'''
tiparirea elementelor unei liste
'''
def tipar(lista):
    tipar_rec(lista.prim)

def tipar_rec(nod):
    if nod != None:
        print (nod.e)
        tipar_rec(nod.urm)


'''
Check if a list is a set.
'''

def isSet(list):
    return isSetRec(list.prim, [])

def isSetRec(nod, found):
    if nod == None:
        return True

    if nod.e in found:
        return False

    return isSetRec(nod.urm, found + [nod.e])


def numOfDistElems(list):
    return numOfDistElemsRec(list.prim, [])

def numOfDistElemsRec(nod, found):
    if nod == None:
        return 0

    if nod.e in found:
        return numOfDistElemsRec(nod.urm, found)

    return 1 + numOfDistElemsRec(nod.urm, found + [nod.e])


'''
program pentru test
'''

def main():
    list = creareLista()
    print("List is a set: ")
    print(isSet(list))

    print("Number of distinct elements: ")
    print(numOfDistElems(list))

main()
