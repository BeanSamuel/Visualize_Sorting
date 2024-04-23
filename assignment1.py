import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class BubbleSort:
    def __init__(self, arr, ax):
        self.arr = arr
        self.is_sorted = False
        self.idx = 1
        self.times = 1
        self.ax = ax

    def update(self):
        if self.is_sorted:
            return
        n = len(self.arr)
        for i in range(self.idx, n):
            if self.arr[i - 1] > self.arr[i]:
                self.arr[i - 1], self.arr[i] = self.arr[i], self.arr[i - 1]
                if i >= n - self.times:
                    self.times = self.times + 1
                    self.idx = 1
                    return
                else:
                    self.idx = i
                    return
        if self.times == n:
            self.is_sorted = True
            return
        self.idx = 1
        self.times = self.times + 1

    def draw(self,frame=None):
        self.ax.clear()
        if frame == None:
            self.ax.set_title("Bubble Sort")
        else :
            self.ax.set_title(f"Bubble Sort Frame: {frame}")
        self.ax.bar(range(1, len(self.arr) + 1), self.arr, color="skyblue")


class InsertionSort:
    def __init__(self, arr, ax):
        self.arr = arr
        self.is_sorted = False
        self.idx = 1
        self.times = 1
        self.ax = ax

    def update(self):
        if self.is_sorted or self.times >= len(self.arr):
            return
        n = len(self.arr)
        while self.times < n:
            while self.idx > 0:
                if self.arr[self.idx - 1] > self.arr[self.idx]:
                    self.arr[self.idx - 1], self.arr[self.idx] = (
                        self.arr[self.idx],
                        self.arr[self.idx - 1],
                    )
                    if self.idx == 1:
                        self.idx = self.times + 1
                        self.times = self.times + 1
                        return
                    else:
                        self.idx = self.idx - 1
                        return
                self.idx = self.idx - 1
            self.idx = self.times + 1
            self.times = self.times + 1
        self.is_sorted = True

    def draw(self,frame=None):
        self.ax.clear()
        if frame == None:
            self.ax.set_title("Insertion Sort")
        else :
            self.ax.set_title(f"Insertion Sort Frame: {frame}")
        self.ax.bar(range(1, len(self.arr) + 1), self.arr, color="skyblue")


class MergeSort:
    def __init__(self, arr, ax):
        self.arr = arr
        self.is_sorted = False
        self.idx = 0
        self.merge_length = 1
        self.left = 0
        self.right = 1
        self.mid = 1
        self.ax = ax

    def update(self):
        n = len(self.arr)
        if self.is_sorted or self.merge_length >= n:
            return
        while self.merge_length < n:
            while self.idx + self.merge_length < n:
                if self.left >= self.mid or self.right >= self.mid or self.left == 0:
                    self.left = self.idx
                    self.right = min(self.left + 2 * self.merge_length - 1, n - 1)
                    self.mid = self.left + self.merge_length
                while self.right >= self.mid:
                    while self.left < self.mid:
                        if self.arr[self.left] > self.arr[self.right]:
                            self.arr[self.left], self.arr[self.right] = (
                                self.arr[self.right],
                                self.arr[self.left],
                            )
                            return
                        self.left = self.left + 1

                    self.right = self.right - 1
                    self.left = self.idx

                self.idx = self.mid + self.merge_length
                self.left = self.idx
            self.merge_length = 2 * self.merge_length
            self.idx = 0
            self.left = 0
        self.is_sorted = True

    def draw(self,frame=None):
        self.ax.clear()
        if frame == None:
            self.ax.set_title("Merge Sort")
        else :
            self.ax.set_title(f"Merge Sort Frame: {frame}")
        self.ax.bar(range(1, len(self.arr) + 1), self.arr, color="skyblue")


class QuickSort:
    def __init__(self, arr, ax):
        self.arr = arr
        self.ax = ax
        self.is_sorted = False
        self.record = [(0, len(arr) - 1)]
        self.left = -1
        self.right = -1

    def update(self):
        if self.is_sorted:
            return
        while len(self.record) > 0:
            tmp_left, tmp_right = self.record.pop(0)
            if self.left == -1 and self.right == -1:
                self.left = tmp_left + 1
                self.right = tmp_right

            pivot = self.arr[tmp_left]
            while self.left <= self.right and self.arr[self.left] < pivot:
                self.left += 1
            while self.left <= self.right and self.arr[self.right] > pivot:
                self.right -= 1
            if self.left < self.right:
                self.arr[self.left], self.arr[self.right] = (
                    self.arr[self.right],
                    self.arr[self.left],
                )
                self.record.insert(0, (tmp_left, tmp_right))
                return
            if self.left >= self.right:
                self.arr[tmp_left], self.arr[self.right] = (
                    self.arr[self.right],
                    self.arr[tmp_left],
                )
                if tmp_right - self.left > 0:
                    self.record.insert(0, (self.left, tmp_right))
                if self.right - 1 - tmp_left > 0:
                    self.record.insert(0, (tmp_left, self.right - 1))
                self.left = self.right = -1
                return
        self.is_sorted = True

    def draw(self,frame=None):
        self.ax.clear()
        if frame == None:
            self.ax.set_title("Quick Sort")
        else :
            self.ax.set_title(f"Quick Sort Frame: {frame}")
        self.ax.bar(range(1, len(self.arr) + 1), self.arr, color="skyblue")


