# Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно вставив после строки N (N – задается пользователем)
# произвольную фразу.
l = 0

for i in open('text18-29.txt', encoding='UTF-8'):
    print(i, end='', )
    for m in i:
        l += 1
print("\nКолличество симмволов в тексте :", l)

n = int(input("Введите номер строки, после которой будет вставлена строка : "))
d = input("Введите фразу , которая будет последней строкой : ")
l = open("text.txt", "w", encoding="UTF-8")
for i in open('text18-29.txt', encoding='UTF-8'):
    l.write(i)

f1 = open('text18-29.txt', encoding='UTF-8')
l = f1.readlines()
l[n - 1] = l[n - 1] + d
f1.close()

f2 = open('text.txt', "w", encoding='UTF-8')
f2.writelines(l)
f2.close()
