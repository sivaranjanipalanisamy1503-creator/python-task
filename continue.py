'''#continue
#1,print number from 1 to 10 but skip 5
n=11
for h in range (1,11,1):
    if h==5:
        continue
    print(h)
#2,print only odd num
n=20
for h in range (1,20,1):
    if h%2==0:
        continue
    print(h)
#3,find the sum of num 1 to 50 excluding multi of 3
n=0
for i in range (1,50):
    if i%3==0:
        continue
    else:
        n=n+i
        print(n)
#4,find sum of a list while skipping negative num
for i in range (-10,5):
    if i<=0:
        continue
    print(i)
#5,count the consonants in a string , skipping vowels.
name=('sivaranjani')
vo=('a','e','i','o','u')
for i in name:
    if i in  vo:
        continue
    print(i)
#6,print the charc of string while skipping space.
name=('siva ranjani')
s=(" ")
for i in name:
    if i in s:
        continue
    print(i,end='')
#7,print num from 1to30 that are divi by neither 2 nor 3
n=30
for i in range(1,30):
    if i%2==0 or i%3==0:
        continue
    print(i)
#8,print the items of list, skipping none values.
l=(2,5,7,3,None,6,9,None)
n=(None)
for i in l:
    if i in n:
        continue
    print(i)
#9,find the product of non-zero elements of list
l=(20)
for i in range(1,21):
    if i%10!=0 :
        continue
    print(i)
#10,print letters of a word excluding the letter A
w=('siva ranjani')
ex=('a')
for i in w:
    if i in ex:
        continue
    print(i)'''
#12,print num 1to20 skipping perfect square
s=1
p=1
for i in range(1,21):
    s=i**0.5
    p=(s**2)
    if p==i:
        print(p,s)



    

