# Space Complexity:
# The space complexity of this function is O(n).
#
# 'n' represents the number of elements we want to store.
#
# Initially, arr is an empty list.
# The loop runs n times.
# During every iteration, one element is added to arr.
#
# If n = 5:
# arr = [0, 1, 2, 3, 4]
#
# If n = 10:
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Therefore, the size of arr increases as n increases.
#
# Space used by arr = n
# Space Complexity = O(n)


def create_arr(n):
    arr = []

    for i in range(n):
        arr.append(i)

    return arr

print(create_arr(10))