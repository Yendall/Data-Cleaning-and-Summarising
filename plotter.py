import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt


def plot_scatter_matrix(data):
    """
    Scatter Matrix for all numeric data in the data frame
    :param data: Entire data frame
    :return: XMing Plot
    """
    # Create a numeric mask
    numeric_mask = data.select_dtypes(include=['float64', 'int64'])
    # Delete prof as it is not numeric
    del numeric_mask['prof']
    # Plot the scatter matrix
    scatter_matrix(numeric_mask, alpha=0.2, figsize=(16, 16), diagonal='hist')
    plt.show()

def basic_plot(data):
    """
    Single-Column basic plots for visualising different fields
    :param data: Entire data frame
    :return: XMing Plots
    """
    # Plot pie chart for percentage of lecturers belonging to a minority vs non-minority
    data['minority'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Lecturers by Minority')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of ages as a histogram
    data['age'].plot(kind='hist', bins=20, linewidth=1.0, rwidth=0.8)
    plt.title('Lecturers by Age')
    plt.xlabel('Age')
    plt.ylabel('Number of Lecturers')
    plt.legend(shadow=True)
    plt.show()

    # Plot pie chart for percentage of lecturers gender
    data['gender'].value_counts().plot(kind='bar')
    plt.title('Lecturers by Gender')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of credits as histogram
    data['credits'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Courses by Single-Credit and More than Single-Credit')
    plt.legend(shadow=True)
    plt.show()

    # Plot beauty ratings as density plot
    data['beauty'].plot(kind='density')
    plt.title('Distribution of lecturer beauty ratings')
    plt.xlabel('Beauty Rating')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of evaluation ratings as a histogram
    data['eval'].plot(kind='hist', bins=20, linewidth=1.0, rwidth=0.8)
    plt.title('Distribution of Evaluation Ratings')
    plt.xlabel('Evaluation Rating')
    plt.ylabel('Number of Lecturers')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of divisions as pie chart
    data['division'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of courses by Division')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of native-language speaking lecturers as bar chart
    data['native'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of Native Speaking Lecturers')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of tenure and non-tenure working staff
    data['tenure'].value_counts().plot(kind='pie', autopct='%.2f')
    plt.title('Percentage of Leturers Permanently employed (tenure)')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of participating students using a box plot
    data['students'].plot(kind='box')
    plt.title('Distribution of Participating Students')
    plt.legend(shadow=True)
    plt.show()

    # Plot distribution of number of students in a class
    data['allstudents'].plot(kind='density')
    plt.title('Distribution of All Students')
    plt.xlabel('Number of Students')
    plt.legend(shadow=True)
    plt.show()


def relationship_plots(data):
    """
    Column specific plots based on hypothesis
    :param data: Entire data frame
    :return: XMing Plots
    """
    # Is there a relation between course evaluation scores and gender?
    data.boxplot(column='eval', by='gender')
    plt.title('Course Evaluation Scores by Gender')
    plt.ylabel('Evaluation Score')
    plt.show()

    # Is there a relationship between beauty perception and gender?
    data.boxplot(column='beauty', by='gender')
    plt.title('Beauty Rating by Gender')
    plt.ylabel('Beauty Rating')
    plt.show()

    # Is there a relationship between minorities and native language speakers?
    native_counts = data['native'].value_counts()

    mask_native = data['native'] == 'yes'
    mask_non_native = data['native'] == 'no'

    native_minority = data.loc[mask_native, 'minority'].value_counts()
    non_native_minority = data.loc[mask_non_native, 'minority'].value_counts()

    prop = [native_minority[1] / float(native_counts['yes']), non_native_minority[1] / float(native_counts['no'])]
    plt.bar(range(2), prop, color='g', align='center')
    plt.xticks(range(2), ['native', 'non-native'])
    plt.xlabel('Native Speaker')
    plt.ylabel('Minority Proportion')
    plt.show()


def begin_plotting():
    """
    Read Teaching Ratings from CSV and begin plotting the data.
    :return: XMing Plots
    """
    # Read csv from file into a Pandas data frame
    teaching_data = "data/TeachingRatings_Clean.csv"
    teaching_ratings = pd.read_csv(teaching_data, sep=',', decimal='.')
    # Plot basic and advanced plots
    basic_plot(teaching_ratings)
    relationship_plots(teaching_ratings)
    plot_scatter_matrix(teaching_ratings)


if __name__ == "__main__":
    begin_plotting()
