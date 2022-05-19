#!/usr/bin/env python
# coding: utf-8

#  # PROJECT                        

# ### CALCULATING TIME OF FOLLOWING SORTING ALGORYTMS 

# In[78]:


import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
arr=[]
students=[]
for i in range(0,3000):
    n = random.randint(1,300000)
    arr.append(n)
print("\n")
print("Given array is", end="\n")
print(arr)
print("\n")

#------------------------------------------
# YOU CAN TAKE INPUT USING THIS CODE :-

# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = int(input())  
#     arr.append(ele)
# arr= [12, 11, 13, 5, 6, 7]
# printList(arr)
#-----------------------------------------


begin = 0
# Python program for MergeSort
#-----------------------------------------
#TIMER BEINGS
begin = time.time()
def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2

		L = arr[:mid]

		R = arr[mid:]

		mergeSort(L)

		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
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

# Code to print the list
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

#-------------------------------------
mergeSort(arr)
end = time.time()
print("Merge Sorted array is: ")
print("--------------------------------------")
printList(arr)
print("--------------------------------------")
value1= (end - begin)/1000
students.append(value1)

# print(f"{value:.2f}")
print(f"Total runtime of the program is {value1} s")
print("\n")
#---------------------------------------
begin = 0

# Python program for Quick sort
#-----------------------------------------
#TIMER BEINGS
begin = time.time()
# Function to find the partition position
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
        (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)    


#-------------------------------------
quick_sort(arr, 0, len(arr) - 1)
end = time.time()
print("--------------------------------------")
print(arr)
print("--------------------------------------")
value2= (end - begin)/1000
students.append(value2)
# print(f"{value:.2f}")
print(f"Total runtime of the program is {value2} s")
print("\n")
#-------------------------------------

begin = 0
# Python program for heaap sort
#-----------------------------------------
#TIMER BEINGS
begin = time.time()

def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap
		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)


heapSort(arr)
end = time.time()
n = len(arr)
print("Quick Sorted array is")
print("--------------------------------------")
print(arr)
print("--------------------------------------")
value3= (end - begin)/1000
students.append(value3)
# print(f"{value:.2f}")
print(f"Total runtime of the program is {value3} s")
print("\n")

begin = 0
#insertions sort 
begin = time.time()
# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

insertionSort(arr)
end = time.time()
print("Insertion Sorted array is")
print("--------------------------------------")
print(arr)
print("--------------------------------------")
value4= (end - begin)/1000
students.append(value4)
print(f"Total runtime of the program is {value4} s")

begin = 0
print("--------------------------------------")
print(students)
print("--------------------------------------")
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = [ 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Insertion Sort']
ax.bar(langs,students)
plt.show()


# In[ ]:




