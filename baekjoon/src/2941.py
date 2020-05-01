# 크로아티아 알파벳
import sys

I = sys.stdin.readline().rstrip()
I = I.replace("dz=", "#")
I = I.replace("lj", "%")
I = I.replace("nj", "^")
I = I.replace("c=", "!")
I = I.replace("c-", "@")
I = I.replace("z=", "*")
I = I.replace("d-", "$")
I = I.replace("s=", "&")

print(len(I))