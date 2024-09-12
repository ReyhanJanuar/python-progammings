jumlah_set = int(input("jumlah set transaksi:"))

for i in range(jumlah_set):
    print(f"\nSet Transaksi ke-{i+1}")

    target_uang = int(input("Masukkan target jumlah uang: "))

    jumlah_100 = int(input("Masukkan jumlah lembar/koin uang Rp.100"))
    jumlah_500 = int(input("Masukkan jumlah lembar/koin uang Rp.500"))
    jumlah_1000 = int(input("Masukkan jumlah lembar/koin uang Rp1000"))
    jumlah_5000 = int(input("Masukkan jumlah lembar/koin uang Rp.5000"))
    jumlah_10000 = int(input("Masukkan jumlah lembar/koin uang Rp.10000"))
    jumlah_20000 = int(input("Masukkan jumlah lembar/koin uang Rp.20000"))
    jumlah_50000 = int(input("Masukkan jumlah lembar/koin uang Rp.50000"))
    jumlah_100000 = int(input("Masukkan jumlah lembar/koin uang Rp.100000"))

    total_uang = (jumlah_100*100)+(jumlah_500*500)+(jumlah_1000*1000)+(jumlah_5000*5000)+(jumlah_10000*10000)+(jumlah_20000*20000)+(jumlah_50000*50000)+(jumlah_100000*100000)

    if total_uang > target_uang:
        print(f"Target jumlah uang Rp.{target_uang} sesuai dengan total uang sebesar Rp.{total_uang}")
    elif total_uang < target_uang:
        print(f"Target jumlah uang Rp.{target_uang} telah tercapai dengan total uang sebesar Rp.{total_uang}")
    else:
        print(f"Target jumlah uang Rp.{target_uang} Belum tercapai dengan total uang sebesar Rp.{total_uang}")
        