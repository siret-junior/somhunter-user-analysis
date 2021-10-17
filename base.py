import pandas as pd
import numpy as np

def get_dataset_and_group_by_user(dataset="result_collection.csv"):
    return pd.read_csv(dataset).sort_values(['timestamp']).groupby('user')

def get_dataset_with_browsing_id_and_group_by_user(dataset="result_collection_browsing_id.csv"):
    return pd.read_csv(dataset).sort_values(['timestamp']).groupby('user')

def filter_out_mess(group):
    group = group[group['target_id'] != 0]
    group = group[group['target_id'] != 1088886]
    group = group[group['target_id'] != 171357]
    group = group[group['type'] != 'reset']
    group = group[group['type'] != 'issue']
    return group
