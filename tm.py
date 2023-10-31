from timeit import timeit
from functools import reduce
from random import randint

def prod1(nums):
    return reduce(lambda x, y: x*y, nums)

def prod2(nums):
    prod = 1
    for i in nums:
        prod *= i
    return prod

if __name__ == "__main__":
    array = [randint(-10, 10) for i in range(12)]
    # print(array)

    timestamp1 = timeit('prod1(array)', globals=globals())
    timestamp2 = timeit('prod2(array)', globals=globals())

    print(f"It took {timestamp1:.2f}sec to execute prod1")
    print(f"It took {timestamp2:.2f}sec to execute prod2")
        
    input('~press enter to exit~')

