from typing import Protocol
from trading_framework import ExecutionClient

class Pricelistener(Protocol):
    def on_price_tick(self, product_id: str, price: float):
        pass

class LimitOrderAgent:
    def __init__(self, execution_client: ExecutionClient):
        self.execution_client = execution_client
        self.orders = []

    def add_order(self, buy_flag: bool, product_id: str, amount: int, limit_price: float):
        self.orders.append((buy_flag, product_id, amount, limit_price))

class LimitOrderAgentTest(unittest.TestCase):
    def test_add_order(self):
        execution_client = ExecutionClient()
        agent = LimitOrderAgent(execution_client)
        agent.add_order(True, "IBM", 1000, 99)
        self.assertEqual(len(agent.orders), 1)
        self.assertEqual(agent.orders[0], (True, "IBM", 1000, 99))

if __name__ == "__main__":
    unittest.main()