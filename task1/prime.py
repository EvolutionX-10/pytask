# find prime number in an array

arr = input("Enter array: ")
arr = arr.split()
arr = [int(i) for i in arr]

prime = []
for i in arr:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

print("Prime numbers are: ", prime)
