from typing import Dict

memo: Dict[int, int] = {0: 1, 1: 1}


def fib3(n: int) -> int:
    print(f"fib1({n})")
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


if __name__ == '__main__':
    print(fib3(5))
