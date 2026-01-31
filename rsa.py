import base64

p = 17099348593910752567
q = 13612755315628198297
e = 0x10001
n = p*q
phi = (p - 1)*(q - 1)
d = pow(e, -1, phi)
string = "wazzuuuuuuuuuuuuuuup"
m = string.encode('utf-8')
mtoi = int.from_bytes(m, byteorder='big', signed=False)
c = pow(mtoi, e, n)
print(c)