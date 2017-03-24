import pandas as pd
from include.Header import *

# Create a new header object for referencing
header = Header()


def convert_type(data_frame, type):
    """
    Converts a data frame based on a passed in type.
    Assumes sanitised column as per pre-conversion cleaning

    :param data_frame: data frame column to convert
    :param type: data type to convert
    :return: converted data frame
    """
    if type == 'numeric_int':
        data_frame = data_frame.astype('int64')
    elif type == 'numeric_float':
        data_frame = data_frame.astype('float64')
    elif type == 'string':
        data_frame = data_frame.astype('str')

    return data_frame


def fill_na_mean(data_frame):
    """
    Populates a data frame's NaN entries as the column-wise mean

    :param data_frame: data frame column to populate
    :return: populated data frame
    """
    data_frame.fillna((data_frame.mean()), inplace=True)
    return data_frame


def clean_data(data_frame):
    for key, value in header.header.iteritems():

        data_type = str(data_frame[key].dtype)
        old_type = header.type_conversions[data_type]
        # Check if the data frame is numeric.
        if old_type == 'numeric_float' or 'numeric_int':

            # Check if there are NaN values, and replace with the column-wise mean
            if data_frame[key].isnull().values.any():
                data_frame[key] = fill_na_mean(data_frame[key])

        # Check for type mismatches
        if data_type != value:
            new_type = header.type_conversions[value]
            data_frame[key] = convert_type(data_frame[key], new_type)

        # Convert all string-wise columns to lowercase and strip
        string_cols = data_frame.loc[:, data_frame.dtypes == object]
        for col in string_cols:
            data_frame[col] = data_frame[col].str.lower()
            data_frame[col] = data_frame[col].str.strip()

        #

    return data_frame


def sanitise():
    # Read csv from file into a Pandas data frame
    teaching_data = "data/TeachingRatings.csv"
    teaching_ratings = pd.read_csv(teaching_data, sep=',', decimal='.')

    teaching_ratings = clean_data(teaching_ratings)

    # print teaching_ratings['gender'].value_counts()
    print teaching_ratings['gender'].value_counts()

if __name__ == "__main__":
    sanitise()
