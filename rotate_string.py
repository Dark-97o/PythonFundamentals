def rotate_string(s, k):
    n = len(s)
    k = k % n  # Normalize k
    return s[-k:] + s[:-k]

if __name__ == "__main__":
    s = input("Enter the string: ")
    k = int(input("Enter the number of positions to rotate: "))
    rotated = rotate_string(s, k)
    print("Rotated string:", rotated)
