import time
import random
import sys
class CustomRandom:
    def __init__(self):
        """
        Инициализация генератора случайных чисел, зависимого от текущего времени.
        """
        self.seed = int(time.time())

    def random(self):
        """
        Генерация случайного числа в диапазоне [0, 1).
        """
        self.seed = (self.seed * 1103515245 + 12345) & 0x7fffffff
        return self.seed / 0x7fffffff

    def randint(self, a, b):
        """
        Генерация случайного целого числа в диапазоне [a, b].
        """
        return int(self.random() * (b - a + 1)) + a

class TreeNode:
    def __init__(self, value):
        """
        Инициализация узла дерева с указанным значением.
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Возвращает строковое представление узла.
        """
        return f"Node({self.value})"

class BinaryTree:
    def __init__(self):
        """
        Инициализация пустого бинарного дерева.
        """
        self.root = None
        # self.initial_traversal = None  # Свойство для хранения исходного состояния дерева обхода

    def insert(self, value):
        """
        Вставка значения в бинарное дерево.
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        """
        Вспомогательная рекурсивная функция для вставки значения в дерево.
        """
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def depth_first_traversal(self, node=None):
        """
        Обход дерева в порядке глубины (in-order traversal).
        """
        if node is None:
            node = self.root

        if node:
            if node.left:
                self.depth_first_traversal(node.left)
            print(node.value, end=" ")
            if node.right:
                self.depth_first_traversal(node.right)

    def set_initial_traversal(self):
        """
        Записывает исходное состояние дерева обхода.
        """
        if self.root is not None:
            self.initial_traversal = []
            self._record_initial_traversal(self.root)

    def _record_initial_traversal(self, node):
        """
        Вспомогательная рекурсивная функция для записи исходного состояния дерева обхода.
        """
        if node:
            self._record_initial_traversal(node.left)
            self.initial_traversal.append(node.value)
            self._record_initial_traversal(node.right)

def main():
    # Создаем экземпляр рандома
    custom_random = CustomRandom()

    # Создаем пустое бинарное дерево
    binary_tree = BinaryTree()
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0

    count_1_1 = 0
    count_2_2 = 0
    count_3_3 = 0
    count_4_4 = 0
    count_5_5 = 0
    count_6_6 = 0


    # Разыгрываем случайное СВ:
    for _ in range(100000):
        v = custom_random.randint(1, 6)
        if v == 1:
            count_1 = count_1 + 1
        if v == 2:
            count_2 = count_2 + 1
        if v == 3:
            count_3 = count_3 + 1
        if v == 4:
            count_4 += 1
        if v== 5:
            count_5 += 1
        if v==6:
            count_6 += 1
    print("1:", count_1 , " 2:", count_2, " 3: ", count_3, " 4:", count_4, " 5:", count_5, " 6:", count_6)
    for _ in range(100000):
        v = random.randint(1, 6)
        if v == 1:
            count_1_1 = count_1_1 + 1
        if v == 2:
            count_2_2 = count_2_2 + 1
        if v == 3:
            count_3_3 = count_3_3 + 1
        if v == 4:
            count_4_4 += 1
        if v == 5:
            count_5_5 += 1
        if v == 6:
            count_6_6 += 1
    print("1:", count_1_1, " 2:", count_2_2, " 3: ", count_3_3, " 4:", count_4_4, " 5:", count_5_5, " 6:", count_6_6)

    #Подсчитать мат ожидание и дисперсию.



    # Вставляем случайные значения в дерево
    for _ in range(10):
        value = custom_random.randint(1, 100)
        print("Рандомное число:" , value)
        binary_tree.insert(str(value) + "char")

    # Выводим дерево в порядке глубины
    print("\nОбход дерева в порядке глубины:")
    binary_tree.depth_first_traversal()

    # Создаем узлы и связываем их между собой
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    print("\n", root)

if __name__ == "__main__":
    main()
