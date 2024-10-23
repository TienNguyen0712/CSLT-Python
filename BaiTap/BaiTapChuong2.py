# BAI TAP 2.1 
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
# BAI TAP 2.2 
# CAU A
n = int(input())
sum = 0, tich = 1
for i in range(1, n + 1):
    tich*=i
    sum+=tich
print(sum)
# CAU B
n = int(input("Nhap so n: "))
tich = 1, sum = 0
for i in range(1, n + 1):
    tich*=(n-i)
    sum+=tich
print(sum)
# CAU C
n = int(input("Nhap so n: "))
x = int(input("Nhap so x: "))
sum = 0
for i in range(1, n + 1):
    sum+=i
print(math.pow(x, n)/sum)
# CAU D
n = int(input("Nhap so n: "))
x = int(input("Nhap so x: "))
sum = 0
for i in range(1, n + 1):
    sum+=(i/i)
print(math.pow(x, n)/sum)
# CAU e
# cau f
# BAI TAP 2.3
sum = 0, m = 5
for i in range(1, 100):
    sum+=i;
    if sum < m:
        d = m - sum
print(d)
# BAI TAP 2.4
n = int(input("Nhap vao so n: "))
for z in range(1, n+1):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
           if (x < y) and (y < z) and (int(z) == int(x**2 + y**2)):
               print(str(x) + " " + str(y) + " " + str(z))
# BAI TAP 2.5
n = int(input("Nhap ngay: "))
t = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
# CAU A
if n <= 31 and t <= 12:
    print("Ngay va thang hop le")
# CAU B
ngaytieptheo = n + 1
if(ngaytieptheo > 31):
    ngaytieptheo = 1
    t+=1
    if(t > 12):
        t = 1
        nam+=1
print("Ngay tiep theo la: " + str(ngaytieptheo) + "/" + str(t) + "/" + str(nam))
# CAU C
ngaytruocdo = n - 1
if(ngaytruocdo <= 0):
    ngaytruocdo = 1
    t-=1
    if(t <= 0):
        t = 1
        nam-=1
print("Ngay truoc do la: " + str(ngaytruocdo) + "/" + str(t) + "/" + str(nam))
# BAI TAP 2.6
# CAU A
n = int(input("Nhap ngay: "))
t = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0
for i in range(0, t-1):
    sum+=arr[i]
if(nam % 400 == 0 or nam % 100 != 0 and nam % 4 == 0):
    print(str(n) + "/" + str(t) + "/" + str(nam) + "la ngay thu " + str(sum+1+n) + " trong nam")
else:
    print(str(n) + "/" + str(t) + "/" + str(nam) + "la ngay thu " + str(sum+n) + " trong nam")
# CAU B 
n = int(input("Nhap ngay: "))
t = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
print("Ngay bat dau nghi huu: " + str(n) + "/" + str(t) + "/" +str(nam + 55))
# CAU C
n = int(input("Nhap ngay: "))
t = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
print("Ngay bat dau nghi huu: " + str(n) + "/" + str(t) + "/" +str(nam + 49))
# BAI TAP 2.7
# CAU A
tienvay = int(input("Nhap so tien vay: "))
thang = int(input("Nhap so thang vay: "))
lai = int(input("Nhap lai suat vay: "))
tong = tienvay + (tienvay * (lai/100/12) * thang)
print("So tien phai tra: " + str(tong))
# CAU B 
tienvay = int(input("Nhap so tien vay: "))
thang = int(input("Nhap so thang vay: "))
lai = int(input("Nhap lai suat vay: "))
laithang = lai/100/12
tra_goc_thang = tienvay / thang
tong_so_tien_tra = 0

for thang in range(1, thang + 1):
    laivay = tienvay * laithang
    tong_tra_thang = tra_goc_thang + laivay
    tong_so_tien_tra += tong_tra_thang
    tienvay -= tra_goc_thang
print("Tien phai tra " + str(tong_so_tien_tra))
