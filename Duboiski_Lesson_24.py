#ДЗ на пятницу. Создайте таблицу в БД, заполните минимум 10-ю записями.
# Половину записей удалите (DELETE), а вторую измените (с помощью UPDATE).
# Точное количество записей вы не знаете, поэтому код должен быть
# универсальным - для любого количества записей в таблице.

import sqlite3, random
conn = sqlite3.connect('my_db.db')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1 TEXT) ''')

cursor.execute('''DELETE FROM table1''')
conn.commit()

col = int(input('Введите какое количество записей добавить в базу данных: '))
for i in range(col):
    cursor.execute(''' INSERT INTO table1(col_1) VALUES (?) ''', ('Строка ' + str(i+1),))
conn.commit()

print('Записи в базе данных:')
cursor.execute('''SELECT * FROM table1''')
k = cursor.fetchall()
for i in k:
    print(*i)

cursor.execute('''SELECT id FROM table1''')
k = cursor.fetchall()
n = len(k)//2
for i in range(n):
    cursor.execute('''DELETE FROM table1 WHERE id=?''', (random.choice(k)[0],))
    conn.commit()
cursor.execute('''SELECT id FROM table1''')
k = cursor.fetchall()
for i in k:
    cursor.execute('''UPDATE table1 SET col_1=? WHERE id=?''', (f'Строка {str(i[0])} обновлена', i[0]))
    conn.commit()

print('Осталось в базе записей:')
cursor.execute('''SELECT * FROM table1''')
k = cursor.fetchall()
for i in k:
    print(*i)
conn.close()