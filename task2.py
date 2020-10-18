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
]
]

dna_elements = ["A", "T", "G", "C"]

arr = []
valid = True
for element in user_dna_sequence[0][2] :
    if element in dna_elements :
        print(element, end = ' ')
       
for element in user_dna_sequence[1][2] :
    if element in dna_elements :
        print(element,end = ' ')
for element in user_dna_sequence[2][2] :
    if element in dna_elements :
        print(element,end=' ')
for element in user_dna_sequence[3][2] :
    if element in dna_elements :
        print(element,end = ' ')
                   
