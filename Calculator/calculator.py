print("Calculato Python")
print("----------------")

print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Pembagian")
print("4. Perkalian")
print("----------------")

#Logic
def penjumlahan(x,y):
    return x + y

def pengurangan(x,y):
    return x - y

def perkalian(x,y):
    return x * y

def pembagian(x,y):
    return x / y

tipe = input("Silahkan Masukan nomer yang kalian inginkan: ")

if tipe in('1', '2', '3', '4'):
    angka1 = float(input("Angka Pertama: "))
    angka2 = float(input("Angka Kedua: "))
    print("----------------")
    if tipe == '1':
        print("Jawabannya adalah: ", penjumlahan(angka1, angka2))
    if tipe == '2':
        print("Jawabannya adalah: ", pengurangan(angka1, angka2))
    if tipe == '3':
        print("Jawabannya adalah: ", perkalian(angka1, angka2))
    if tipe == '4':
        print("Jawabannya adalah: ", pembagian(angka1, angka2))
    print("----------------")