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

    def test_to_list(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        self.assertEqual(ll.to_list(), [
            {'id': 0, 'username': 'serebro'},
            {'id': 1, 'username': 'lazzy508509'},
            {'id': 2, 'username': 'mik.roz'},
            {'id': 3, 'username': 'mosh_s'}
        ])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
