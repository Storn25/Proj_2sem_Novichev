# Программа переводит все символы верхнего регистра в нижний
a = "СтроКА с ЛюБым ЗНачЕНИем"
print("Оригинал:       ", a)


def aaa():
    yield from [i.lower() if i.isupper() else i for i in a]


print("Итоговый текст: ", "".join(aaa()))
