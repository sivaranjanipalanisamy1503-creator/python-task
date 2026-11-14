'''#conver sec into hour
sec=7500
hour=sec//3600
print(hour)
#covert hour into minu
hour=3
minu=hour*60
print(minu)
#convert minu into sec
minu=180
sec=minu*60
print(sec)
#sep last digi and remaining
num=386
last=num%10
print(last)
rem=num//10
print(rem)
#check a num divisible by 3 and 5 using logical ope
num=22
if num%3==0 and num%5==0 :
    print('the num are divisible by 3 and 5')
else :
    print('the num are not divisible by 3 and 5 ')
#check num is power of 2 using bitwise ope
num=55
print((num>0)and(num&(num-1)==0))
# numer is odd using bitwise using and 
num=44
print(num&1==1)'''
#divid by 8 using shift
num=68
print (num<<3)
print (num>>3)




