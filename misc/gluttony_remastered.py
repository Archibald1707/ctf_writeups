#ncat mctf-game.ru 4040 | gluttony1.py

import sys

max_number = 0
max_id = 0
was_last_number = 0

while sys.stdin != '':
    gavno = sys.stdin.readline()
    sys.stdout.write(gavno)
    if len(gavno) >= 3:
        if ord(str(gavno)[2]) == 45 and was_last_number == 1:
            print(max_id)
            sys.stdout.write(str(max_id))
            max_number = 0
            max_id = 0
        if ord(str(gavno)[2]) >= 49 and ord(str(gavno)[2]) <= 57:
            was_last_number = 1
            number = int((gavno.split('|')[-2]).replace(' ',''))
            idx = int((gavno.split('|')[1]).replace(' ','').replace('.', ''))
            if max_number < number:
                max_number = number
                max_id = idx
        else:
            was_last_number = 0