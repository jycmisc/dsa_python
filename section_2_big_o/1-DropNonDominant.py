def print_items(n):
    for i in range(n):
        for _ in range(n):
            print(i, _)

    for _ in range(n):
        print(_)

print_items(10)

# O(n^2 + n) = O(n^2