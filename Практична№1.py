import math

a1 = int(input("������ a1: "))
a2 = int(input("������ a2: "))
b1 = int(input("������ b1: "))
b2 = int(input("������ b2: "))
m = int(input("������ m: "))


A = a1 * b1 - a2 * b2 / (m * a1 - a2 ** 2)

print("�������� A =", A)
