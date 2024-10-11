# BAI TAP 1.1 
import math
# CAU A
def sont(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# CAU B
def sohc(n):
    for i in range (1 , n):
        sum = sum + i
        if sum == n:
            return True
    return False
# CAU C
def sodoixung(n):
    sum = 0
    while n != 0:
        sum = sum*10 + n % 10
        n/10
        if sum == n:
            return  True
    return False
# CAU D
def sodn(n):
    sum = 0
    while n != 0:
        sum = sum*10 + n % 10
        n/10
    return sum
# CAU E
def soA(n):
    sum = 0
    for i in range (1 , n):
        sum = sum + math.pow(i, 3)
        if sum == n:
            return True
    return False
# CAU F
def M(n):
    if(sont(n)):
        for i in range (2, n/2):
            sum = math.pow(2, i) - 1
        if sum == n:
            return True
    return False
# CAU H
def tbNhan(n):
    d = 0, sum = 0
    for n in range (0, n):
        m = int(input("Nhap so: "))
        d+=1
        sum+=m
    return math.pow(sum, 1/d)

n = int(input("Nhap so n:"))
if(sont(n)):
    print("So nguyen to") 
else:
    print("Khong la nguyen to")
if(sohc(n)):
    print("So hoan chinh") 
else:
    print("Khong la so hoan chinh")
if(sodoixung(n)):
    print("So doi xung") 
else:
    print("Khong la so doi xung")
sodn(n)
if(soA(n)):
    print("So Armstrong") 
else:
    print("Khong la so Armstrong")
if(M(n)):
    print("So Mersenne") 
else:
    print("Khong la so Mersenne")
tbNhan(n)