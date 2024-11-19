class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.__top = None

    def __str__(self):
        node = self.top
        result = []
        while node is not None:
            result.append(node.data)
            node = node.next_node

        return '\n'.join(i for i in result)


    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

        node = Node(data, self.top)
        self.__top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        elif isinstance(self.top, Node):
            node = self.top
            self.__top = self.top.next_node
            return node.data

    @property
    def top(self):
        return self.__top

