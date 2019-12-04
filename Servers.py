#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict
from abc import ABC, abstractmethod
import re

class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające
    #  nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności --
    #  i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)


class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


class Server(ABC):
    @abstractmethod
    def search_products(self, name_length: int = 1)-> List[float]:
        pass
    @abstractmethod
    def add_product(self, product: Product):
        pass

# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#  (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products`
#  zgodnie z typem reprezentacji produktów na danym serwerze,
#  (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int)
#  wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania, (3) możliwość odwołania się do metody
#  `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania


class ListServer(Server):
    def __init__(self, product_list: List[Product]):
        self.product_list = product_list

    def search_products(self, name_length: int = 1) -> List[float]:
        price_list: List[float] = []
        for product in self.product_list:

            if re.match(len(product.name), name_length):

                #price_list.append(product.name)
    def add_product(self, product: Product):
        self.product_list.append(product)

class MapServer:
    def __init(self, product_dict: Dict[Product.name,Product]):
        self.product_dict= product_dict
   


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
 
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
