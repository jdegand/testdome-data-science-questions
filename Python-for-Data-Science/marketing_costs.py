import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
    """
    :param marketing_expenditure: (list) A list of integers with the expenditure for each previous campaign.
    :param units_sold: (list) A list of integers with the number of units sold for each previous campaign.
    :param desired_units_sold: (integer) Target number of units to sell in the new campaign.
    :returns: (float) Required amount of money to be invested.
    """
    # Convert lists to NumPy arrays
    X = np.array(units_sold).reshape(-1, 1)  # Feature (units sold)
    y = np.array(marketing_expenditure)  # Target (marketing expenditure)

    # Normalize input features using MinMaxScaler
    scaler = MinMaxScaler()
    x_scaled = scaler.fit_transform(X)

    # Train linear regression model
    model = LinearRegression()
    model.fit(x_scaled, y)

    # Scale the desired units sold
    desired_scaled = scaler.transform(np.array([[desired_units_sold]]))

    # Predict required marketing expenditure
    predicted_expenditure = model.predict(desired_scaled)

    return predicted_expenditure.item()

# Example usage
print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))  # Expected output: 250000.0
