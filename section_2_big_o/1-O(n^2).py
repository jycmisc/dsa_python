def print_items(n):
    for i in range(n):
        for _ in range(n):
            print(i, _)

print_items(10)

# O(n^2)