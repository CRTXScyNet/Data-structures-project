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
