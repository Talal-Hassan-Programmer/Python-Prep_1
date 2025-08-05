# Element Search

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def search_element(element, lst):
    left = 0
    right = len(l1) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == element:
            return True
        elif lst[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    return False

X = int(input("Enter a number to search for: "))
print(search_element(X, l1))