'''BAI TAP 1.1'''
import math
import numpy as np
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
delta = b*b - 4*a*c
if a == 0:
    print("Khong phai phuong trinh bac hai")
else: 
    if delta > 0:
        x1 = int((-b -math.sqrt(delta)) / 2*a)
        x2 = int((-b +math.sqrt(delta)) / 2*a)
        print("Phuong trinh co 2 nghiem phan biet: ")
        print("x1: "+ str(x1))
        print("x2: "+ str(x2))
    if delta == 0:
        x = -b / (2*a)
        print("Phuong trinh co hai nghiem kep: +-" + str(x))
    if delta < 0:
        print("Phuong trinh vo nghiem")
'''BAI TAP 1.2'''
def giai_he_pt_gauss(A, b):
  n = len(A)
  if len(b) != n:
    raise ValueError("Kích thước ma trận và vector không tương thích")
  augmented = np.concatenate((A, b[:, np.newaxis]), axis=1)
  for i in range(n):
    max_row = np.argmax(np.abs(augmented[i:, i])) + i
    augmented[[i, max_row]] = augmented[[max_row, i]]
    augmented[i] /= augmented[i, i]
    for j in range(i+1, n):
    augmented[j] -= augmented[j, i] * augmented[i]
  x = np.zeros(n)
  for i in range(n-1, -1, -1):
    x[i] = augmented[i, -1] - np.dot(augmented[i, :n-1], x[i+1:])
  return x
'''BAI TAP 1.3'''
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
max = max(a,b,c)
min = min(a,b,c)
mid = (a+b+c) - max - min
print(str(min) + str(mid) + str(max))
'''BAI TAP 1.4'''
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
d = int(input("Nhap d: "))
e = int(input("Nhap e: "))
f = int(input("Nhap f: "))
arr = [a, b, c, d, e, f]
so0 = soam = soduong = 0
for i in range(0, len(arr)):
    if arr[i] < 0:
        soam+=1
    if arr[i] == 0:
        so0+=1    
    if arr[i] > 0:
        soduong+=1
print("Co " + str(soam) + " so am")
print("Co " + str(so0) + " so 0")
print("Co " + str(soduong) + " so duong")
'''BAI TAP 1.5'''
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
d = int(input("Nhap d: "))
arr1 =[a, b, c, d]
'''CAU A'''
max1 = a
if b > max1:
    max1 = b
if c > max1:
    max1 = c
if d > max1:
    max1 = d
min1 = a
if b < min1:
    min1 = b
if c < min1:
    min1 = c
if d < min1:
    min1 = d
print(max1)
print(min1)
'''CAU B'''
print(sorted(arr1))
'''CAU C'''
dem = 0
for i in range(0, len(arr1)):
    for j in range(0, len(arr1)):
        if arr1[i] != arr1[j]:
            dem+=1
print(dem)
'''CAU D'''
min1 = a - b
if b - c < min1:
    min1 = b - c
if c - d < min1:
    min1 = c - d
if b - c < min1:
    min1 = b - c
if b - a < min1:
    min1 = b - a
if d - c < min1:
    min1 = d - c
if c - b < min1:
    min1 = c - b
print("Khoang cach gan nhat la: " + str(min1));
'''BAI TAP 1.6'''
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
if a + b > c and a + c > b and c + b > a:
    print("La 3 canh cua tam giac")
    if a == b == c:
        print("La tam giac deu")
    if a == b or a == c or c == b:
        print("La tam giac can")
    if a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
        print("La tam giac vuong")
    else:
        print("La tam giac thuong")
else: 
    print("Khong phai 3 canh cua tam giac")


