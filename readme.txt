# Assignment 1: Data Cleaning and Summarising
# Max Yendall : S3436993

#### Table of Contents

1. [Assumptions]- Asssumptions needing to be met to ensure code will execute
2. [Explanation of Files] - Explanation of all included files in this package
3. [Running The Scripts]
    * [Running task1_parser.py]
    * [Running task2_plotter.py]

### Content

1. [Assumptions]:
    Classes:
    This Python application uses an Object-Oriented Paradigm with the inclusion of a Header class for table look-ups.
    This file MUST BE present in order for the scripts to execute properly, as look-up tables are imported for the
    parsing functions to reference. All scripts will work if kept in the same directory.

    Typo Checking:
    Instead of hard-coding typo checking, a SequenceMatching library has been used to find the similarity between
    terms, using a similar flavour of algorithm to the Gestalt Pattern Matching algorithm. This is also explained in
    the report if anything is not clear from the code

    CSV Files:
    This Python application will read and write CSV files from the root directory ONLY. There is no user input and will
    only read a file specifically named "TeachingRatings.csv" and it must be located in the root directory of this
    application. If it is not present, the Python application will fail to run.

    The parser will output a new CSV file called "TeachingRatings_Clean.csv" to the root directory, which will be
    read into memory in the plotting script.

    iPython Execution:
    This Python application is written as standard Python scripts, which can be executed from an iPython environment
    using the %run command.

2. [Explanation of Files]:
    Header.py:
        Class header for table look-ups. Essential for the functionality of task1_parser.py and task2_plotter.py
    task1_parser.py:
        Task 1 script which reads the TeachingRatings.csv file, sanitises the data and outputs to a new CSV
    task2_plotter.py:
        Task 2 script which reads the TeachingRatings_Clean.csv file and plots data as per specifications

3. [Running the scripts]:
    Both scripts are built to be run sequentially. You must run task1_parser.py BEFORE running task2_plotter.py,
    as the parser will output a new, cleaned CSV file for reference in the plotter script.

    * [Running task1_parser.py:
        This Python script will run when calling the following command from an iPython environment:
            %run task1_parser.py
    * [Running task2_plotter.py:
        This Python script will run when calling the following command from an iPython environment:
            %run task2_plotter.py

