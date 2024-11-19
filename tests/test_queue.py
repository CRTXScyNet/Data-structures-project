"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Node, Queue


class TestNode(unittest.TestCase):

    def test_init(self):
        node = Node('sss',None)
        self.assertEqual(node.data, 'sss')
        self.assertIsNone(node.next_node)

class TestQueue(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.head.data, 'data1' )
        self.assertEqual(queue.tail.data, 'data3' )

    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(str(queue), 'data1\ndata2\ndata3')