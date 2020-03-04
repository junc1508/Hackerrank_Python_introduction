#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#Mat size must be X. ( is an odd natural number, and  is  times .)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.
#Size: 7 x 21 
#    ---------.|.---------
#    ------.|..|..|.------
#    ---.|..|..|..|..|.---
#    -------WELCOME-------
#    ---.|..|..|..|..|.---
#    ------.|..|..|.------
#    ---------.|.---------




n,m = map(int,input().split())
n = int(list[0])
m = int(list[1])
for i in range(int((n-1)/2)):
    print(('.|.'*(2*i+1)).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(int((n-1)/2),0,-1):
    print(('.|.'*(2*i-1)).center(m,'-'))
