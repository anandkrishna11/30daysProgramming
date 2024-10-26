'''author:Anand krishna M A
Date:26-10-2024
description:program that repeatedly asks from users some numbers until string 'done' is typed.the program should return the sum of numbers! '''

total=0
num=input("Enter the number or done:")
while num!='done':
    num=int(num)
    total+=num
    num=input("Enter the number or done")
print('the sum of numbers is',total)
