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
    if element[1] < 20 :
        arr.append(element)
print(arr)

for i in arr[0][2] :
    arr[0][2] = i.replace("T","C")
    arr[0][2] = i.replace("G","A")
    print(arr[0][2], end = '')
     
for i in arr[1][2] :
    arr[1][2] = i.replace("T","C")
    arr[1][2] = i.replace("G","A")
    print(arr[1][2], end = '')  
