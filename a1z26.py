import os                                                           #only used to clear command prompt
def A1Z26_encrypt(cistring):                                        #encrypt string by converting each letter to a number
    string=" "                                                      #place holder variable
    cistring = cistring.lower()                                     # Format to lower case
    cistring = " ".join(cistring.split())                           #remove spaces from string
    for x in range(0,len(cistring)):                                #loop through each character of a string
        char=ord(cistring[x])-96
        if char > 0 and char <=26 :string  +=str(char) +  "  "      #store value in string variable
    return(string)                                                  #return cipher string

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

