import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def begin_plotting():
    """
    Read Teaching Ratings from CSV and begin plotting the data.
    :return: CSV File
    """
    # Read csv from file into a Pandas data frame
    teaching_data = "data/TeachingRatings_Clean.csv"
    teaching_ratings = pd.read_csv(teaching_data, sep=',', decimal='.')

    # Plot pie chart for percentage of lecturers gender
    teaching_ratings['gender'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of Lecturers by Gender')
    plt.show()

    # Plot distribution of ages as a histogram
    teaching_ratings['age'].value_counts().plot(kind='hist', bins=20, linewidth=4.0,rwidth=0.8)
    plt.title('Distribution of Lecturers by Age')
    plt.xlabel('Age')
    plt.ylabel('Number of Lecturers')
    plt.show()

    # Plot pie chart for percentage of lecturers belonging to a minority vs non-minority
    teaching_ratings['minority'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of Lecturers by Minority')
    plt.show()

    # Plot distribution of credits as histogram
    teaching_ratings['credits'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of courses by Single-Credit and More than Single-Credit')
    plt.show()

    # Plot beauty ratings as box plot
    teaching_ratings['beauty'].plot(kind='density')
    plt.title('Distribution of lecturer beauty ratings')
    plt.xlabel('Beauty Rating')
    plt.show()

    # Plot distribution of evaluation ratings as a histogram
    teaching_ratings['eval'].value_counts().plot(kind='hist', bins=20, linewidth=4.0, rwidth=0.8)
    plt.title('Distribution of Lecturers by Age')
    plt.xlabel('Age')
    plt.ylabel('Number of Lecturers')
    plt.show()

if __name__ == "__main__":
    begin_plotting()
