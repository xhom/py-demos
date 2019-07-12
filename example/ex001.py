# coding=UTF-8

# 001.题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
print '-------------------------------------001'
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (j!=k) and (k!=i):
                print i*100+j*10+k

print '-------------------------------------002'
'''
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
"""
0<I<=10,   R0=10%, S0 = I*R0 = 0 + f0(I)
10<I<=20,  R1=7.5%, S1 = (10*R0) + (I-10)*R1 = f0(10) + (I-10)*R1 = f1(I)
20<I<=40,  R2=5%, S2 = (10*R0) + (20-10)*R1 + (I-20)*R2 = f(20) + (I-20)*R2 = f2(I)
40<i<=60,  R3=3%, S3 = (10*R0) + (20-10)*R1 + (40-20)*R2 + (I-40)*R3 = f2(40)+ (I-40)*R3 = f3(I)
60<I<=100, R4=1.5%, S4 = (10*R0) + (20-10)*R1 + (40-20)*R2 + (60-40)*R3 + (I-60)*R4 = f3(60)+ (I-60)*R4 = f4(I)
100<I,     R5=1%, S5= (10*R0) + (20-10)*R1 + (40-20)*R2 + (60-40)*R3 + (100-60)*R4 + (I-100)*R5 = f4(100) + (I-100)*R5
"""

rates = [
    {'P': 1000000, "R": 0.01 },
    {'P': 600000,  "R": 0.015},
    {'P': 400000,  "R": 0.03 },
    {'P': 200000,  "R": 0.05 },
    {'P': 100000,  "R": 0.075},
    {'P': 0,       "R": 0.1  },
]

def reward(I):
    if I==0: return 0
    for item in rates:
        P,R = item['P'],item["R"]
        if I>P: return (I-P)*R + reward(P)

print reward(120000)

print '-------------------------------------003'
# 找100-999的水仙花数
import math

for i in range(100,1000):
    a,b,c = i//100, i%100//10, i%100%10
    if i == math.pow(a,3)+math.pow(b,3)+math.pow(c,3):
        print i

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
print '-------------------------------------004'
height = 100
jump = 0
sum = 0
for i in range(0,10):
    sum += height+jump
    jump = height/2.0
    print '第',i+1,'次反弹高度：', jump,'总距离：',sum
    height = jump

print '-------------------------------------005'
a,b = 2.0,1.0
sum = 0

for i in range(0,20):
    sum += a/b
    print '第',i+1,'项：', a,'/', b , 'sum=', sum
    _b = b; b = a; a = a+_b

print '-------------------------------------006'

def print_reverse(arr):
    size = len(arr)
    if size==0:
        return
    print arr[size-1]
    print_reverse(arr[0:size-1])

print_reverse([1,2,3,4,5,6])

print '-------------------------------------007'
# 回文串检测
def check_hw(str):
    start,end = 0,len(str)-1
    while start<end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True

print check_hw("123454321")
print check_hw("123321")
print check_hw("123431")