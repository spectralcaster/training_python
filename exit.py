from time import sleep

def exit_program():
    print('Program akan dihentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program berhasil dihentikan..')
    exit()

if __name__ == '__main__':
    exit_program()