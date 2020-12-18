a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(input("Write a number : "))


inferior = []

for i in range(len(a)-1):
    if (number > a[i]):
        inferior.append(a[i])

print(f'The numbers from the list smaller than {number} are : {inferior}')
