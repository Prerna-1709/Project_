# Program to print double of number after deleting second last digit. input 2637 output 534
a=int(input("Enter a number"))
b= a//100
c=a%10
d=str(b)+str(c)
e=int(d)
print(e*2)