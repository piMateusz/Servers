import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer

server_types = (ListServer, MapServer)


class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))
    def test_list_get_entries(self):
        products = [Product('SD12', 1), Product('PQ34', 2), Product('PP235', 1)]
        server = ListServer(products)
        entries = server.filtrate(2)
        self.assertEqual(Counter([products[2], products[1]], products[0]), Counter(entries))

class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))
    def test_total_price_for_exceptions_execution(self):
        products = [Product('PP246', 4), Product('PP235', 2), Product('PP543', 6), Product('PP278', 4)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))
    def test_total_price_for_price_list_is_empty(self):
        products = [Product('PP246', 4), Product('PP235', 2), Product('PP543', 6), Product('PP278', 4)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(3))  

if __name__ == '__main__':
    unittest.main()
