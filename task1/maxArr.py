# find max number in an array

arr = input("Enter array: ")
arr = arr.split()
arr = [int(i) for i in arr]

max = arr[0]

for i in arr:
    if i > max:
        max = i

print("Max number is: ", max)
