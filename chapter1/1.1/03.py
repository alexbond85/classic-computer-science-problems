def fib4(n: int) -> int:
    print(f"fib1({n})")
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)


if __name__ == '__main__':
    print(fib4(5))
