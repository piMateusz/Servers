#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict
from abc import ABC, abstractmethod
import re

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    # TO_DO

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


class Server(ABC):

    @abstractmethod
    def search_products(self, name_length: int = 1)-> List[float]:
        pass

#   (3) możliwość odwołania się do metody
#  `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania


class ListServer(Server):

    n_max_returned_entries: int = 3

    def __init__(self, products: List[Product]):
        self.products = products

    def get_entries(self, n_letters: int = 1) -> List[float]:
        price_list: List[float] = []
        for product in self.product_list:

            if re.match(len(product.name), n_letters):
                pass
                #price_list.append(product.name)

class MapServer:
    def __init(self, product_dict: Dict[Product.name,Product]):
        self.product_dict= product_dict
   


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
 
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
