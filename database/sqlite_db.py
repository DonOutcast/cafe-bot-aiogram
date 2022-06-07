import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect("cafe.db")
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, types_dish TEXT, price INT)')
    base.commit()

async def sql_add_command(state):
    async  with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?,?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute("SELECT * FROM menu").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_read2():
    return cur.execute("SELECT * FROM menu").fetchall()

async def sql_salad(message):
    for ret in cur.execute("SELECT * FROM menu WHERE types_dish LIKE 'Салаты'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}' )

async def sql_first_dish(message):
    for ret in cur.execute("SELECT * FROM menu WHERE types_dish LIKE 'Первое блюдо'").fetchall():
      await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_second_dish(message):
    for ret in cur.execute("SELECT * FROM menu WHERE types_dish LIKE 'Второе блюдо'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_drinks(message):
    for ret in cur.execute("SELECT * FROM menu WHERE types_dish LIKE 'Напитки'  ").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_flour_products(message):
    for ret in cur.execute("SELECT * FROM menu WHERE types_dish LIKE 'Мучное изделие' ").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_desserts(message):
    for ret in cur.execute("SELECT * FROM menu WHERE types_dish LIKE 'Дессерт' ").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def rename_price(new_price, new_name):
    cur.execute("UPDATE menu SET price = "+new_price +" WHERE name = "+new_name)
async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()