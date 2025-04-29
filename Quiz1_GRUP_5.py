# Grup 5

# 210201140
# Ahmad Alhomsi

# 210201126 
# Ebrar Mustafa AÇIKYOL

# 210201120
# Cem Korkmaz



from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import random


def generate_s_box(dizi):
    """
    Generate a substitution box (S-Box) using AES encryption.
    The S-Box is created by encrypting all possible byte values (0-255).
    """
    yeniD = []
    
    for i in dizi:
        random_sayi=random.randint(0,15)
        yeniD.append(dizi[random_sayi])

    return yeniD

if __name__ == "__main__":


    dizi =[]

    for i in range(0,16):
#        print(random.randint(0,15))
        dizi.append((random.randint(0,15)))

    print(dizi)
    
    s_box = generate_s_box(dizi)
    print("Generated S-Box:")
    print(s_box)
    
    dizi2 = []
    for i in range(0,16):
        print(random.randint(0,15))
        dizi2.append((random.randint(0,15)))

    print("2 DIZILER")
    print(dizi)
    print(dizi2)
    
    for i in range(0,16):
        dizi[i] = bin(dizi[i])[2:]
        if(len(dizi[i]) == 1):
            dizi[i] = "000" + dizi[i] 
        elif(len(dizi[i]) == 2):
            dizi[i] = "00" + dizi[i] 
        elif(len(dizi[i]) == 3):
            dizi[i] = "0" + dizi[i] 

    
    
    for i in range(0,16):
        dizi2[i] = bin(dizi2[i])[2:]
        if(len(dizi2[i]) == 1):
            dizi2[i] = "000" + dizi2[i] 
        elif(len(dizi2[i]) == 2):
            dizi2[i] = "00" + dizi2[i] 
        elif(len(dizi2[i]) == 3):
            dizi2[i] = "0" + dizi2[i] 
        
    print("Binary 4 Bit Output")    
    print(dizi)
    print(dizi2)
    
    yeniD = []
    yeniD2 =[]

    c3 = 0
    for i in range(0,16):
        counter =0
        counter2 =0
        for j in range(0,4):
            if(dizi[i][j] == "1"):
                counter +=1
                
        for j in range(0,4):
            if(dizi2[i][j] == "1"):
                counter2 +=1
        
        print("Counter:", counter)   
        print("Counter2:", counter2)   

        if((counter % 2) == 0 and (counter2 % 2) == 0): # Cift sayi
            yeniD.append(int(dizi[i], 2) ^ int(dizi2[i], 2))
            
            print("YENI DIZI:")
            print(yeniD)            
            yeniD[c3] = bin(yeniD[c3])[2:]
            if(len(yeniD[c3]) == 1):
                yeniD[c3] = "000" + yeniD[c3] 
            elif(len(yeniD[c3]) == 2):
                yeniD[c3] = "00" + yeniD[c3] 
            elif(len(yeniD[c3]) == 3):
                yeniD[c3] = "0" + yeniD[c3] 
                
          
            
            print("XXX", yeniD)
            result = 0
            for k in range(0,4):
                result = int(yeniD[c3][0],2) ^ int(yeniD[c3][1],2)
                result = result ^ int(yeniD[c3][2],2)
                result = result ^ int(yeniD[c3][3],2)
            print("RESULT", result)
            yeniD2.append(result)

            c3 += 1
            
        else:
            result2 = 0
            result3 = 0
            for k in range(0,4):
                result2 = int(dizi[i][0],2) ^ int(dizi[i][1],2)
                result2 = result2 ^ int(dizi[i][2],2)
                result2 = result2 ^ int(dizi[i][3],2)
                
            for k in range(0,4):
                result3 = int(dizi2[i][0],2) ^ int(dizi2[i][1],2)
                result3 = result3 ^ int(dizi2[i][2],2)
                result3 = result3 ^ int(dizi2[i][3],2)
            
            result4= result2 ^ result3
            print("RESULT4:", result4)
            yeniD2.append(result4)
            
            
    print(yeniD2)
    print('Enter your number:')
    x = input()
        
    print(x)
    P1=[]
    P2=[]
    P3=[]
    P4=[]
    c0 = 0
    for i in range(0,16):
        if(c0 < 4):
            P1.append(yeniD2[i])
            c0+=1
        elif(c0 < 8):
            P2.append(yeniD2[i])
            c0+=1
        elif(c0 < 12):
            P3.append(yeniD2[i])
            c0+=1
        elif(c0 < 16):
            P4.append(yeniD2[i])
            c0+=1
    
    print(P1)
    print(P2)
    print(P3)
    print(P4)
    
    # for i in range(0,4):
        
        
        
    # for i in x:
    #     if(i )
            
            