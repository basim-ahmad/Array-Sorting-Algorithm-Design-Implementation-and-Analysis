#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time



def selection_sort(arr):
    n = len(arr)
    num_comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            num_comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return num_comparisons

def insertion_sort(arr):
    num_comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            num_comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return num_comparisons

def merge(arr, l, m, r):
    num_comparisons = 0
    L = arr[l:m+1]
    R = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < len(L) and j < len(R):
        num_comparisons += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return num_comparisons

def merge_sort(arr, l, r):
    total_comparisons = 0
    if l < r:
        m = (l+r)//2
        total_comparisons += merge_sort(arr, l, m)
        total_comparisons += merge_sort(arr, m+1, r)
        total_comparisons += merge(arr, l, m, r)
    return total_comparisons

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    num_comparisons = 0
    for j in range(low, high):
        num_comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1, num_comparisons

def quick_sort(arr, low, high):
    total_comparisons = 0
    if low < high:
        pi, comps = partition(arr, low, high)
        total_comparisons += comps
        total_comparisons += quick_sort(arr, low, pi-1)
        total_comparisons += quick_sort(arr, pi+1, high)
    return total_comparisons

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    num_comparisons = 0
    if l < n:
        num_comparisons += 1
        if arr[l] > arr[largest]:
            largest = l
    if r < n:
        num_comparisons += 1
        if arr[r] > arr[largest]:
            largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        num_comparisons += heapify(arr, n, largest)
    return num_comparisons

def heap_sort(arr):
    n = len(arr)
    total_comparisons = 0
    for i in range(n//2 - 1, -1, -1):
        total_comparisons += heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        total_comparisons += heapify(arr, i, 0)
    return total_comparisons

def counting_sort(B):
    start_time = time.time()
    if not B:
        return 0, 0
    min_element = min(B)
    max_element = max(B)
    range_of_elements = max_element - min_element + 1
    C = [0] * range_of_elements
    sorted_B = [0] * len(B)
    num_comparisons = 0

    for number in B:
        C[number - min_element] += 1
    for i in range(1, range_of_elements):
        C[i] += C[i - 1]
    for i in reversed(range(len(B))):
        num_comparisons += 1
        sorted_B[C[B[i] - min_element] - 1] = B[i]
        C[B[i] - min_element] -= 1
    B[:] = sorted_B
    elapsed_time = (time.time() - start_time) * 1000  # Convert to ms
    return num_comparisons


def generate_array(n):
    return [random.randint(-10000, 10000) for _ in range(n)]

def test_single_algorithm():
    while True:
        print("\nChoose a sorting algorithm to test:")
        print("1. Selection Sort")
        print("2. Insertion Sort")
        print("3. Merge Sort")
        print("4. Quick Sort")
        print("5. Heap Sort")
        print("6. Counting Sort")
        print("7. Back")
        choice = int(input("Enter your choice (1-7): "))
        if choice == 7:
            break
        n = int(input("Enter the size of the array: "))
        array = generate_array(n)
        start_time = time.time()
        if choice == 1:
            comps = selection_sort(array)
        elif choice == 2:
            comps = insertion_sort(array)
        elif choice == 3:
            comps = merge_sort(array, 0, n-1)
        elif choice == 4:
            comps = quick_sort(array, 0, n-1)
        elif choice == 5:
            comps = heap_sort(array)
        elif choice == 6:
            comps = counting_sort(array)  # Your Counting Sort Function
        end_time = time.time()
        print(f"Sorted Array: {array[:10]}...")  # Show only first 10 elements
        print(f"Number of comparisons: {comps}")
        print(f"Run time (in ms): {(end_time - start_time) * 1000:.2f}")

algorithms = [
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", lambda arr: merge_sort(arr, 0, len(arr)-1)),
        ("Quick Sort", lambda arr: quick_sort(arr, 0, len(arr)-1)),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort)
        ]

def test_multiple_algorithms():
    n = int(input("Enter the size of the array: "))
    original_array = generate_array(n)
#     algorithms = [
#         ("Selection Sort", selection_sort),
#         ("Insertion Sort", insertion_sort),
#         ("Merge Sort", lambda arr: merge_sort(arr, 0, len(arr)-1)),
#         ("Quick Sort", lambda arr: quick_sort(arr, 0, len(arr)-1)),
#         ("Heap Sort", heap_sort),
#         ("Counting Sort", counting_sort)
#     ]
    print("\nSorting algorithm name\tArray size\tNum. of Comparisons\tRun time (in ms.)")
    for name, func in algorithms:
        array = original_array.copy()
        start_time = time.time()
        comps = func(array)
        end_time = time.time()
        print(f"{name}\t\t{n}\t\t{comps}\t\t\t{(end_time - start_time) * 1000:.2f}")

def average_results(results, num_runs):
    averaged_results = {name: {size: total / num_runs for size, total in sizes.items()} for name, sizes in results.items()}
    return averaged_results

def print_table(title, header, data):
    print(f"\n{title}")
    print("\t".join(["Sorting Algorithm"] + [str(h) for h in header]))
    for name, results in data.items():
        print(name, "\t".join(f"{result:.2f}" for result in results.values()), sep='\t\t')

def run_experiments(algorithms, sizes, num_runs=10):
    results_comparisons = {name: {size: 0 for size in sizes} for name, _ in algorithms}
    results_times = {name: {size: 0 for size in sizes} for name, _ in algorithms}

    for size in sizes:
        for _ in range(num_runs):
            original_array = [random.randint(-10000, 10000) for _ in range(size)]
            for name, func in algorithms:
                array = original_array.copy()
                start_time = time.time()
                comps = func(array)
                end_time = time.time()
                results_comparisons[name][size] += comps
                results_times[name][size] += (end_time - start_time) * 1000

    avg_comparisons = average_results(results_comparisons, num_runs)
    avg_times = average_results(results_times, num_runs)

    print_table("Table 1: Average number of comparisons for sorting arrays of n integers (over 10 runs).", sizes, avg_comparisons)
    print_table("Table 2: Average running time (in ms) for sorting arrays of n integers (over 10 runs).", sizes, avg_times)
        
def main_menu():
    sizes = [100, 200, 400, 800, 1000, 2000]
    
        
    while True:
        print("\nMain Menu:")
        print("1. Test an individual sorting algorithm")
        print("2. Test multiple sorting algorithms")
        print("3. Run Experimental Study")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            test_single_algorithm()
        elif choice == 2:
            test_multiple_algorithms()
        elif choice == 3:
            run_experiments(algorithms, sizes)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()


# In[ ]:




