import time


count = 0
while True:
    zero = 0
    minute = 'minute'
    count = count + 1

    for x in range(0, 60):
        if x < 10:
            print(f'{minute, count}:{zero}{x}')
        elif x > 9:
            print(f'{minute, count}:{x}')
        
        time.sleep(1)
