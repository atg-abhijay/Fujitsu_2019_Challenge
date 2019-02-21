import pandas as pd

def main():
    df = pd.DataFrame()
    with open('employees.dat') as infile:
        df = pd.read_csv(infile, comment='#', header=None, names=['emp_number', 'emp_first_name', 'emp_last_name'], sep=" |,", engine='python')

    sorted_by_num = df.sort_values(by=['emp_number'])
    print_in_format("Processing by employee number...", sorted_by_num)
    print()
    sorted_by_last_name = df.sort_values(by=['emp_last_name'])
    print_in_format("Processing by last (family) Name...", sorted_by_last_name)


def print_in_format(message, dataframe):
    print(message)
    for record in dataframe.itertuples(index=False, name=None):
        print(str(record[0]) + ',' + record[1] + ' ' + record[2])


if __name__ == '__main__':
    main()
