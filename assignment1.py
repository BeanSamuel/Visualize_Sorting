import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bubble_sort_step(parameters1):
    arr, is_sorted, idx, times = parameters1
    if is_sorted: return parameters1
    n = len(arr)
    for i in range(idx, n):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            if i>=n-times: return (arr, False, 1, times+1)
            else: return (arr, False, i, times)
    if times==n: return (arr, True, 1, times+1)
    return (arr, False, 1, times+1)

def insertion_sort_step(parameters2):
    arr, is_sorted, idx, times = parameters2
    if is_sorted or times >= len(arr): return (arr, True, idx, times)
    n = len(arr)
    while times<n:
        while idx>0:
            if arr[idx-1]>arr[idx]:
                arr[idx-1],arr[idx] = arr[idx], arr[idx-1]
                if idx==1: return (arr,False,times+1,times+1)
                else: return (arr,False,idx-1,times)
            idx-=1
        times+=1
        idx = times
    return (arr, True, idx, times)



def init():
    global parameters1, parameters2
    ax1.clear()
    ax1.bar(range(len(parameters1[0])), parameters1[0], color='skyblue')
    ax1.set_title('Bubble Sort')
    ax2.clear()
    ax2.bar(range(len(parameters2[0])), parameters2[0], color='skyblue')
    ax2.set_title('Insertion Sort')
    

def update(frame):
    global parameters1, parameters2

    #Bubble Sort
    if not parameters1[1]:
        parameters1 = bubble_sort_step(parameters1)
        ax1.clear()
        ax1.set_title(f'Bubble Sort - {frame} times')
        ax1.bar(range(len(parameters1[0])), parameters1[0], color='skyblue')
    
    # Insertion Sort
    if not parameters2[1]:
        parameters2 = insertion_sort_step(parameters2)
        ax2.clear()
        ax2.set_title(f'Insertion Sort - {frame} times')
        ax2.bar(range(len(parameters2[0])), parameters2[0], color='skyblue')

if __name__ == '__main__':
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(14, 6))
    random_arr = np.random.choice(range(1, 11), 10, replace=False)
    # random_arr = [10,9,8,7,6,5,4,3,2,1]
    
    #Bubble Sort
    arr1 = random_arr.copy()
    parameters1 = (arr1, False, 1, 1)
    
    # Insertion Sort
    arr2 = random_arr.copy()
    parameters2 = (arr2, False, 1, 1)

    ani = FuncAnimation(fig, update, init_func=init, frames=range(100), interval=100, repeat=False)
    plt.show()
