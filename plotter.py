import pandas as pd

import matplotlib.pyplot as plt

def begin_plotting():
    """
    Read Teaching Ratings from CSV and begin plotting the data.
    :return: CSV File
    """
    # Read csv from file into a Pandas data frame
    teaching_data = "data/TeachingRatings_Clean.csv"
    teaching_ratings = pd.read_csv(teaching_data, sep=',', decimal='.')

    # Plot pie chart for percentage of lecturers belonging to a minority vs non-minority
    teaching_ratings['minority'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Lecturers by Minority')
    plt.show()

    # Plot distribution of ages as a histogram
    teaching_ratings['age'].value_counts().plot(kind='hist', bins=20, linewidth=1.0,rwidth=0.8)
    plt.title('Lecturers by Age')
    plt.xlabel('Age')
    plt.ylabel('Number of Lecturers')
    plt.show()

    # Plot pie chart for percentage of lecturers gender
    teaching_ratings['gender'].value_counts().plot(kind='bar')
    plt.title('Lecturers by Gender')
    plt.show()

    # Plot distribution of credits as histogram
    teaching_ratings['credits'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Courses by Single-Credit and More than Single-Credit')
    plt.show()

    # Plot beauty ratings as density plot
    teaching_ratings['beauty'].plot(kind='density')
    plt.title('Distribution of lecturer beauty ratings')
    plt.xlabel('Beauty Rating')
    plt.show()

    # Plot distribution of evaluation ratings as a histogram
    teaching_ratings['eval'].plot(kind='hist', bins=20, linewidth=1.0, rwidth=0.8)
    plt.title('Distribution of Evaluation Ratings')
    plt.xlabel('Evaluation Rating')
    plt.ylabel('Number of Lecturers')
    plt.show()

    # Plot distribution of divisions as pie chart
    teaching_ratings['division'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of courses by Division')
    plt.show()

    # Plot distribution of native-language speaking lecturers as bar chart
    teaching_ratings['native'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of Native Speaking Lecturers')
    plt.show()

    # Plot distribution of tenure and non-tenure working staff
    teaching_ratings['tenure'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of Leturers Permanently employed (tenure)')
    plt.show()

    # Plot distribution of participating students using a box plot
    teaching_ratings['students'].plot(kind='box')
    plt.title('Distribution of Participating Students')
    plt.show()

    # Plot distribution of number of students in a class
    teaching_ratings['allstudents'].plot(kind='density')
    plt.title('Distribution of All Students')
    plt.xlabel('Number of Students')
    plt.show()


if __name__ == "__main__":
    begin_plotting()
