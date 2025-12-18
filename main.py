# TASKS

# 1.

n = int(input("Musbat son kiriting(n>0): "))
m = int(input("Qaysi sonning darajasi: "))
asl_son = n
k = 0

while n > 1:
    n //= m
    k += 1
if m**k == asl_son and asl_son > 0:
    print(f"{asl_son} = {m}^{k}")
    print(f"k = {k}")
else:
    print(f"{asl_son} soni {m} ning darajasi emas")

