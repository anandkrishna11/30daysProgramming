'''author:Anand Krishna M A
date:7-11-2024
description: write a program using function that takes amount-in-dollars and rupees ; convert dollar to rupee and rupee to doller as the users choice
'''

def dol_2_inr(x):
    r=x*82
    return r
def inr_2_dol(x):
    d=x/82
    return d

print("do you want to (1)covert dollar into rs OR (2)convert rs to dollar")
choice=int(input("Enter your choice:"))
print("Current value: 1$ = 82rs")
if choice==1:
    dollar=float(input("Enter dollars:"))
    print(f"the dollar you entered in inr = {dol_2_inr(dollar)}")
elif choice==2:
    rupee=float(input("Enter rupees:"))
    print(f"the rupees you entered in dollar = {inr_2_dol(rupee)}")
else:
    print("Enter a valid choice!")


    



