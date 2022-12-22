n=int(input('ДАЙ ЧИСЛО ОТ 1 ДО 15 И Я СОЗДАМ ТАБЛИЦУ УМНОЖЕНИЯ ДЛЯ ТЕБЯ: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, end="\t")
    print()
