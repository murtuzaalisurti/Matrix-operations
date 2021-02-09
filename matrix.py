print("PLEASE ENTER 3x3 MATRIX \n")
arr = []
print("Enter nine elements: (For First Matrix) \n")
# User Input for the first Matrix
for i in range(9):
    print("Enter Element Number " , i+1  , "-->")
    arr.append(int(input()))
arr1 = []
print("Enter nine elements: (For Second Matrix) \n")
# User Input for the Second Matrix
for i in range(9):
    print("Enter Element Number " , i+1 , "-->")
    arr1.append(int(input()))
arr2 = []
arrLen = len(arr)
arr1Len = len(arr1)
arr3 = [] #Blank Array for Storing the Multiplication of Matrix

print("This is First Matrix (3x3): \n" )
index = 4
for i in range(arrLen):
    print(arr[i],' ' ,  end=' ')
    if (index % 3 == 0):
        print('\n')
    index+=1


print("This is Second Matrix (3x3): \n")
index1 = 4
for j in range(arr1Len):
    print(arr1[j], ' ' , end = ' ')
    if (index1 % 3 == 0):
        print('\n')
    index1+=1

# User choice for Addition/Subtract/Multiplication:

#addition
Code = input("What operation do you want to perform on these Matrices (Add or Substract or Multiplication)--> ")
if Code == "Add" or Code == "ADD" or Code == "add" or Code == "+":
    print("The Sum of these two above matrices will be: \n")
    for i in range(arrLen):
          arr2.append(arr[i] + arr1[i])
    
    indexans = 4
    for k in range(arrLen):
        print(arr2[k] , ' ' , end='')
        if (indexans % 3 == 0):
            print('\n')
        indexans+=1
#Subutaction
elif Code == "Subtract" or Code == "SUBTRACT" or Code == "subtract" or Code == "-":
    print("\nThe subtraction of these two above matrices will be: \n")
    for i in range(arrLen):
        arr2.append(arr[i] - arr1[i])

    indexans = 4
    for k in range(arrLen):
        print(arr2[k] , ' ' , end='')
        if (indexans % 3 == 0):
            print('\n')
        indexans+=1

#Multiplication
elif Code == "Multiply" or Code == "MULTIPLY" or Code == "multiply" or Code == "*":
    print("\nThe multiplication of these two above matrices will be: \n")
    for i in range(arrLen):
        #------------------------ ROW 1 -------------------------------------------
        arr3.append(((arr[0] * arr1[0]) + (arr[1] * arr1[3]) + (arr[2] * arr1[6])))
        arr3.append(((arr[0] * arr1[1]) + (arr[1] * arr1[4]) + (arr[2] * arr1[7])))
        arr3.append(((arr[0] * arr1[2]) + (arr[1] * arr1[5]) + (arr[2] * arr1[8])))
        #-------------------------- ROW 2 -----------------------------------------
        arr3.append(((arr[3] * arr1[0]) + (arr[4] * arr1[3]) + (arr[5] * arr1[6])))
        arr3.append(((arr[3] * arr1[1]) + (arr[4] * arr1[4]) + (arr[5] * arr1[7])))
        arr3.append(((arr[3] * arr1[2]) + (arr[4] * arr1[5]) + (arr[5] * arr1[8])))
        #------------------------- ROW 3 -----------------------------------------
        arr3.append(((arr[6] * arr1[0]) + (arr[7] * arr1[3]) + (arr[8] * arr1[6])))
        arr3.append(((arr[6] * arr1[1]) + (arr[7] * arr1[4]) + (arr[8] * arr1[7])))
        arr3.append(((arr[6] * arr1[2]) + (arr[7] * arr1[5]) + (arr[8] * arr1[8])))

    indexans = 4
    for l in range(arrLen):
        print(arr3[l] , ' ' , end='')
        if (indexans % 3 == 0):
            print('\n')
        indexans+=1
