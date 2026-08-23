# Space Complexity:
# The space complexity of this program is O(1).
#
# The array 'arr' contains a fixed number of elements,
# so its memory usage remains constant.
#
# The function f() does not create any additional data
# structure or allocate memory that grows with the input.
#
# arr[4] directly accesses the 5th element of the array.
# Accessing one element requires constant extra space.
#
# Therefore:
# Auxiliary Space Complexity = O(1)
# Overall Space Complexity   = O(1)


arr = [10, 200, 3000, 40000, 5000000, 6000000, 800000000000]

def f():
    # Accessing the element at index 4.
    # Indexing does not require extra space.
    print(arr[4])

f()