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

class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


class Server(ABC):

    def get_entries(self, n_letters: int = 1) -> List[float]:
        pattern = '[a - z]{n}[0-9]{2-3}'
        try:
            price_list: List[float] = filtrate(pattern)
            if price_list is None:      # None if too many products
                raise ValueError()      # TO DO: replace it with appropriate error
            else:
                return price_list       # TO DO - sort returned list here
        except ValueError():
            print("Too many products in server !")

    @abstractmethod
    def filtrate(self, n_letters: int = 1):
        raise NotImplementedError()


class ListServer(Server):

    n_max_returned_entries: int = 3

    def __init__(self, products: List[Product]):
        self.products = products

    def filtrate(self, pattern: str):
        price_list: List[float] = []
        for product_index in range(len(self.products)):
            if product_index == n_max_returned_entries - 1:
                return None
            if re.match(pattern, self.products[product_index].name):
                price_list.append(product.name)

        return price_list


class MapServer(Server):
    def __init__(self, products: List[Product]):       #konstruktor ma brac jako argument liste produktow tak jak w ListServer (products: List[Product])
        products_dict = {}
        for product in products:
            products_dict[product.name] = product
        self.products = products_dict                                        #i z niej inicjalizowac slownik (kluczem jest nazwa produktu, wartością – obiekt reprezentujący produkt
    def filtrate(self, n_letters: int = 1):
        price_list: List[float]=[]
        names=self.products.keys()
        prod=self.products.values()
        for product_index in range(len(names)):
            if product_index == n_max_returned_entries -1:
                return None
            if re.match(pattern, names[product_index]):
                price_list.append(prod[product_index])
        return price_list


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, serwer:Server):
        self.client = serwer
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            price_list=self.client.get_entries(n_letters)
            if price_list is None:
                raise ValueError()
            else:
                price_all_products = 0
                for i in price_list:
                    price_all_products = price_all_products + i.price
                return price_all_products
        except ValueError():
            print("Zero products in server !")
