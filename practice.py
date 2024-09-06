def calculate_roi(net_profit, investment_cost, partnership_interest=0):
    try:
        # Calculate the partner's share of the profit
        partners_share = net_profit * partnership_interest
        print(f"\nPartner's Share of Profit: {partnership_interest*100}% of {net_profit} = {partners_share:.2f} Rs.")
        
        # Adjust net profit by subtracting the partner's share
        adjusted_net_profit = net_profit - partners_share
        print(f"Adjusted Net Profit: {net_profit} - {partners_share:.2f} = {adjusted_net_profit:.2f} Rs.")
        
        # Calculate ROI
        roi = (adjusted_net_profit / investment_cost) * 100
        print(f"ROI Calculation: ({adjusted_net_profit:.2f} / {investment_cost}) * 100 = {roi:.2f}%")
        
        return roi
    except ZeroDivisionError:
        return "Investment cost cannot be zero."

# Get input values from the command line
net_profit = float(input("Enter the net profit (in Rs): "))
investment_cost = float(input("Enter the investment cost (in Rs): "))
partnership_interest = float(input("Enter the partnership interest (as a percentage): ")) / 100

# Calculate ROI based on user inputs
roi = calculate_roi(net_profit, investment_cost, partnership_interest)
print(f"Final ROI: {roi:.2f}%")
