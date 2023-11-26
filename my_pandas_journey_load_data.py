#TASK:#TASK: Create a function which receive a StringIO with the content of a CSV as parameter and returns a Pandas Dataframe.
import pandas as pd
def my_pandas_journey_load_data(csv_content): 
    df=pd.read_csv(csv_content)
    return df 