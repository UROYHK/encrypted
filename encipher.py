#The symbol table holds all characters and their corresponding encryption values.You can add custom values if needed just make sure they don't already exist in the table.
symbol_map={"a":".","b":":","c":":.","d":"::","e":"|","f":"|.","g":"|:","h":"|:.","i":"|::","j":"||","k":"||.","l":"||:","m":"||:.","n":"||::","o":"|||","p":"|||.","q":"|||:","r":"|||:.","s":"|||::","t":"||||","u":"||||.","v":"||||:","w":"||||:.","x":"||||::","y":"|||||","z":"|||||."," ":"~","?":"qushion mark"}

reversed_map={v: k for k,v in symbol_map.items()}  #this line is used to revers the symbol map while doing the decryption function.

#the decryption function.
def decripter(text):
     decripter_text=""                                    # Creates a string  where the decrypted values are added ione after an other unit the hole input is scaned 
     symbols = text.strip().split()                       # hear we are appling strip and split function to the text! what is the text its the input given by the user and assign this editied text to a varible called symbols  . strip()-> removes white spaces , splits()-> splits the chars into individual words for decription process it needs to detecct each individual chars  
     for symbol in symbols:                               # hear we are now keeping the newly assigned varible symbols in a for loop until every char in the input is scaned 
        if symbol in reversed_map:                        #if symbol is present in symbol table it adds it to the decripter_text
               decripter_text += reversed_map[symbol]
        else:                                             # if symbol is not present it addas a (?) to represent the unknow value 
             decripter_text += "?"
     return decripter_text




# the encryption function 
def encripter(text):
    encripter_text=""                                     # this creates a string to stores the encripted text
    for char in text.lower():                             # turns any char from input to lower case   
          if char in symbol_map:                          # checks if the input is present in the symbol map
               encripter_text += symbol_map[char] + " "   #  here i added  ("") because this adds space after each encripted char which helps in analysing the charactes better 
          else:                                           # else it relaces the unidentified char with a question mark
               encripter_text += '?'
    return encripter_text.strip()                         # returns the encripted text




# this the main code that runs the file 
if __name__=="__main__":                                 #this line is help full if you are running this function from this code in an othere code this line will make sure that the function only runs when called  not always
 while True:                                             # while true was added to make the program run more than once
  choice = input("do you wish to encript or decrypt type(ec /or/ dc) or typ (bye) to exit ")

  if choice == 'ec':                                      # this choice calls the encryption function 
     message = input("please enter your message :")
     result = encripter(message)                       
     print("Encripted message:", result)  

  elif choice == 'dc':                                    # this choice calls the decryption function.
      message = input("please enter your message :")
      original_message = decripter(message)
      print("Decrypted message:", original_message ) 

  elif choice == 'bye':                                   # this choice ends the program 
       print ("ok bye")
       break   

  else :                                                  #this choice  helps to show you what are the possible choices are 
      print("this is not a valid option try (ec) to encript or (dc) to dcript  or say(type) bye to exit ")   
  
    
   
   
    
    
