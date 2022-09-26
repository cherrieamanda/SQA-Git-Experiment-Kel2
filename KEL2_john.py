# Kelompok 2
# Cherrie Gracilia Amanda
# Fauzan Farhan Antoro
# Farrel Ibrahim

# Seminggu (40 jam)
# Pengeluaran = 600000
# standar = 15000 per jam
# lembur 1.5x gaji standar
# lembur = 22500 per jam

def hitung_gaji(jam):
    if jam <= 40:
        gaji = jam * 15000
    else:
        gaji = 40 * 15000 + (jam - 40) * 22500

    return gaji

def main():
    jam = int(input("Masukkan jumlah jam kerja: "))
    gaji = hitung_gaji(jam)
    
    print("Gaji yang diterima: Rp. {0}".format(gaji))

    pengeluaran = int(input("Masukkan pengeluaran: "))
    if pengeluaran > gaji:
        print("cari tambahan")
    elif pengeluaran == gaji:
        print("tidak bisa menabung")
    else:
        print("bisa menabung")
    
if __name__ == "__main__":
    main()