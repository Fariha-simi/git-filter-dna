"""
Let's make some horrible operation in people's DNA
"""
user_dna_sequence = [
[
"Roksana Kozlova", 18, "GTTAAGCCGACTTGGCXCTTT"
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

print("for the 1st element of user_dna_sequence")
count = 0
count1 = 0
count2 = 0
count3 = 0
for elements in user_dna_sequence [0][2] :
    if elements == dna_elements[0] :
        count += 1
    if elements == dna_elements[1] :
        count1 += 1
    if elements == dna_elements[2] :
        count2 += 1
    if elements == dna_elements[3] :
        count3 += 1
print(dna_elements[0],count)
print(dna_elements[1],count1)    
print(dna_elements[2],count2)
print(dna_elements[3],count3)

print("for the 2nd element of user_dna_sequence")
count = 0
count1 = 0
count2 = 0
count3 = 0
for elements in user_dna_sequence [1][2] :
    if elements == dna_elements[0] :
        count += 1
    if elements == dna_elements[1] :
        count1 += 1
    if elements == dna_elements[2] :
        count2 += 1
    if elements == dna_elements[3] :
        count3 += 1
print(dna_elements[0],count)
print(dna_elements[1],count1)    
print(dna_elements[2],count2)
print(dna_elements[3],count3)

print("for the 3rd element of user_dna_sequence")
count = 0
count1 = 0
count2 = 0
count3 = 0
for elements in user_dna_sequence [2][2] :
    if elements == dna_elements[0] :
        count += 1
    if elements == dna_elements[1] :
        count1 += 1
    if elements == dna_elements[2] :
        count2 += 1
    if elements == dna_elements[3] :
        count3 += 1
print(dna_elements[0],count)
print(dna_elements[1],count1)    
print(dna_elements[2],count2)
print(dna_elements[3],count3)

print("for the 4th element of user_dna_sequence")
count = 0
count1 = 0
count2 = 0
count3 = 0
for elements in user_dna_sequence [3][2] :
    if elements == dna_elements[0] :
        count += 1
    if elements == dna_elements[1] :
        count1 += 1
    if elements == dna_elements[2] :
        count2 += 1
    if elements == dna_elements[3] :
        count3 += 1
print(dna_elements[0],count)
print(dna_elements[1],count1)    
print(dna_elements[2],count2)
print(dna_elements[3],count3)
