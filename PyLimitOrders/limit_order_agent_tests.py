

from unittest.mock import MagicMock
import unittest

class LimitOrderAgentTest(unittest.TestCase):
    def test_add_order(self):
        # Mock execution client
        execution_client = MagicMock()
        agent = LimitOrderAgentTest(execution_client)

        # Add a buy order
        agent.add_order(True, "IBM", 500, 98)

        # Check if the order was added correctly
        self.assertEqual(agent.orders, [(True, "IBM", 500, 98)])

    def test_execute_held_orders_buy(self):
        # Mock execution client
        execution_client = MagicMock()
        agent = LimitOrderAgentTest(execution_client)

        # Add a buy order and simulate price_tick
        agent.add_order(True, "IBM", 500, 98)
        agent.price_tick("IBM", 97)

        # Verify that execute_order method was called with the correct parameters
        execution_client.execute_order.assert_called_with("buy", "IBM", 500, 97)

    def test_execute_held_orders_sell(self):
        # Mock execution client
        execution_client = MagicMock()
        agent = LimitOrderAgentTest(execution_client)

        # Add a sell order and simulate price_tick
        agent.add_order(False, "IBM", 500, 102)
        agent.price_tick("IBM", 103)

        # Verify that execute_order method was called with the correct parameters
        execution_client.execute_order.assert_called_with("sell", "IBM", 500, 103)

if __name__ == "__main__":
    unittest.main()

