# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if isinstance(x, int) and isinstance(y,int) and 0<= x <=100 and 0 <= y <=100:
        return x+y
    else:
        return -1
