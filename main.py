# code sorting algorithm for a list of numbers using various sorting algorithms
# and comparing their performance in terms of time taken to sort the list

import random
import time
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


# create a class for the sorting algorithms then ask the user to choose which algorithm to use
# then generate a list of random numbers and sort them using the chosen algorithm ask the user if they want to continue
# if yes then generate another list of random numbers and sort them using the same algorithm
# if no then ask the user if they want to choose another algorithm

def plot_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Number of elements')
    plt.ylabel('Time taken')
    plt.title('Sorting Algorithms')
    plt.show()


class SortingAlgorithms:
    def __init__(self):
        self.merge = None
        self.numbers = []
        self.sorted_numbers = []
        self.start_time = 0
        self.end_time = 0
        self.time_taken = 0

    def generate_random_numbers(self):
        self.numbers = [random.randint(0, 1000) for _ in range(1000)]
        return self.numbers

    def bubble_sort(self):
        self.start_time = time.time()
        for i in range(len(self.numbers) - 1):
            for j in range(len(self.numbers) - 1 - i):
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return self.numbers, self.time_taken

    def selection_sort(self):
        self.start_time = time.time()
        for i in range(len(self.numbers) - 1):
            min_index = i
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[j] < self.numbers[min_index]:
                    min_index = j
            self.numbers[i], self.numbers[min_index] = self.numbers[min_index], self.numbers[i]
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return self.numbers, self.time_taken

    def insertion_sort(self):
        self.start_time = time.time()
        for i in range(1, len(self.numbers)):
            current_value = self.numbers[i]
            position = i
            while position > 0 and self.numbers[position - 1] > current_value:
                self.numbers[position] = self.numbers[position - 1]
                position -= 1
            self.numbers[position] = current_value
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return self.numbers, self.time_taken

    def merge_sort(self, numbers):
        if len(numbers) > 1:
            mid = len(numbers) // 2
            left_half = numbers[:mid]
            right_half = numbers[mid:]

            self.merge_sort(left_half)
            self.merge
            self.merge_sort(right_half)
            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    numbers[k] = left_half[i]
                    i += 1
                else:
                    numbers[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                numbers[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                numbers[k] = right_half[j]
                j += 1
                k += 1
        return numbers

    def quick_sort(self, numbers):
        if len(numbers) <= 1:
            return numbers
        else:
            pivot = numbers.pop()
        items_greater = []
        items_lower = []
        for item in numbers:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)

    def heap_sort(self, numbers):
        self.start_time = time.time()
        for i in range(len(numbers), -1, -1):
            self.heapify(numbers, len(numbers), i)
        for i in range(len(numbers) - 1, 0, -1):
            numbers[i], numbers[0] = numbers[0], numbers[i]
            self.heapify(numbers, i, 0)
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return numbers, self.time_taken

    def heapify(self, numbers, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and numbers[i] < numbers[left]:
            largest = left
        if right < n and numbers[largest] < numbers[right]:
            largest = right
        if largest != i:
            numbers[i], numbers[largest] = numbers[largest], numbers[i]
            self.heapify(numbers, n, largest)

    def shell_sort(self, numbers):
        self.start_time = time.time()
        gap = len(numbers) // 2
        while gap > 0:
            for i in range(gap, len(numbers)):
                current_value = numbers[i]
                position = i
                while position >= gap and numbers[position - gap] > current_value:
                    numbers[position] = numbers[position - gap]
                    position -= gap
                numbers[position] = current_value
            gap //= 2
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return numbers, self.time_taken

    def bucket_sort(self, numbers):
        self.start_time = time.time()
        largest = max(numbers)
        length = len(numbers)
        size = largest / length
        buckets = [[] for _ in range(length)]
        for i in range(length):
            j = int(numbers[i] / size)
            if j != length:
                buckets[j].append(numbers[i])
            else:
                buckets[length - 1].append(numbers[i])
        for i in range(length):
            self.insertion_sort()
        result = []
        for i in range(length):
            result = result + buckets[i]
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return result, self.time_taken

    def counting_sort(self, numbers):
        self.start_time = time.time()
        largest = max(numbers)
        length = len(numbers)
        result = [0] * length
        count = [0] * (largest + 1)
        for i in range(0, length):
            count[numbers[i]] += 1
        for i in range(1, largest + 1):
            count[i] += count[i - 1]
        i = length - 1
        while i >= 0:
            result[count[numbers[i]] - 1] = numbers[i]
            count[numbers[i]] -= 1
            i -= 1
        for i in range(0, length):
            numbers[i] = result[i]
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return numbers, self.time_taken

    def radix_sort(self, numbers):
        self.start_time = time.time()
        largest = max(numbers)
        exp = 1
        while largest / exp > 0:
            self.counting_sort(numbers)
            exp *= 10
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time
        return numbers, self.time_taken


# generate a list of random numbers and sort them using the chosen algorithm ask the user if they want to continue
# and plot the performance of the algorithm in terms of time taken to sort the list
def main():
    sorting_algorithms = SortingAlgorithms()
    while True:
        print("Choose the sorting algorithm you want to use:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Heap Sort")
        print("7. Shell Sort")
        print("8. Bucket Sort")
        print("9. Counting Sort")
        print("10. Radix Sort")
        print("11. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.bubble_sort()
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 2:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.selection_sort()
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 3:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.insertion_sort()
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 4:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.merge_sort(sorting_algorithms.numbers)
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 5:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.quick_sort(sorting_algorithms.numbers)
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 6:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.heap_sort(sorting_algorithms.numbers)
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 7:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.shell_sort(sorting_algorithms.numbers)
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 8:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.generate_random_numbers()
                sorting_algorithms.bucket_sort(sorting_algorithms.numbers)
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 9:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.counting_sort(sorting_algorithms.numbers)
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 10:
            x = []
            y = []
            for i in range(1000, 10001, 1000):
                sorting_algorithms.radix_sort(sorting_algorithms.numbers)
                x.append(i)
                y.append(sorting_algorithms.time_taken)
            plot_graph(x, y)
        elif choice == 11:
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
