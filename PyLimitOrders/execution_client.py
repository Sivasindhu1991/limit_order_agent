
from typing import Protocol

class ExecutionException(Exception):
    pass

class ExecutionClient(Protocol):
    def buy(self, product_id: str, amount: int):
        """
        Execute a buy order, throws ExecutionException on failure

        :param product_id: the product to buy
        :param amount: the amount to buy
        :return: None
        """
        pass

    def sell(self, product_id: str, amount: int):
        """
        Execute a sell order, throws ExecutionException on failure

        :param product_id: the product to sell
        :param amount: the amount to sell
        :return: None
        """
        pass

class LimitOrderAgent:
    def __init__(self, execution_client: ExecutionClient):
        self.execution_client = execution_client
        self.orders = []

    def price_tick(self, product_id: str, price: float):
        # Check if any held orders can be executed
        self.execute_held_orders(product_id, price)

    def add_order(self, buy_flag: bool, product_id: str, amount: int, limit_price: float):
        self.orders.append((buy_flag, product_id, amount, limit_price))

    def execute_held_orders(self, product_id: str, price: float):
        for order in self.orders:
            buy_flag, _, amount, limit_price = order
            if (buy_flag and price <= limit_price) or (not buy_flag and price >= limit_price):
                try:
                    if buy_flag:
                        self.execution_client.buy(product_id, amount)
                    else:
                        self.execution_client.sell(product_id, amount)
                except ExecutionException as e:
                    print(f"Execution failed: {e}")
        # Remove executed orders