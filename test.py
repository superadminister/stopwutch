import time


count = 0
while True:
    zero = 0
    minute = 'minute'
    count = count + 1

    for x in range(0, 60):
        time.sleep(59)
        if x < 10:
            print(f'{minute, count}:{zero}{x}')
        elif x > 9:
            print(f'{minute, count}:{x}')
