import pandas as pd

def main():
    """
    main function that deals with the file input and
    running the program.
    """
    df = pd.DataFrame()
    with open('employees.dat') as infile:
        """
        1. only reading the non-commented lines.
        2. separating the record by ',' or ' ' into 3
            columns - employee number, first name and last name
        """
        df = pd.read_csv(infile, comment='#', header=None, names=['emp_number', 'emp_first_name', 'emp_last_name'], sep=" |,", engine='python')

    process_dataframe(df, 'emp_number', 'Processing by employee number...')
    print()
    process_dataframe(df, 'emp_last_name', 'Processing by last (family) Name...')


def process_dataframe(dataframe, sort_column, message):
    """
    Sort the given dataframe according to the column
    specified and print the records from the resulting
    dataframe along with the supplied message.

    :param pandas.DataFrame dataframe: Dataframe to process
    :param str sort_column: column by which to sort the dataframe
    :param str message: a message to show before printing the sorted data
    """
    sorted_df = dataframe.sort_values(by=[sort_column])
    print(message)
    for record in sorted_df.itertuples(index=False, name=None):
        print(str(record[0]) + ',' + record[1] + ' ' + record[2])


if __name__ == '__main__':
    main()
