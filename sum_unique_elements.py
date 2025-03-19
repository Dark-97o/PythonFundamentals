def sum_unique_elements(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    return sum(num for num, count in frequency.items() if count == 1)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = sum_unique_elements(arr)
    print(result)
