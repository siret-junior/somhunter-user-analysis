import pandas as pd
import numpy as np

# script for creating result_collection with browsing ID

if __name__ == "__main__":
    data = pd.read_csv('result_collection.csv').sort_values(['timestamp'])
    data.insert(0, "browsing_id", np.nan)
    data_grouped = data.groupby('user')
    for username, group in data_grouped:
        browsing_id_it = -1
        print(username)
        for index, row in group.iterrows():
            if row['type'] == "reset" or row['type'] == 'text':
                browsing_id_it += 1
            data.at[index, 'browsing_id'] = browsing_id_it

    data.to_csv('result_collection_browsing_id.csv', index=False)





