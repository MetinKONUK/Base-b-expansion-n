import math
def binary_expansion(n, b):
    res = ""
    q = n
    k = 0
    while q!=0:
        ak = q % b
        res += str(ak)
        q = math.floor(q / b)
        k += 1
    return res[::-1]
print(binary_expansion(35,2))
