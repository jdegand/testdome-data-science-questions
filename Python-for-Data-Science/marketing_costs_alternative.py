import numpy as np
from sklearn.linear_model import TheilSenRegressor, LinearRegression

class MarketingCosts:
    """
    A class to predict required marketing expenditure using Theil-Sen regression.

    Idea came from: https://gist.github.com/mfakbar/f97949299171c75e868a37f3f578fa54

    I looked for alternative solutions after dealing with the floating point errors.

    Theil-Sen regression can throw exceptions when there is insufficient data and I think this is a
    potential reason why exceptions are thrown during TestDome testing.
    """

    @staticmethod
    def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
        """
        :param marketing_expenditure: (list) Expenditure for each previous campaign.
        :param units_sold: (list) Number of units sold for each previous campaign.
        :param desired_units_sold: (int) Target number of units to sell in the new campaign.
        :returns: (float) Required amount of money to be invested.
        """
        try:
            # Validate input data
            if not marketing_expenditure or not units_sold:
                raise ValueError("Input lists cannot be empty.")
            if len(marketing_expenditure) != len(units_sold):
                raise ValueError("Mismatch between marketing_expenditure and units_sold lengths.")

            # Convert lists to NumPy arrays and reshape for sklearn
            units_sold = np.array(units_sold).reshape(-1, 1)
            marketing_expenditure = np.array(marketing_expenditure)

            # Initialize and train the Theil-Sen regressor
            lm = TheilSenRegressor(max_subpopulation=10)
            lm.fit(units_sold, marketing_expenditure)

            # Predict required marketing expenditure for desired units sold
            predicted_expenditure = lm.predict(np.array([[desired_units_sold]]))

        except Exception as e:
            print(f"Warning: Theil-Sen failed due to '{e}', switching to Linear Regression.")

            # Fallback to Linear Regression
            lm = LinearRegression()
            lm.fit(units_sold, marketing_expenditure)
            predicted_expenditure = lm.predict(np.array([[desired_units_sold]]))

        return round(predicted_expenditure.item(), 2)  # Convert to float and round for cleaner output

# Example usage
print(MarketingCosts.desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))  # Expected output: 250000.0
