import time
def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return f(n - 1) + f(n - 2)
print("-------begin-------")
t1 = time.time();print(t1)
_f = f(5)
t2 = time.time();print(t2)
print("value = %d use: %fs"%(_f, t2-t1))
for i in range(1, 101):
    print(i, ": ", f(i))