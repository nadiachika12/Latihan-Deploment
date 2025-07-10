"""
# apa itu function

def sapa():
    print("pagi sayangku")

sapa()

# parameter
def sapa_nama(nama):
    print("namaku adalah", nama)

sapa_nama("chika")    
"""

'''
def luas_persegi_panjang(panjang, lebar):
    #isi function
    luas = panjang  * lebar
    return luas

panjang = 20
lebar = 3

#memanggil function
luas_persegi = luas_persegi_panjang(panjang, lebar)
print("luas persegi panjang: ", luas_persegi)
'''

'''
               #param1  param2
def luas_persegi_panjang(panjang, lebar):
    #isi function
    # logic/rumus
    luas = panjang * lebar
    #pengembalian
    return luas
# definisi variable
panjang = 20
lebar = 3

#memangil function
              # panggil func  # args1  #args2
luas_persegi_panjang(panjang, lebar)
'''

'''
def hitung_nilai(jumlah_benar):
    total_soal = 10
    nilai_maksimum = 100
    nilai = (jumlah_benar / total_soal) * nilai_maksimum
    return nilai
jawaban_benar = int(input("masukan jumlah soal yang di jawab benar (0-10: "))
if 0 = jawaban_benar ,= 10:
    nilai_akhir = hitumg_nilai(jawaban_benar)
    print(f"nilai akhir anda adalah:{nilai_akhir}")
else:
    print("input tidak valid. masukan angka antara 0 sampai 10.  ")
'''
#fungsi untuk menampilkan menu
def tampilkan_menu():
    print("====menu makanan====")
    print("1. nasi goreng -Rp15.000")
    print("2. nasi rames -Rp10.000")
    print("3. nasi ayam -Rp8.000")
    print("4. mie goreng -Rp18.000")
def main():
    tampilkan_menu()
    
    # cari menu
    cari = input("\ingin cari menu? (ketik nama menu yang ingin di pesan: ").lower()
    pilihan = input("\masukan nama menu yang indngin di pesan: ").lower()
    if pilihan in menu:
        harga = menu[pilihan]
        print(f"n\anda memilih: {pilihan.title()} - Rp {harga}")
        else:
            print("menu tidak tersedia.")

main()            
        
def main():
    tampilkan_menu()
    pilihan = int(input("\nmasukan nomor menu yang ingin di pesan: "))
    if pilihan == 1:
        makanan = "nasi goreng"
        harga = 15000
    elif pilihan == 2:
        makanan = "nasi rames"
        harga = 10000
    elif pilihan == 3:
        makanan = "nasi ayam"
        harga = 8000
    elif pilihan == 4:
        makanan = "mie goreng"
        harga = 18000    
    else:
        print("pilihan tidak tersedia.")
        return
    print(F"\nanda memilih: {makanan} -Rp{harga}")
    pembayaran(harga)


main()
        
def pembayaran(harga):
    print(f"\ntotal yang harus dibayar:Rp{harga}")
    uang = int(input("masukan jumlah uang anda:Rp"))
    if uang.harga:
        kembalian = uang-harga
        print(f"pembayaran berhasil.kembalian anda:Rp{kembalian}")
    else:
        print("uang tidak cukup silahkan coba lagi.")
























































