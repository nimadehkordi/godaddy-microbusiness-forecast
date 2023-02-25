# imports
import tensorflow as tf
from tfx import v1 as tfx

# TFX libraries
import tensorflow_data_validation as tfdv
import tensorflow_transform as tft
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext

# For performing feature selection
from sklearn.feature_selection import SelectKBest, f_classif

# For feature visualization
import matplotlib.pyplot as plt 
import seaborn as sns

# Utilities
from tensorflow.python.lib.io import file_io
from tensorflow_metadata.proto.v0 import schema_pb2
from google.protobuf.json_format import MessageToDict
from  tfx.proto import example_gen_pb2
from tfx.types import standard_artifacts
from tensorflow_transform.tf_metadata import dataset_metadata, schema_utils
import tensorflow_transform.beam as tft_beam
import os
import pprint
import tempfile
import pandas as pd

# To ignore warnings from TF
tf.get_logger().setLevel('ERROR')

# For formatting print statements
pp = pprint.PrettyPrinter()

FEATURES_TO_REMOVE = ["row_id", "first_day_of_month"]
FEATURES_CENSUS = ['pct_bb', 'pct_college', 'pct_foreign_born', 'pct_it_workers', 'median_hh_inc']

def _pivot_census(census_df, category):
    """This function prepares and melts the census dataframe"""
    
    df_cols = [col for col in census_df.columns if category in col]  # select relevant columns
    df = census_df[df_cols+['cfips']] # subset the dataframe
    # renaming columns
    df_cols = [col[-4:] for col in df.drop('cfips', axis=1).columns]
    df.columns = df_cols+['cfips']
    # melting a dataframe
    df = pd.melt(df, id_vars='cfips', value_vars=['2017','2018','2019','2020','2021'],
                    var_name='year', value_name=category).sort_values('cfips').reset_index(drop=True)
    return df

def _pivot_census_all(census_df):
    for category in FEATURES_CENSUS:
        df = _pivot_census(census_df, category)
        if category == FEATURES_CENSUS[0]:
            census_df = df
        else:
            census_df = pd.merge(census_df, df, on=['cfips','year'])
    census_df.sort_values(['cfips','year'], inplace=True)
    census_df['year'] = census_df['year'].astype('int')
    return census_df

def preprocessing_fn(inputs, training=True, census_df=None):
    """Preprocess input columns into transformed columns."""

    outputs = inputs.copy()

    # Get year and month from first_day_of_month
    outputs['year'] = tf.strings.to_number(tf.strings.substr(outputs['first_day_of_month'], 0, 4), out_type=tf.dtypes.int32)
    outputs['month'] = tf.strings.to_number(tf.strings.substr(outputs['first_day_of_month'], 5, 2), out_type=tf.dtypes.int32)

    # Merge census data
    census_df = _pivot_census_all(census_df)
    outputs = pd.merge(outputs, census_df, on=['cfips','year'])

    # Filter redundant features
    for key in FEATURES_TO_REMOVE:
        del outputs[key]

    return outputs