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

string1 = user_dna_sequence[0][2]
for index in range(19,len(string1)) :
    #print(string1[index],index)
     if string1[20] == "G" :
        
         print(user_dna_sequence[0])
        

string2 = user_dna_sequence[1][2]
for index in range(18,len(string2)) :
    #print(string1[index],index)
     if string2[18] == "G" :
        
         print(user_dna_sequence[1])
        

string3 = user_dna_sequence[2][2]
for index in range(18,len(string3)) :
    #print(string1[index],index)
     if string3[18] == "G" :
        
         print(user_dna_sequence[2])
        

string4 = user_dna_sequence[3][2]
for index in range(17,len(string3)) :
    #print(string1[index],index)
     if string3[17] == "G" :
        
         print(user_dna_sequence[3])
        



