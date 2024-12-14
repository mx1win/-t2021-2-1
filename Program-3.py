def generate_series(a):
    if a%2 == 0:
        a -= 1
    series = [2*i + 1 for i in range(a)]
    return series
a = int(input("Enter an integer a: "))
result = generate_series(a)
print(", ".join(map(str, result)))