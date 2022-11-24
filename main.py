def create_index(name: str, table: str, column: str):
    return f"create index ix{table}_{name} on {table} ({column})"


def start():
    res = []
    table_name: str = f'[{input("Введите название таблицы: ")}]'
    counter: int = int(input("Введите количество стобцов: "))
    tmp: int = counter
    while tmp != 0:
        a: str = input("введите имя столбца: ")
        res.append(f'[{a}]')
        tmp -= 1
    question: str = input("Хотите ли вы задать для каждого поля имя индекса? д/н ")
    if (question != 'д'):
        with open(f"{table_name}.txt", 'w') as file:
            file.write(table_name + " " + ",".join(res))
        return
    question: str = input("Хотите автоматически заполнить индексы теми же именами что и столбец? д/н ")
    if (question == 'д'):
        result = []
        for column in res:
            s = create_index(column, table_name, column)
            result.append(s)
        with open(f"{table_name}.sql", "w") as file:
            text = "\n".join(result)
            file.write(text)
        return
    if (question != 'н'):
        return
    strs = []
    i = 0
    while i != counter:
        b: str = input("Введите имя индекса вашего поля: ")
        if len(b.split(" ")) > 1:
            b = "_".join(b.split(" "))
        strs.append(create_index(b, table_name, res[i]))
        i += 1
    with open(f"{table_name}.sql", "w") as file:
        text = "\n".join(strs)
        file.write(text)


if __name__ == "__main__":
    start()
