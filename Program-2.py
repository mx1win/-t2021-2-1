def generate_series(a):
    series = []
    for i in range(a):
        series.append(2*i + 1)
    return series
a = int(input("Enter an integer a: "))
result = generate_series(a)
print(", ".join(map(str, result)))
