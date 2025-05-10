import pandas as pd
import numpy as np

def login_table(id_name_verified, id_password):
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.   
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password.
    :returns: (None) The function should modify id_name_verified DataFrame in-place. 
              It should not return anything.
    """   
    # Column names are case-sensitive in Python.
    id_name_verified.drop(columns=["Verified"], inplace=True)

    # Convert NumPy array to DataFrame and rename columns
    id_password_df = pd.DataFrame(id_password, columns=["Id", "Password"])

    # Merge DataFrames on 'Id'
    merged_df = id_name_verified.merge(id_password_df, on="Id")

    # This prints the correct result, but the tests do not pass. 
    # This solution is very similar to my R solution.
    print(merged_df)

# Example usage
id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122]], np.int32)

login_table(id_name_verified, id_password)