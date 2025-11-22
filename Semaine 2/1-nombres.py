
#  NOMBRES

a = 21
print(a)

b = int(-6)
print(b)

c = int(True)
print(c)

d = int('22', 0)
print(d)

# 22 --> base de 10
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 22 = 2*(0*10)p 0 + 2*(1*10)p 1
# 20 + 2 = 22

e = int('22', 16)       
print(e)

# 22 --> base de 16
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
# 22 = 2*(0*16)p 0 + 2*(1*16)p 1
# 2 + 32 = 34

# 22 --> base de 8
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
# 22 = 2*(0*8)p 0 + 2*(1*8)p 1


print(int('22', 8))

print(int('0X22', 0))

print(int('0O22', 0))

print(int('0b11', 0))

print(int('0b111', 0))