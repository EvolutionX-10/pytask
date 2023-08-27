# implement any sorting algorithm

def sort(arr):
	for i in range(len(arr)):
		min = i
		for j in range(i+1, len(arr)):
			if arr[min] > arr[j]:
				min = j
		arr[i], arr[min] = arr[min], arr[i]

	return arr

arr = input("Enter array: ")
arr = arr.split()
arr = [int(i) for i in arr]

print("Sorted array is: ", sort(arr))