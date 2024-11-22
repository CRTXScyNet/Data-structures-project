class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, previous, next):
        self.__data = data
        self.previous = previous
        self.next_node = next

    @property
    def data(self):
        return self.__data


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.begin = None
        self.end = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет
        узел с этими данными в начало связанного списка"""
        if self.begin is None:
            self.begin = Node(data, None, None)
            self.end = Node(data, None, None)
        else:
            if self.begin.next_node is None:
                self.begin = Node(data, None,self.end)
                self.end.previous = self.begin
            else:
                node = self.begin
                self.begin = Node(data, None, node)
                node.previous = self.begin

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет
        узел с этими данными в конец связанного списка"""
        if self.end is None:
            self.begin = Node(data, None, None)
            self.end = Node(data, None, None)
        else:
            if self.end.previous is None:
                self.end = Node(data, self.begin, None)
                self.begin.next_node = self.end
            else:
                node = self.end
                self.end = Node(data, node, None)
                node.next_node = self.end


    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.begin
        if node is None:
            return str(None)

        ll_list = []
        while node:
            ll_list.append(f'{str(node.data)}')
            node = node.next_node

        ll_string = ' -> '.join(ll_list)
        ll_string += ' -> None'
        return ll_string
