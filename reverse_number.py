def test(i = 0, n = [], sum = 0):
    if i == len(n):
        return sum
    sum += n[i]
    return test(i + 1, n, sum)

def test2(n, name):
    if n == 0:
        return
    print("Name is", name)
    return test2(n-1, name)

def test3(i, n):
    if i == n:
        return
    print("1 to N", i)
    test3(i+1, n)

def test4(i, n):
    if i == n:
        return
    print("N to 1", n)
    test4(i, n-1)

def test5(i, n):
    if i < 1:
        return
    test5(i-1, n)
    print("Backtracking 1 to N :", i)

def test6(i, n):
    if i<0:
        return
    print("Backtracking n to 1 :", i)
    test6(i-1, n)

class Solution:
    def n_numbers_sum(self, N):
        if N == 1:
            return 1
        return N + self.n_numbers_sum(N - 1)

class Fibonacci:
    def print_fibo(self, n):
        fibo = []
        if n <= 1:
            return n
        val = self.print_fibo(n-1) + self.print_fibo(n-2)
        fibo.append(val)
        return fibo

if __name__ == "__main__":
    print(test(0, [1,2,3,4,5], 0))
    print(test2(5, "Sumanth"))
    print(test3(0, 5))
    print(test4(0, 5))
    print(test5(3, 3))
    print(test6(3, 3))
    sol = Solution()
    print(sol.n_numbers_sum(4))
    fib = Fibonacci()
    print(fib.print_fibo(10))