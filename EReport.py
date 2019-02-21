import pandas as pd

def main():
    df = pd.DataFrame()
    with open('employees.dat') as infile:
        df = pd.read_csv(infile, comment='#', header=None, names=['emp_number', 'emp_first_name', 'emp_last_name'], sep=" |,", engine='python')

    print(df.head())
    print("\nProcessing by employee number...")
    sorted_by_num = df.sort_values(by=['emp_number'])
    print(sorted_by_num)
    print("\nProcessing by last (family) Name...")
    sorted_by_last_name = df.sort_values(by=['emp_last_name']).to_csv(index=False, columns=None)
    print(sorted_by_last_name)


if __name__ == '__main__':
    main()
