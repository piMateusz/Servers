#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict
from abc import ABC, abstractmethod
import re


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

class ServerExceptions(Exception):
    """Class for server's errors"""
    def __init__(self, msg = None):
        if msg is None:
            msg = "Server error occured"
        super().__init__(msg)

class TooManyProductsFoundError(ServerExceptions):
    """Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów."""
    def __init__(self, msg = None):
        if msg is None:
            msg = "Too many products found"
        super().__init__(msg)


class NoProductFoundError(ServerExceptions):
    """Reprezentuje wyjątek związany z brakiem szukanego produktu."""
    def __init__(self, msg = None):
        if msg is None:
            msg = "Product matching your expectations does not exist"
        super().__init__(msg)

class Server(ABC):
    @abstractmethod
    def filtrate(self, pattern: str):
        raise NotImplementedError()

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        pattern: str = r'^[a-zA-Z]{' + str(n_letters) + r'}\d{2,3}$'
        price_list: List[Product] = self.filtrate(pattern)
        if price_list is None:      # None if too many products
            raise TooManyProductsFoundError
        if not price_list:
            raise NoProductFoundError
        else:
            price_list = sorted(price_list, key=lambda product: product.price)
            return price_list

class ListServer(Server):

    n_max_returned_entries: int = 3

    def __init__(self, products: List[Product]):
        self.products = products

    def filtrate(self, pattern: str):
        price_list: List[Product] = []
        for product_index in range(len(self.products)):
            if len(price_list) > self.n_max_returned_entries:
                return None
            if re.match(pattern, self.products[product_index].name):
                price_list.append(self.products[product_index])
        return price_list


class MapServer(Server):

    n_max_returned_entries: int = 3

    def __init__(self, products: List[Product]):
        products_dict: Dict[str, Product] = {}
        for product in products:
            products_dict[product.name] = product
        self.products = products_dict

    def filtrate(self,  pattern: str):
        price_list: List[Product] = []
        for product_name in self.products:
            if len(price_list) > self.n_max_returned_entries:
                return None
            if re.match(pattern, product_name):
                price_list.append(self.products[product_name])
        return price_list


class Client:
    def __init__(self, server: Server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            price_list: Optional[float] = self.server.get_entries(n_letters)
            price_all_products: int = 0
            for product in price_list:
                price_all_products += product.price
            return price_all_products

        except TooManyProductsFoundError:
            return None

        except NoProductFoundError:
            return None