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

    def get_entries(self, n_letters: int = 1)-> List[float]:
        price_list: List[float] = filtrate(n_letters)

        # TO DO - sort returned list

    @abstractmethod
    def filtrate(self, n_letters: int = 1):
        pass

#   (3) możliwość odwołania się do metody
#  `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania


class ListServer(Server):

    n_max_returned_entries: int = 3

    def __init__(self, products: List[Product]):
        self.products = products

    def filtrate(self, n_letters: int = 1):
        price_list: List[float] = []
        for product_index in range(len(self.products)):
            if product_index == n_max_returned_entries - 1:
                break
            if re.match('[a - z]{n}[0-9]{2-3}', self.products[product_index].name):
                price_list.append(product.name)

        return price_list

class MapServer:
    def __init__(self, product_dict: Dict[Product.name,Product]):
        self.product_dict= product_dict
   


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
 
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
