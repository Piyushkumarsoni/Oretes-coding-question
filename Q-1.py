def convertTime(s):
    # Get hours values
    h1 = ord(s[1]) - ord('0')
    h2 = ord(s[0]) - ord('0')
    hh = (h2 * 10 + h1 % 10)
  
    # If time is in "AM" then 
    if (s[9] == 'A'):
        if (hh == 12):
            print('00', end = '')
             
            for i in range(2, 8):
                print(s[i], end = '')
 
        else:
            for i in range(0, 8):
                print(s[i], end = '')
  
    # If time is in "PM" then 
    else:
        if (hh == 12):
            print("12", end = '')
             
            for i in range(2, 8):
                print(s[i], end = '')
         
        else:
            hh = hh + 12
            print(hh, end = '')
             
            for i in range(2, 8):
                print(s[i], end = '')
             
# Main function of program       
if __name__=="__main__":
 
   s = input()
    
   convertTime(s)