# Nama : Muhammad Syawal Samir
# NIM  : 2509116079
# Kelas: B

import pwinput

kabel_list = ["kabel utp", "kabel dropcore", "kabel lan", "kabel stp"]

users = {
    "manager": {"password": "123", "role": "Manager"},
    "staff": {"password": "123", "role": "Staff"}
}

def login():
    kesempatan = 3
    while kesempatan > 0:
        username = input("username: ")
        password = pwinput.pwinput("password:")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"\nSelamat datang {username} (Role: {role})")
            return role
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print(f"login gagal. sisa kesempatan: {kesempatan}")
            else:
                print("login gagal setelah 3 kali. keluar program,")
                exit()

def tampilkan_kabel():
    print("\n=== Daftar Kabel ===")
    for idx, nama in enumerate(kabel_list, start=1):
        print(f"{idx}. {nama}")

def tambah_kabel():
    nama = input("Masukkan nama kabel baru: ")
    kabel_list.append(nama)
    print(f"Kabel '{nama}' ditambahkan.")

def update_kabel():
    tampilkan_kabel()
    try:
        nomor = int(input("Masukkan nomor kabel yang mau diupdate: "))
        if 1 <= nomor <= len(kabel_list):
            nama_baru = input("Masukkan nama baru: ")
            kabel_list[nomor-1] = nama_baru
            print("Data berhasil diupdate.")
        else:
            print("Nomor tidak ditemukan.")
    except ValueError:
        print("Masukkan angka!")

def hapus_kabel():
    tampilkan_kabel()
    try:
        nomor = int(input("Masukkan nomor kabel yang mau dihapus: "))
        if 1 <= nomor <= len(kabel_list):
            dihapus = kabel_list.pop(nomor-1)
            print(f"Kabel '{dihapus}' dihapus.")
        else:
            print("Nomor tidak ditemukan.")
    except ValueError:
        print("Masukkan angka!")
    except KeyboardInterrupt:
        print("Jangan Tekan CTRL+C")
    except EOFError:
        print("Jangan Tekan CTRL+Z")

def menu(role):
    while True:
        if role == "Manager":
            tampilkan_kabel()
            print("\nMenu Manager:")
            print("1. Tambah Kabel")
            print("2. Update Kabel")
            print("3. Hapus Kabel")
            print("4. Keluar")
            pilih = input("Pilih menu: ")

            if pilih == "1":
                tambah_kabel()
            elif pilih == "2":
                update_kabel()
            elif pilih == "3":
                hapus_kabel()
            elif pilih == "4":
                print("Keluar.")
                break
            else:
                print("Pilihan tidak ada.")
        else:
            print("\nMenu Staff:")
            print("1. Lihat Kabel")
            print("2. Keluar")
            pilih = input("Pilih menu: ")

            if pilih == "1":
                tampilkan_kabel()
            elif pilih == "2":
                print("Keluar.")
                break
            else:
                print("Pilihan tidak ada.")

def main():
    role = login()
    menu(role)

main()