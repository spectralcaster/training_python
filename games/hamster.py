import random
import main

def start():
    nama_user = input("Masukan nama anda : ")

    while nama_user == "":              # Untuk mencegah user tidak input nama
        nama_user = input("Silahkan diisi nama anda : ")

    while True:                         # Awal looping program

        bentuk_kotak = "|_|"
        kotak = [bentuk_kotak] * 4

        kotak_kosong = kotak.copy()         # Mengcopy Variable

        hamster_position = random.randint(1, 4)
        kotak[hamster_position - 1] = "|0_0|"
        kotak = '  '.join(kotak)
        kotak_kosong = '  '.join(kotak_kosong)

        print(f"\nHallo {nama_user} !! Coba perhatikan kotak dibawah ini")
        print(f"\n{kotak_kosong}")

        pilihan_user = int(input("\nmenurut anda, hamster ada di kotak berapa..? [1 / 2 / 3 / 4] = "))

        # print(f"Pilihan anda adalah : {pilihan_user}")
        confirm_answer = input(f"Apakah anda yakin dengan jawaban : {pilihan_user} ? [y/n]: ")

        while confirm_answer == "n":
            pilihan_user = int(input("\nmenurut anda, hamster ada di kotak berapa..? [1 / 2 / 3 / 4] = "))
            confirm_answer = input(f"Apakah anda yakin dengan jawaban : {pilihan_user} ? [y/n]: ")

        if confirm_answer == "y":
            print (f"\n{kotak}")
            if pilihan_user == hamster_position:
                print(f"Selamat {nama_user}, Anda benar.. Posisi Hamster ada dikotak {hamster_position} dan pilihan anda adalah kotak {pilihan_user}.")
            else:
                print(f"Tetot, jawaban anda salah.. Posisi Hamster ada dikotak {hamster_position}")

        play_again = input("\nApakah ingin melanjutkan gamenya lagi.? [y/n] :")
        if play_again == "n":
    #         break       # break bisa digunakan jika menggunakan fungsi looping
    # # print("Program Selesai")
            main.menu()

if __name__ == '__main__':
    start()
