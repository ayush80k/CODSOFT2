import random as rd
char_l = []
print("Welcome to Password Generator.\n")
length = int(input("Enter the desired password length(positive): "))

while True:
    comp = int(input("\nEnter the desired complexity: \n1 for Basic: Letters only\n2 for Moderate: Letters and Numbers\n3 for Complex: Letters,Numbers and Symbols\n"))
    password = ''
    if comp == 1:
        for ascii in list(range(65,91)) + list(range(97,123)):
            val = chr(ascii)
            char_l.append(val)

        flag = length
        while flag>0:
            password += rd.choice(char_l)
            flag -= 1
        break

    elif comp == 2:
        for ascii in list(range(48,58)) + list(range(65,91)) + list(range(97,123)):
            val = chr(ascii)
            char_l.append(val)

        flag = length
        while flag>0:
            password += rd.choice(char_l)
            flag -= 1
        break

    elif comp == 3:
        for ascii in range(33,127):
            val = chr(ascii)
            char_l.append(val)

        flag = length
        while flag>0:
            password += rd.choice(char_l)
            flag -= 1
        break

    else:
        print("\nEnter a valid choice\n")

print("\nYour generated password:  ",password)
