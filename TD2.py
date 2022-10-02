from sha256 import * 
import secrets as s
import hashlib
import sys


#Functions shamefully stolen to professor, converts byte into binary value
def padd_binary(bin_str: str, size: int) -> str:
    """
    Pads a binary string with zeros to the left
    :param bin_str: binary string to pad
    :param size: size of the padded string
    :return: padded binary string
    """
    for _ in range(size - len(bin_str)):
        bin_str = '0' + bin_str
    return bin_str

def byte_to_binary(b: bytes, size: int) -> str:
    """
    Converts a byte to a binary string
    :param byte: byte to convert
    :param size: size of the binary string
    :return: binary string
    """
    order = -1 if sys.byteorder == 'little' else 1
    bin_n = bin(int.from_bytes(b, byteorder='big'))[2:]
    return padd_binary(bin_n, size)


#Accepts binary entropy entry as parameter, enering no parameters generates a random crypo safe entropy
def Generate_Seed(entropy=None):
    
#Generate safe random integer as entropy
    if entropy==None:        
        entropy= s.randbits(128)
        print("entropy : ",entropy)
        entropy=bin(entropy)[2:].zfill(128)
    else:
        entropy=bin(entropy)[2:].zfill(128)
    #print(len(entropy))
    #print("binary entropy : ",entropy)
    
        

#Checksum moment :

#Generate Hash of entropy

    hash=generate_hash(str(entropy))   #Hashs the entropy
    #print(hash)


    checksum=byte_to_binary(hash, 256)[:4]  #Converts it to bytes and keeps the 4 first
    #print("checksum : ",checksum)

    final_entropy= str(entropy) + str(checksum)   #adds it to entropy to have a 132 bits final entropy
    #print(final_entropy)

    #creates an array and keeps every 11 bits from the final hash
    segments=[]
    for i in range(12):
        segments.append(final_entropy[11*i:11*(i+1)])

    #print(segments)

#i found online a text file with BIP39 words sorted by int value (0 is "abandon" etc...)

    file=open('BIP39words.txt','r')
    bipw=file.readlines()

    #print(bipw)

    #Converts the binary segments into int then the int into to corresponding word
    bwl=[]
    for k in segments:    
        k=bipw[int(str(k),2)]
        bwl.append(k)    
    
    #print(bwl)
    print("\n")
    for l in bwl:
        print(l)
    
def Import_Seed(seed:str):
    #Checksum not implemented yet so this function isn't perfectly working  :'-(
    #Some bugs are still remaining
    
    bin_res=[]
    
    file=open('BIP39words.txt','r')
    bipw=file.readlines()
    bipw[-1]+="\n"
    #print(bipw)
    
    mnemo=seed.split()
    #print(mnemo)
    
    #For each mnemo word, checks its presence in the Bip39 Mnemo words and append its decimal value in a list
    #If a word is incorrect, returns an error.
    for i in mnemo:
        resp=True
        for j in range(len(bipw)):            
            if bipw[j]==i+"\n":
                bin_res.append(j)
                resp=False                
        if resp:
            print("Word",i,"is incorrect.")
            bin_res=None
            break
        
    
    
    #print(bin_res)
    
    #creates a list from the mnemo words binary equivalent
    bin_fin=[]
    for k in range(len(bin_res)):
        bin_fin.append(bin(bin_res[k])[2:].zfill(11))
    
    
    #print(bin_fin)
    
    "creates a string to return the complete entropy"
    entropy=""
    for f in bin_fin:
        entropy+=f
    
    entropy=entropy[:-5]
    print("Binary entropy is : ",entropy)
    print("Integer entropy is : ",int(entropy,2))
    
    
    
    

def Extract_MasterKey(seed:str):
    print(hashlib.sha512(seed))
    
    


#Generate_Seed(107539121524694991868515036671812879545)
#Import_Seed("peace innocent alcohol clip invest squeeze flock grass buzz across girl tortoise")

#Generate_Seed(130907837269173211963531510614441289891)

#Extract_MasterKey("peace innocent alcohol clip invest squeeze flock grass buzz across girl tortoise")


print("Welcome to Gabriels Saliba's TD2 of blockchain programming")
print("To generate a Seed, enter 1 \n To find entropy from a defined Seed, enter 2")
inp = input()
if inp == "1":
    print("To generate the words from a defined integer seed, press 1\n to Generate a crypto-safe integer seed press 2")
    inp2=input()
    if inp2=="1":
        print("enter your integer seed")
        Generate_Seed(int(input()))
    else:
        Generate_Seed()
else:
    print("enter your seed words separated by a space, all in lower case size")
    Import_Seed(input())
