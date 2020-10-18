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

string = ""
string = user_dna_sequence[0][2]

for element in range(len(string)) :
    if string == dna_elements[0] :
        print(string)
    else :
        print("not A")
    
    
    
#actual_dna = "ATGCGCGGA"
#mutated_dna = "AAGCGCGGA"

#for index in range(len(actual_dna)):
 #   if actual_dna[index] != mutated_dna[index]:
  #      print(actual_dna[index], mutated_dna[index], index)


