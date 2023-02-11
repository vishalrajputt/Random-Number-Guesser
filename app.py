import random


n=random.randint(1,10)
j=random.randint(10,50)

print("You have to guess a number between ",n," and ",j)

k=random.randint(n,j)

p=1

o=int(input("Guess the number-> "))

while True:
    if o==k:
        print("Your Answer-> ",o,"Right answer is -> ",k,"Congratulations")
        print("Total number of try:->",p)
        break
    else:
        p=p+1
        print("Your Guess is wrong ,Try again")
        o=int(input("Guess the number-> ")) 