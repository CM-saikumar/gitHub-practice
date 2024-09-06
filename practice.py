def calculate_roi(net_profit, investment_cost):
    try:
        roi = (net_profit / investment_cost) * 100
        return roi
    except ZeroDivisionError:
        return "Investment cost cannot be zero."

net_profit = 50000  # Example net profit
investment_cost = 200000  # Example investment cost

roi = calculate_roi(net_profit, investment_cost)
print(f"ROI: {roi}%")