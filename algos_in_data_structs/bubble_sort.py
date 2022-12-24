# Bubble sort - Optimized vs Unoptimized

def bubble_optimitzed(A):
    iterations = 0
    for i in range(len(A)):
        # this - 1 for range is due to one being already sorted
        for j in range(len(A) - i - 1):

            #print(j)

            iterations += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A, iterations

A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_optimitzed(A))