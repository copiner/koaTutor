def addend(L=[]):
    L.append('end')
    return L

print(addend())
print(addend())

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())
