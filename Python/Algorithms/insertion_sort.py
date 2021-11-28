def insertion_sort(A):
    # input: an array of numbers <a1,a2,a3,...,an>
    # output: a sorted array of numbers <a1',a2',a3',..an'>
    # such that a1' <= a2' <= a3' <= ... <= an'

    for i in range(1,len(A)):
        j = i - 1
        key = A[i]
        while j >= 0 and A[j] > key: # A[j] < key to sort in descending order
            # swap
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A


if __name__ == '__main__':
    print(insertion_sort([9,3,8,5,7,3,7,4,8]))