alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", \
"r","s","t","u","v","w","x","y","z",' ']
number = ["0","1","2","3","4","5","6","7","8","9","-"]

index1 = alphabet[22]+alphabet[4]+alphabet[26]+alphabet[0]+alphabet[17]+alphabet[4]+alphabet[26] \
    +alphabet[18]+alphabet[10]+alphabet[7]+alphabet[20]+alphabet[26]+alphabet[11]+alphabet[8] \
    +alphabet[10]+alphabet[4]+alphabet[11]+alphabet[8]+alphabet[14]+alphabet[13]
print(index1)

index2 = alphabet[7]+alphabet[0]+alphabet[2]+alphabet[10]+alphabet[26] \
    +alphabet[24]+alphabet[14]+alphabet[20]+alphabet[17]+alphabet[26] \
    +alphabet[11]+alphabet[8]+alphabet[5]+alphabet[4]
print(index2)

index3 = alphabet[12]+alphabet[24]+alphabet[26] \
    +alphabet[13]+alphabet[0]+alphabet[12]+alphabet[4]+alphabet[26] \
    +alphabet[8]+alphabet[18]
print(index3,"이나현")

index4 = number[2]+number[0]+number[0]+number[3] \
    +number[0]+number[3]+number[0]+number[7]
print("제 생일은", index4, "입니다.")

index5 = number[0]+number[1]+number[0]+number[10] \
    +number[8]+number[9]+number[1]+number[0]+number[10] \
    +number[1]+number[4]+number[4]+number[1]
print("제 전화번호는", index5, "입니다.")

index6 = number[2]+number[0]+number[2]+number[2] \
    +number[1]+number[4]+number[0]+number[3]+number[6]
print("제 학번은", index6, "입니다.")