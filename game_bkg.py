import random, sys

print('BATU, KERTAS, GUNTING')

# Variabel untuk menyimpan nilai menang, kalah dan seri
menang = 0
kalah = 0
seri = 0

while True:
    print('%s Menang, %s Kalah, %s Seri' %(menang,kalah,seri))
    while True: # Input loop pemain
        print('Masukkan langkahmu : (b)atu, (k)ertas, (g)unting atau (q)uit')
        pemain = input()
        if pemain == 'q':
            sys.exit() # Keluar dari program
        if pemain == 'b' or pemain == 'k' or pemain == 'g':
            break
        print('Ketik salah satu b, k, g atau q')

    #Tampilkan apa yang pemain pilih
    if pemain == 'b':
        print('BATU melawan...')
    elif pemain == 'k':
        print('KERTAS melawan...')
    elif pemain == 'g':
        print('GUNTING melawan...')

    #Tampilkan apa yang dipilih komputer
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        komputer = 'b'
        print('BATU')
    if randomNumber == 2:
        komputer = 'k'
        print('KERTAS')
    if randomNumber == 3:
        komputer = 'g'
        print('GUNTING')

    # Tampilkan dan catat menang / kalah / seri:
    if pemain == komputer:
        print('Seri!')
        seri = seri+1
    elif pemain == 'b' and komputer == 'g':
        print('Kamu menang!')
        menang = menang+1
    elif pemain == 'k' and komputer == 'b':
        print('Kamu menang!')
        menang = menang+1
    elif pemain == 'g' and komputer == 'k':
        print('Kamu menang!')
        menang = menang+1
    elif pemain == 'b' and komputer == 'k':
        print('Kamu kalah!')
        kalah = kalah+1
    elif pemain == 'k' and komputer == 'g':
        print('Kamu kalah!')
        kalah = kalah+1
    elif pemain == 'g' and komputer == 'b':
        print('Kamu kalah!')
        kalah = kalah+1
