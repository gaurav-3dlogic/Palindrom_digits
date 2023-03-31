num = int(input("Enter a number: "))
temp = num 
rev = 0


while(num > 0):
    rev = (rev * 10) + num % 10
    num = num // 10
    
if(temp == rev):
    print("Number is palindrom")
else:
    print("Number is not palindrome")
    
    
# Time Complexity: O(n) 
# Space Complexity: O(1)