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

def selection_sort(arr, direction = "vzestupně"):
    n = len(arr)
    for i in range(n-1):
        if direction == "vzestupně":
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if direction == "sestupně":
            max_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[max_idx]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            raise ValueError("Neplatny smer razeni")
    return arr

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
        arr[j + 1] = key

def main():
    #pass
    file_name = "numbers.csv"
    data = read_data(file_name)
    print(data)


if __name__ == '__main__':
    main()
