import math as m
#Vidu1
a = int(input("Nhap chieu dai HCN: "))
b = int(input("Nhap chieu rong HCN: "))
print("Chu vi la: " + str((a+b)*2))
print("Chu vi la: " + str((a*b)))
print("Duong cheo: "+ str(m.sqrt((a*a + b*b))))
#Vidu2
c = int(input("Nhap so co ba chu so: "))
print("Tong la: " + str(c/100 + c%100/10 + c%10))
#Vidu3
a1 = int(input("Toa do diem xA: "))
a2 = int(input("Toa do diem yA: "))
b1 = int(input("Toa do diem xB: "))
b2 = int(input("Toa do diem yB: "))
c1 = int(input("Toa do diem xC: "))
c2 = int(input("Toa do diem yC: "))
#Tinh cac canh cua tam giac 
ab = float(m.sqrt((b1-a1)*(b1-a1) + (b2 - a2)*(b2-a2)))
ac = float(m.sqrt((c1-a1)*(c1-a1) + (c2 - a2)*(c2-a2)))
bc = float(m.sqrt((c1-b1)*(c1-b1) + (c2 - b2)*(c2-b2)))
NuaChuVi = (ab + ac + bc)/2
DienTich = float(m.sqrt(NuaChuVi*(NuaChuVi-ab)*(NuaChuVi-ac)*(NuaChuVi-bc)))
BanKinh = float((ab*ac*bc)/45)
print("Trong tam cua tam giac ABC: " + str((a1 + b1 + c1)/3) + " " + str((a2 + b2 + c2)/3))
print("\nDien tich duong tron noi tiep tam giac ABC: " + str(BanKinh*BanKinh*m.pi))
print("\nDien tich duong tron ngoai tiep tam giac ABC: " + str(((BanKinh/NuaChuVi)*(BanKinh/NuaChuVi))*m.pi))
#Vidu4 
x = int(input("Nhap so a: "))
y = int(input("Nhap so b: "))
if x != 0:
    print("Phuong trinh co nghiem: " + str(round(-y/x, 2)))
elif x == y:
    print("Phuong trinh co vo so nghiem!")
else: 
    print("Phuong trinh vo nghiem!")
#Vidu5
canh = int(input("Nhap canh hinh vuong: "))
print("Chu vi cua hinh vuong: "+ str(canh*4))
print("Dien tich cua hinh vuong: " + str(canh*canh))
print("Duong cheo cua hinh vuong: " + str (round(canh*m.sqrt(2), 2)))