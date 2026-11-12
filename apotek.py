
print("=== DATA OBAT DI APOTEK ===")

obat = [
    ["Paracetamol", 5000, 50],
    ["Amoxicillin", 12000, 20],
    ["Vitamin C", 10000, 30],
    ["Antasida", 8000, 15],
    ["Ibuprofen", 9000, 8],
    ["CTM", 4000, 0],
    ["Omeprazole", 18000, 12],
    ["Oralit", 3000, 40],
    ["Cetirizine", 7000, 5],
    ["OBH", 15000, 25]
]

for data in obat:
    nama = data[0]
    harga = data[1]
    stok = data[2]

    print("\nNama Obat:", nama)
    print("Harga: Rp", harga)
    print("Stok:", stok)

    if stok > 20:
        print("Keterangan: Stok Banyak")
    elif stok >= 10:
        print("Keterangan: Stok Cukup")
    elif stok > 0:
        print("Keterangan: Stok Menipis")
    else:
        print("Keterangan: Obat Habis")

    if stok == 0:
        print("Status: Tidak Tersedia")
    else:
        print("Status: Tersedia")

print("\nData obat selesai ditampilkan.")
