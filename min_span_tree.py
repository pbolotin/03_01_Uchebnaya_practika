import sys

class Graph:
    #set_of_vertex
    #list_of_edges
    
    def __init__(self, vertex):
        self.set_of_vertex = set()
        list_of_edges = []
        pass
        
    def add_edge(existing_vertex, new_vertex, weight):
        pass

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

def check_and_prepare_data(data):
    try:
        data[0][0] = int(data[0][0])
    except ValueError:
        print("""ОШИБКА!

Значение n в матрице, не получается конвертировать в число

Ниже показан пример правильной матрицы где n в левом верхнем углу равно 5.

5;A;B;C;D;E
A;0;2;0;8;4
B;2;0;3;0;0
C;0;3;0;5;1
D;8;0;5;0;7
E;4;0;1;7;0

Проверьте это место в ваших данных!""")
        exit()
    
    if data[0][0] < 1:
        print("""ОШИБКА!

Проверьте значение n - оно не должно быть меньше 1.""")
        exit()
    if len(data) != data[0][0] + 1:
        print("""ОШИБКА!

Проверьте количество строк входных данных!
Оно должно быть равно """, data[0][0] + 1, " для вашего n.")
        exit()
    for i in range(data[0][0] + 1):
        if len(data[i]) != data[0][0] + 1:
            print("""ОШИБКА!

Проверьте строки данных в них должно быть """, data[0][0]+1, "ячеек\n")
            exit()

    for i in range(1, data[0][0] + 1):
        if data[i][0] != data[0][i]:
            print("""ОШИБКА!

Названия вершин по вертикали и горизонтали должны быть последовательны!\n\n""", " Название: ", data[i][0], " не соответствует названию: ", data[0][i], "\n")
            exit()
            
    for i in range(1, data[0][0] + 1):
        for j in range(1, data[0][0] + 1):
            try:
                data[i][j] = int(data[i][j])
                if i == j and data[i][j] != 0:
                    print("""ПРЕДУПРЕЖДЕНИЕ!

В ячейке с индексами:""", i, i, 
"""ненулевое значение!
Это соответствует петле в графе, для минимального остова эти данные игнорируются!\n\n""")
            except ValueError:
                print("""ОШИБКА!

В ячейке матрицы данные которые не получается конвертировать в число!\n\nИндексы:""", i, j, "\nДанные:", data[i][j], "\n")
                exit()
                
    for i in range(1, data[0][0] + 1):
        for j in range(1, data[0][0] + 1):
            if data[i][j] != data[j][i]:
                print("""ОШИБКА!

Матрица смежности неориентированного взвешенного графа должна быть
симметричной относительно диагонали!
""")
                exit()

def check_number_of_arguments():
    if 2 != len(sys.argv): return False

def load_matrix_from_file():
    data_file = open(sys.argv[1])
    data = [] 
    for i in data_file:
        data.append(i.strip().split(";"))
        
    data_file.close()
    check_and_prepare_data(data)
    return data

def min_span_tree_Kruskal(data):
    pass
    
if __name__ == "__main__":
    if(check_number_of_arguments() == False):
        print_help()
        exit()
    data = load_matrix_from_file()
    min_span_tree_Kruskal(data)