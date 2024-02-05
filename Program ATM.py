class ATM:
    def __init__(self, saldoA=0):
        self.saldo = saldoA
        self.mutasi_list = []

    def cek_saldo(self):
        return self.saldo

    def ambil_uang(self, jumlah):
        if jumlah > 0 and jumlah <= self.saldo:
            self.saldo -= jumlah
            self.mutasi_list.append(f"Keluar: Mengambil {jumlah} uang. Saldo anda sekarang: {self.saldo}")
            return f"Anda berhasil mengambil {jumlah} uang. Saldo anda sekarang: {self.saldo}"
        else:
            return "Gagal mengambil uang. Saldo tidak mencukupi."

    def simpan_uang(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            self.mutasi_list.append(f"Masuk: Menyimpan {jumlah} uang. Saldo anda sekarang: {self.saldo}")
            return f"Anda berhasil menyimpan {jumlah} uang."
        else:
            return "Gagal menyimpan uang. Jumlah uang harus lebih dari 0."

    def mutasi(self):
        return self.mutasi_list

# Pindahkan fungsi main() ke luar dari class
atm = ATM()
Max = 3
count = 0
if count < Max:
    while True:
        pw = input("Masukkan password: ")
        if pw == '123':
            while True:
                print("\nMenu ATM: ")
                print("1. Cek Saldo")
                print("2. Ambil Uang")
                print("3. Simpan Uang")
                print("4. Mutasi")
                print("5. Keluar")

                pilihan = input("Masukkan Pilihan 1-5: ")

                if pilihan == '1':
                    print(f"Saldo anda saat ini: {atm.cek_saldo()}")
                elif pilihan == '2':
                    jumlah = int(input("Masukkan jumlah uang yang akan diambil: "))
                    print(atm.ambil_uang(jumlah))
                elif pilihan == '3':
                    jumlah = int(input("Masukkan jumlah uang yang akan disimpan: "))
                    print(atm.simpan_uang(jumlah))
                elif pilihan == '4':
                    print("Mutasi:")
                    for transaksi in atm.mutasi():
                        print(transaksi)
                elif pilihan == '5':
                    print("Terima kasih! Keluar dari program.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")
        else:
            print("Password anda salah")
            count +=1
            if count == Max:
                print("Akun anda di Blokir!")
                break

