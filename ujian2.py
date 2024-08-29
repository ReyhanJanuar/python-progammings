def cek_status(nilai_tugas):
      if not nilai_tugas:
        return "Daftar nilai tugas kosong."
    
    rata_rata = sum(nilai_tugas) / len(nilai_tugas)
    
    if rata_rata >= 70:
        status = "Lulus"
    elif 50 <= rata_rata < 70:
        status = "Perbaikan"
    else:
        status = "Tidak Lulus"
    
    return f"Status: {status}. Rata-rata nilai tugas: {rata_rata:.2f}"

def main():
    print("Masukkan nilai untuk tiga tugas.")
    
    nilai_tugas = []
    
    for i in range(1, 4): 
        while True:  
            try:
                nilai = float(input(f"Nilai tugas {i}: "))
                if 0 <= nilai <= 100:  # Validasi nilai
                    nilai_tugas.append(nilai)
                    break  
                else:
                    print("Nilai harus antara 0 dan 100. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Harap masukkan nilai numerik.")
    
    hasil = cek_status(nilai_tugas)
    print(hasil)

if __name__ == "__main__":
    main()
