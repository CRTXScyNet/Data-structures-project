"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_init(self):
        node = Node('a', None)
        node2 = Node('b', node)

        self.assertEqual(node.data, 'a')
        self.assertEqual(node2.data, 'b')
        self.assertEqual(node.next_node, None)
        self.assertEqual(node2.next_node, node)
        with self.assertRaises(AttributeError):
            node.next_node.next_node


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('a')

        self.assertEqual(stack.top.data, 'a')

        stack.push('b')

        self.assertEqual(stack.top.data, 'b')

        stack.push('c')

        self.assertEqual(stack.top.data, 'c')

        self.assertEqual(stack.pop(), 'c')

        self.assertEqual(stack.pop(), 'b')

        self.assertEqual(stack.pop(), 'a')

        self.assertEqual(stack.pop(), None)

        self.assertEqual(stack.pop(), None)

    def test_pop(self):

        stack = Stack()
        stack.push('data1')
        data = stack.pop()

        # стэк стал пустой
        self.assertIsNone(stack.top)

        # pop() удаляет элемент и возвращает данные удаленного элемента
        self.assertEqual(data, 'data1')

        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()

        # теперь последний элемента содержит данные data1
        self.assertEqual(stack.top.data, 'data1')

        # данные удаленного элемента
        self.assertEqual(data, 'data2')

    def test_str(self):
        stack = Stack()
        stack.push('sss')
        stack.push('adfasdf')
        stack.push('wssdfksss')
        stack.push('asdf23342dsf')

        self.assertEqual(str(stack), 'asdf23342dsf\nwssdfksss\nadfasdf\nsss')
