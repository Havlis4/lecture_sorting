import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    import csv
    data = {}
    with open (file_path, mode= "r", newline= "") as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)
        for header in headers:
            data[header] = []

        for row in csv_reader:
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))
    return data
def main():
    #pass
    file_name = "numbers.csv"
    data = read_data(file_name)
    print(data)


if __name__ == '__main__':
    main()
