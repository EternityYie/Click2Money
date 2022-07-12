
fn1 = 1
fn2 = 1

n = input("Enter your Fib number: ")
n = int(n)

print("Numbers before", n, ":", end= " ")
for i in range(2, n):
    fn1, fn2=fn2, fn1 + fn2
    print(fn1, end = " ")

print("\nYour number is:", fn2)