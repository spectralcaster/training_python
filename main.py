from banner import banner_message   # import file dengan berbeda folder
import exit                         # import file dalam 1 folder
from games import hamster           # import file dengan berbeda folder
from tools import warung

def options():
    user_option = int(input(f'Menu Program: \n1. Game Hamster \n2. Warung Mini\n3. Keluar Program\n\nSilahkan pilih : '))
    return user_option

def menu():
    # options()                        # Jika tidak ada Variable maka ketika kita ketik apapun program akan lanjut
    user_option = options()
    if user_option == 1:
        hamster.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit.exit_program()
    else:
        # print("Pilih yang tersedia.")
        user_option = int(input(f'\nPilih yang tersedia : '))
        
def main():
    banner_message()
    menu()
    
if __name__ == '__main__':
    main()