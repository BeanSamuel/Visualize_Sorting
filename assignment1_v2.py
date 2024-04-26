import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.axes_grid1.inset_locator import inset_axes



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
        # print(arr)
        self.is_sorted = False
        self.stack = [(i,i) for i in range(len(self.arr))]
        self.ax = ax
        self.ax_inset = inset_axes(self.ax, width="60%", height="20%", loc='upper left')
        self.tmp = []
        self.tmp_record = []

    def update(self):
        self.tmp = []
        if self.is_sorted or len(self.stack) <= 1:
            self.is_sorted = True
            return
        left1, right1 = self.stack.pop(0)
        left2, right2 = self.stack.pop(0)
        if right1 > right2:
            self.stack.append((left1,right1))
            left1, right1 = left2, right2
            left2, right2 = self.stack.pop(0)
        i = left1
        j = left2
        while i <=right1  and j <= right2:
            if self.arr[i] > self.arr[j]:
                self.tmp.append(self.arr[j])
                j += 1
            else:
                self.tmp.append(self.arr[i])
                i += 1
            self.tmp_record.append(list(self.tmp))
        while i<=right1:
            self.tmp.append(self.arr[i])
            i+=1
            self.tmp_record.append(list(self.tmp))
        while j<=right2:
            self.tmp.append(self.arr[j])
            j+=1
            self.tmp_record.append(list(self.tmp))
        self.stack.append((left1,right2))
        for i in range(left1,right2+1):
            self.arr[i] = self.tmp[i-left1]
    

    def draw(self,frame=None):
        if frame == None:
            self.ax.set_title("Merge Sort")
        else :
            self.ax.set_title(f"Merge Sort Frame: {frame}")
        if len(self.tmp_record) == 0:
            self.ax.clear()
            self.ax.bar(range(1, len(self.arr) + 1), self.arr, color="skyblue")
        elif len(self.tmp_record) > 0:
            tmp_arr = self.tmp_record.pop(0)
            tmp_arr = tmp_arr + [0] * (len(self.arr) - len(tmp_arr))
            self.ax_inset.clear()
            self.ax_inset.set_ylim(0, len(self.arr) + 1)
            self.ax_inset.bar(range(1,len(self.arr) + 1), tmp_arr , color="skyblue")
            self.ax_inset.plot([0])



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
    # arr = list(np.random.choice(range(1, 51), 50, replace=False))
    arr = [i for i in range(10,0,-1)]

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
        # bubblesort.draw(frame=frame)
        bubblesort.draw()
        
    # Insertion Sort
    if not insertionsort.is_sorted:
        insertionsort.update()
        insertionsort.draw(frame=frame)
        insertionsort.draw()

    # Merge Sort
    if not mergesort.is_sorted:
        if len(mergesort.tmp_record) == 0:
            mergesort.draw()
            mergesort.update()
        # mergesort.draw(frame=frame)
        mergesort.draw()

    # Quick Sort
    if not quicksort.is_sorted:
        quicksort.update()
        # quicksort.draw(frame=frame)
        quicksort.draw()

    # Heap Sort
    if not heapsort.is_sorted:
        heapsort.update()
        # heapsort.draw(frame=frame)
        heapsort.draw()

    # Bogo Sort
    if not bogosort.is_sorted:
        bogosort.update()
        bogosort.draw(frame=frame)


if __name__ == "__main__":
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(14, 6))

    ani = FuncAnimation(
        fig, update, init_func=init, frames=range(10000), interval=500, repeat=False
    )
    plt.show()
