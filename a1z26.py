import os                                                           
def A1Z26_encrypt(cistring):                                       
    string=" "                                                      
    cistring = cistring.lower()                                   
    cistring = " ".join(cistring.split())                           
    for x in range(0,len(cistring)):                                
        char=ord(cistring[x])-96
        if char > 0 and char <=26 :string  +=str(char) +  "  "      
    return(string)                                               

def A1Z26_decrypt(cistring):
    string=" "
    data = cistring.split()
    for char in data:
        char = chr(int(char) + 96)
        string += char
    return(string)

def A1Z26():
    os.system('cls')
    print("----------------------------------------------------------------------------------------------------------")
    cistring=input("ENTER A STRING TO ENCRYPT:")
    print(A1Z26_encrypt(cistring))
    cistring=input("ENTER A STRING TO DECODE :")
    print(A1Z26_decrypt(cistring))
A1Z26()

