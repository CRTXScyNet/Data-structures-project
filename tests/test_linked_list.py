"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest

from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_insert_at_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})

        self.assertEqual("{'id': 0} -> {'id': 1} -> None", str(ll))

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})

        self.assertEqual("{'id': 2} -> {'id': 3} -> None", str(ll))

