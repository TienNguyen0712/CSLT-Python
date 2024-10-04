import math 
#Vidu2
thang = int(input("Nhap thang : "))
nam = int(input("Nhap nam : "))
match thang:
    case 1:
        ngay = 31
    case 3:
        ngay = 31
    case 4:
        ngay = 30
    case 5:
        ngay = 31
    case 6:
        ngay = 30
    case 7:
        ngay = 31
    case 8:
        ngay = 31
    case 9:
        ngay = 30
    case 10:
        ngay = 31
    case 11:
        ngay = 30
    case 12:
        ngay = 31
    case 2:
        if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
            ngay = 29 
        else:
            ngay = 28
print(ngay)
#Vidu3
i = int(input("Nhap so i: "))
dem = 0
if i == 1 :print(dem)
for j in range(1, i):
    if i % j == 0:
        dem+=1
print("So uoc duong la: " + str(dem))
#Vidu4
sum = 0
i = 1
n = int(input("Nhap so n: "))
while(i < n):
    d = i % 10
    sum = sum + d
    i = i/10
print(sum)
#Q7
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
r = a % b
while r != 0:
    a = b
    b = r
    r = a%b
ucln = b
bcnn = float(a*b/ucln)
print(ucln)
print(bcnn)
#Q8
tu1 = int(input("Nhap tu1: "))
tu2 = int(input("Nhap tu2: "))
mau1 = int(input("Nhap mau1: "))
mau2 = int(input("Nhap mau2: "))
tich = mau1*mau2
hieu = tu1*mau2 - tu2*mau1
tong = tu1*mau2 + tu2*mau1
r = tich % hieu
while r != 0:
    tich = hieu
    b = r
    r = tich%hieu
ucln = hieu
r = tich % tong
while r != 0:
    tich = tong
    tong = r
    r = tich%tong
ucln = tong
print(str(tong/ucln) + "/" + str(tich/ucln))
print(str(hieu/ucln) + "/" + str(tich/ucln))
#Vidu5
sum = 0
while b != 0:
    b = int(input("Nhap so: "))
    sum = sum + b
print(sum)
#Vidu6
a  = int(input("Nhap a: "))
b  = int(input("Nhap b: "))
c  = int(input("Nhap c: "))
if a > 0 and  b > 0 and  c > 0:
    if a + b > c and a + c > b and c + b > a:
        chuvi = a + b + c
        dientich =  float(math.sqrt((a+b+c)/2*((a+b+c)/2-a))*((a+b+c)/2-b)*((a+b+c)/2-c))
print(chuvi)
print(dientich)