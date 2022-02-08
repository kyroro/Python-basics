# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('script_2.txt') as f:
    file = f.readlines()

count_str = 0
for i in file:
    count_str += 1
    count_word = len(i.split())
    print(f'{count_word} - слов в строке')
print(f'{count_str} - количество строк')
