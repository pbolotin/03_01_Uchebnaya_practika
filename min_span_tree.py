import sys

def print_help():
    print("""Для неориентированного взвешенного графа
эта программа может найти минимальное остовное дерево.

Использование программы в командной строке:

[1]              [2]
min_span_tree.py [filename]

[1] - вызов самой программы
[2] - аргумент программы - имя файла с входными данными [filename]

Пример вызова:
min_span_tree.py adjacency_matrix.csv

Формат [filename] формат соответствует стандартному csv-файлу.

В [filename] должны быть следующие данные
(пример для графа из 5 вершин, и 7 рёбер), :

5;A;B;C;D;E
A;0;2;0;8;4
B;2;0;3;0;0
C;0;3;0;5;1
D;8;0;5;0;7
E;4;0;1;7;0

В левом верхнем углу указывается количество вершин в графе (в примере 5).

Разделитель данных - ; - точка с запятой

Далее, по первой горизонтали и вертикали, указываются имена вершин.
Остальные места заполнены матрицей смежности для взвешенного
неориентированного графа.

Вывод программы:
Список рёбер минимального остовного дерева графа. Его вес.
""")

def check_number_of_arguments():
    if 2 != len(sys.argv): return False

def load_matrix_from_file():
    data_file = open(sys.argv[1])
    data = [] 
    for i in data_file:
        data.append(i.strip().split(";"))
        
    data_file.close()
    print(data)

if __name__ == "__main__":
    if(check_number_of_arguments() == False):
        print_help()
        exit()
    load_matrix_from_file()