import random
ran=random.choice (['r','s','p'])
p1=input("enter your choice : ")
p2 = print('computer choice', ran)
if((p1=='r' and p2=='s') or (p1=='p' and p2=='r') or (p1=='s' and p2=='p')):
    print("you won")
elif(p1==p2):
    print("tie between p1 and p2")
else:
   print("you lost")