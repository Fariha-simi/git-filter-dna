"""
Let's make some horrible operation in people's DNA
"""
user_dna_sequence = [
[
"Roksana Kozlova", 18, "GTTAGCCGACTTGGCXCTTT"
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
for element in user_dna_sequence :
    if (element[1]> 18 ) and (element[1] < 25) :
        arr.append(element)
print(arr)

arr2 = []
arr3 = []
for element in arr[0][2] :
    arr2.append(element)
    
#print(arr2)
arr2.reverse()
#print(arr2)

string1 = ""
for element in arr2 :
    string1 += element

print(string1)

for element in arr[1][2] :
    arr3.append(element)
    
#print(arr3)
arr3.reverse()
#print(arr3)

string2 = ""
for element in arr3 :
    string2 += element

print(string2)
