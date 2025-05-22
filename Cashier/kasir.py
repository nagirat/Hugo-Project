menu = {
    "Fried Chicken": 15000,
    "Burger Queen": 25000,
    "French Fries": 10000,
    "Jasmin Tea": 5000,
    "Coca Cola": 12000
}
print("=============DAFTAR MENU=============")
for i in menu:
    print("Daftar Menu: ", i,"\tHarga: ", menu[i])
print("Pembelian Diatas Rp.100. 000, Mendapatkan diskon 15%")
print("======================================")

beli = input("Pilih Menu: ")
jumlah = int(input("Jumlah Pesanan: "))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar * 15/100
    total = bayar - diskon
else:
    total = bayar
    
print("=============Detail Bayar=============")
print("Menu yang dipesan    : ", beli)
print("Jumlah yang dipesan  : ", jumlah)
print("Total biaya          : ", bayar)
print("Total bayar          : ", total)