

from typing import List, Tuple
from price_listener import PriceListener
from execution_client import ExecutionClient

class LimitOrderAgent(PriceListener):
    def __init__(self, execution_client: ExecutionClient) -> None:
        self.execution_client = execution_client
        self.orders: List[Tuple[bool, str, int, float]] = []
        super().__init__()

    def on_price_tick(self, product_id: str, price: float):
        self.execute_held_orders(product_id, price)

    def add_order(self, buy_flag: bool, product_id: str, amount: int, limit_price: float):
        self.orders.append((buy_flag, product_id, amount, limit_price))

    def execute_held_orders(self, product_id: str, price: float):
        for order in self.orders:
            buy_flag, _, _, limit_price = order
            if buy_flag and price <= limit_price:
                self.execution_client.buy(product_id, amount, price)
            elif not buy_flag and price >= limit_price:
                self.execution_client.sell(product_id, amount, price)
        self.orders = [(buy_flag, product_id, amount, limit_price) for buy_flag, product_id, amount, limit_price in self.orders
                       if (buy_flag and price > limit_price) or (not buy_flag and price < limit_price)]