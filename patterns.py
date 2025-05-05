n = 5

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

print("\n==================================================================\n")

for i in range(n):
    for j in range(0, i+1):
        print("*", end="")
    print()

print("\n==================================================================\n")

for i in range(n):
    for j in range(1, i+2):
        print(j, end="")
    print()

print("\n==================================================================\n")

for i in range(1, n):
    for j in range(0, i):
        print(i, end="")
    print()

print("\n==================================================================\n")

for i in range(n):
    for j in range(0, n-i + 1):
        print("*", end="")
    print()

print("\n==================================================================\n")

for i in range(n):
    for j in range(1, n-i + 1):
        print(j, end="")
    print()

print("\n==================================================================\n")

for i in range(n):
    for j in range(0, n - i - 1):
        print(" ", end="")
    for j in range(0, 2 * i + 1):
        print("*", end="")
    for j in range(0, n - i - 1):
        print(" ", end="")
    print()

print("\n==================================================================\n")

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(0, 2 * n - (2*i + 1)):
        print("*", end="")
    for j in range(i):
        print(" ", end="")
    print()

print("\n==================================================================\n")


