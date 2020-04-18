import random

def tebakAngka(jawaban):
    if jawaban == 1:
        return 'Nilai kamu adalah 1'
    elif jawaban == 2:
        return 'Nilai kamu adalah 2'
    elif jawaban == 3:
        return 'Nilai kamu adalah 3'
    elif jawaban == 4:
        return 'Nilai Kamu 4, Bagus!'
    elif jawaban == 5:
        return 'Nilai kamu 5, Keren abis!'

print(tebakAngka(random.randint(1,9)))
