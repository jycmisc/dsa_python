def print_items(a, b):
    for item in a:
        print(item)

    for item in b:
        print(item)

# O(a) + O(b) = O(a + b)

def print_items_nested(a, b):
    for item in a:
        for item2 in b:
            print(item, item2)

# O(a) * O(b) = O(a * b)