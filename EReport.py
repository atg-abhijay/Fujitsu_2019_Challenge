import pandas as pd

def main():
    df = pd.DataFrame()
    with open('employees.dat') as infile:
        df = pd.read_csv(infile, comment='#', header=None, names=['emp_number', 'emp_first_name', 'emp_last_name'], sep=" |,", engine='python')

    process_dataframe(df, 'emp_number', 'Processing by employee number...')
    print()
    process_dataframe(df, 'emp_last_name', 'Processing by last (family) Name...')


def process_dataframe(dataframe, sort_column, message):
    sorted_df = dataframe.sort_values(by=[sort_column])
    print(message)
    for record in sorted_df.itertuples(index=False, name=None):
        print(str(record[0]) + ',' + record[1] + ' ' + record[2])


if __name__ == '__main__':
    main()