class HeapSort:
    def __init__(self, arr, ax):
        self.arr = arr
        self.ax = ax
        self.is_sorted = False
        self.record = []
        self.idx1 = len(self.arr) // 2 - 1
        self.idx2 = len(self.arr) - 1
        self.chk = False
        self.chk2 = True

    def update(self):
        if self.is_sorted:
            return
        self.chk = False
        n = len(self.arr)
        while len(self.record) > 0:
            n, largest = self.record.pop(0)
            self.heapify(n, largest)
            if self.chk:
                return
        while self.idx1 >= 0:
            self.heapify(n, self.idx1)
            self.idx1 = self.idx1 - 1
            if self.chk:
                return
        while self.idx2 > 0:
            if self.chk2:
                self.arr[0], self.arr[self.idx2] = self.arr[self.idx2], self.arr[0]
                self.chk2 = False
                return
            self.heapify(self.idx2, 0)
            self.idx2 = self.idx2 - 1
            self.chk2 = True
            if self.chk:
                return
        self.is_sorted = True

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and self.arr[i] < self.arr[l]:
            largest = l
        if r < n and self.arr[largest] < self.arr[r]:
            largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.chk = True
            self.record.insert(0, (n, largest))

    def draw(self,frame=None):
        self.ax.clear()
        if frame == None:
            self.ax.set_title("Heap Sort")
        else :
            self.ax.set_title(f"Heap Sort Frame: {frame}")
        self.ax.bar(range(1, len(self.arr) + 1), self.arr, color="skyblue")


class BogoSort:
    def __init__(self, arr, ax):
        self.arr = arr
        self.is_sorted = False
        self.sorted_arr = sorted(self.arr.copy())
        self.ax = ax

    def update(self):
        if self.is_sorted:
            return
        for i in range(len(self.arr) - 1):
            if self.arr[i] != self.sorted_arr[i]:
                self.arr = np.random.choice(range(1, len(self.arr) + 1), len(self.arr), replace=False)
                return
        self.is_sorted = True

        

    def draw(self,frame=None):
        self.ax.clear()
        if frame == None:
            self.ax.set_title("Bogo Sort")
        else:
            self.ax.set_title(f"Bogo Sort Frame: {frame}")
        self.ax.bar(range(1, len(self.arr) + 1), self.arr, color="skyblue")


def init():
    global bubblesort, insertionsort, mergesort, quicksort, heapsort, bogosort
    arr = np.random.choice(range(1, 51), 50, replace=False)
    # arr = [i for i in range(32,0,-1)]

    # Bubble Sort
    arr_bubblesort = arr.copy()
    bubblesort = BubbleSort(arr=arr_bubblesort, ax=ax1)
    bubblesort.draw()

    # Insertion Sort
    arr_insertionsort = arr.copy()
    insertionsort = InsertionSort(arr=arr_insertionsort, ax=ax2)
    insertionsort.draw()

    # Merge Sort
    arr_mergesort = arr.copy()
    mergesort = MergeSort(arr=arr_mergesort, ax=ax3)
    mergesort.draw()

    # Quick Sort
    arr_quicksort = arr.copy()
    quicksort = QuickSort(arr=arr_quicksort, ax=ax4)
    quicksort.draw()

    # Heap Sort
    arr_heapsort = arr.copy()
    heapsort = HeapSort(arr=arr_heapsort, ax=ax5)
    heapsort.draw()

    # Bogo Sort
    arr_bogosort = arr.copy()
    bogosort = BogoSort(arr=arr_bogosort, ax=ax6)
    bogosort.draw()


def update(frame):
    # print(f"Frame: {frame}")
    # Bubble Sort
    if not bubblesort.is_sorted:
        bubblesort.update()
        bubblesort.draw(frame=frame)
        
    # Insertion Sort
    if not insertionsort.is_sorted:
        insertionsort.update()
        insertionsort.draw(frame=frame)

    # Merge Sort
    if not mergesort.is_sorted:
        mergesort.update()
        mergesort.draw(frame=frame)

    # Quick Sort
    if not quicksort.is_sorted:
        quicksort.update()
        quicksort.draw(frame=frame)

    # Heap Sort
    if not heapsort.is_sorted:
        heapsort.update()
        heapsort.draw(frame=frame)

    # Bogo Sort
    if not bogosort.is_sorted:
        bogosort.update()
        bogosort.draw(frame=frame)


if __name__ == "__main__":
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(14, 6))

    ani = FuncAnimation(
        fig, update, init_func=init, frames=range(10000), interval=100, repeat=False
    )
    plt.show()
