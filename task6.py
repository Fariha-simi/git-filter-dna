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
print(arr)
print(arr[0])
if (len(arr[0])-1) == dna_elements[0]:
    print(arr[0])
