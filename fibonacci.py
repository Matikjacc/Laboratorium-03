x_size = 10
y_size = x_size
tablica = [[[] for i in range(x_size)] for j in range(y_size)]
x = int((x_size+1) / 2)-1
y = int(y_size / 2)
tablica[y][x] = 1
tablica[y][x + 1] = 1
y -= 1
x += 1
last_1 = 1
last_2 = 1
num_num = 1
parity = 0
direction = 0
while 0 <= x < x_size and 0 <= y < y_size:
    if parity == 0:
        num_num += 1
    # lewo
    if direction == 0:
        for i in range(num_num):
            if 0 <= x < x_size:
                tablica[y][x] = last_1 + last_2
                temp = last_1
                last_1 = last_1 + last_2
                last_2 = temp
                x -= 1
            else:
                break
        direction += 1
    elif direction == 1:
        for i in range(num_num):
            if 0 <= y < y_size:
                tablica[y][x] = last_1 + last_2
                temp = last_1
                last_1 = last_1 + last_2
                last_2 = temp
                y += 1
            else:
                break
        direction += 1
    elif direction == 2:
        for i in range(num_num):
            if 0 <= x < x_size:
                tablica[y][x] = last_1 + last_2
                temp = last_1
                last_1 = last_1 + last_2
                last_2 = temp
                x += 1
            else:
                break
        direction += 1
    elif direction == 3:
        for i in range(num_num):
            if 0 <= y < y_size:
                tablica[y][x] = last_1 + last_2
                temp = last_1
                last_1 = last_1 + last_2
                last_2 = temp
                y -= 1
            else:
                break
        direction = 0
    parity = (parity + 1) % 2
    print()
for i in range(y_size):
    print(tablica[i])
