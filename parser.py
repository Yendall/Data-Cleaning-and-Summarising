import pandas as pd
import numpy as np
from difflib import SequenceMatcher
from include.Header import *

# Create a new header object for referencing
header = Header()


def similar(typo, word):
    """
    Returns similarity as a percentage between a typo sequence and english word
    :param typo: Mispelled word or sequence of words
    :param word: English word in lookup header
    :return: Similarity percentage
    """
    return SequenceMatcher(None, typo, word).ratio()


def check_typos(data_frame, key):
    """
    Takes data set data frame and column key and checks for typos using sequence matching
    :param data_frame: Entire data frame
    :param key: The string-based column which involves typos
    :return: Cleaned data frame with corrected typos from estimation
    """
    # All columns in this dataset have two possible values (assumed)
    fir_val = header.typo_lookup[key][0]
    sec_val = header.typo_lookup[key][1]
    # Check if the data frame column has any values that aren't equal to the first value (this is pretty much always
    # True)
    fir_check = data_frame[key] != fir_val
    # Check if the data frame column has any values that aren't equal to the second value (this is pretty much always
    # True)
    sec_check = data_frame[key] != sec_val
    # Create a logical mask that combines the two statements above, to find values outside of the columns scope
    mask = data_frame[key][fir_check & sec_check].values
    # Declare similarity and set as 0 initially
    similarity = 0
    # Declare pointer to track where we are in the mask
    pointer = 0
    most_sim_val = ""

    for data in mask:
        # Compare expected values to typo value and calculate similarity
        for vals in header.typo_lookup[key]:
            # print 'checking value: ', data, ' against: ', vals
            new_sim = similar(data, vals)
            # Set the highest similarity and apply to mask
            if new_sim > similarity:
                most_sim_val = vals
                similarity = new_sim
        similarity = 0
        mask[pointer] = most_sim_val
        pointer += 1

    # Apply new mask to data frame and return
    data_frame[key][fir_check & sec_check] = mask

    return data_frame


def check_students(data_frame):
    """
    Checks that number of students is less than all students. If they are inverted, students are converted to 60%
    of the all-students column value
    :param data_frame: Whole data frame
    :return: Students and Allstudents data frame corrected
    """
    # Locate anomalies and replace with 60% of the allstudents count
    mask = data_frame.loc[(data_frame['students'] > data_frame['allstudents'])]
    # Replace the anomalies with suitable values
    data_frame.loc[(data_frame['students'] > data_frame['allstudents']), 'students'] = 0.60 * mask['allstudents']
    # Convert the data frame back to integer
    data_frame['students'] = convert_type(data_frame['students'], 'numeric_int')

    return data_frame


def check_range(data_frame, key):
    """
    Converts out of range values in a column to the column-wise mean
    Assumes integer/float based column

    :param data_frame: the entire data frame
    :param key: the column which we're looking for anomalies
    :return: clean data frame
    """
    # Fetch upper, lower and rounding values from hash table
    lower_bound = header.range_lookup[key]['lower']
    upper_bound = header.range_lookup[key]['upper']
    round_val = header.range_lookup[key]['round']
    # If the key is age, force cast as Integer for consistency
    if key == 'age':
        mean = int(np.round(data_frame[key].mean(), round_val))
    else:
        mean = np.round(data_frame[key].mean(), round_val)
    # Locate anomalies and replace with the rounded column-wise mean
    data_frame.loc[(data_frame[key] < lower_bound) | (data_frame[key] > upper_bound), key] = mean

    return data_frame


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
    """

    :param data_frame:
    :return:
    """
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

        # Check for typos
        if key in string_cols:
            if key != 'prof':
                data_frame = check_typos(data_frame, key)

        # Check for out-of-range values
        if key in header.range_lookup:
            data_frame = check_range(data_frame, key)

    # Check that students are less than all students (final range check)
    check_students(data_frame)

    return data_frame


def sanitise():
    """
    Read Teaching Ratings from CSV and begin sanitising the data. Once cleaned, write back to file as CSV
    :return: CSV File
    """
    # Read csv from file into a Pandas data frame
    teaching_data = "data/TeachingRatings.csv"
    teaching_ratings = pd.read_csv(teaching_data, sep=',', decimal='.')
    # Clean the data
    teaching_ratings = clean_data(teaching_ratings)
    # Write new csv file
    teaching_ratings.to_csv('data/TeachingRatings_Clean.csv', sep=',', index=False)

if __name__ == "__main__":
    # Override warning
    pd.options.mode.chained_assignment = None  # default='warn'
    sanitise()
