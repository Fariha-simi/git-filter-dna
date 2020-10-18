"""
Let's make some horrible operation in people's DNA
"""
user_dna_sequence = [
[
"Roksana Kozlova", 18, "GTTAGCCGACTTGGCXCTTTA"
],
[
"Roza Kiseleva", 19, "ATTTGGCGAATTGGCCTTT"
],
[
"Kliment Volkov", 27, "ATTTGACCAATTGZGCAAA"
],
[
"Afanas Morozov", 22, "ATTTGACCGATTNGGCAA"
],
]

dna_elements = ["A", "T", "G", "C"]

arr = []
arr.append(user_dna_sequence[0][2])
arr.append(user_dna_sequence[1][2])
arr.append(user_dna_sequence[2][2])
arr.append(user_dna_sequence[3][2])
#print(arr)

arr1 = []
for i in arr[0] :
    arr1.append(i)
#print(arr1)
arr1.reverse()
#print(arr1)
if arr1[0] == dna_elements[1] :
    print(arr[0])
else :
    print("Last element is not T.")

arr2 = []
for i in arr[1] :
    arr2.append(i)
#print(arr2)
arr2.reverse()
#print(arr2)
if arr2[0] == dna_elements[1] :
    print(arr[1])
else :
    print("Last element is not T.")

arr3 = []
for i in arr[2] :
    arr3.append(i)
#print(arr3)
arr3.reverse()
#print(arr3)
if arr3[0] == dna_elements[1] :
    print(arr[2])
else :
    print("Last element is not T.")

arr4 = []
for i in arr[3] :
    arr4.append(i)
#print(arr4)
arr4.reverse()
#print(arr4)
if arr4[0] == dna_elements[1] :
    print(arr[3])
else :
    print("Last element is not T.")


