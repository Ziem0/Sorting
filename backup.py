import csv
import os, sys
import time 

def read_data():
    """
    Parameters
    ----------
    amount_data : int

    Returns
    -------
    None
    """
    print('''
    1. Three millions
    2. One thousand\n''')
    try:
        user = int(input('choose option: '))
        if user == 1:
            if not os.path.isfile('data_to_sort/three_millions.csv'):
                raise FileNotFoundError('error')
            else:    
                amount_data = 'data_to_sort/three_millions.csv'
        elif user == 2:
            if not os.path.isfile('data_to_sort/one_thousand.csv'):
                raise FileNotFoundError('error')
            else:
                amount_data = 'data_to_sort/one_thousand.csv'

    except ValueError:
        print('error')

    finally:
        with open(amount_data, 'r') as f:
            reader = csv.reader(f)
            numbers = []
            for row in reader:
                numbers.append(int(row[0]))
            return numbers
            

def save_data(numbers):
    """
    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    None
    """
    with open('data_to_sort/sorted_numbers.csv', 'w') as f:
        writer = csv.writer(f)
        for number in numbers:
            writer.writerow([number])


def bubble_sort(numbers):
    """
    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    list of int

    """
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1],numbers[i]
                sorted = False
    return numbers

def insertion_sort(numbers):
    """
    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    list of int
    """
    for i in range(1, len(numbers)):
        while i != 0:
            if numbers[i]<numbers[i-1]:
                numbers[i], numbers[i-1] = numbers[i-1],numbers[i] 
            i -= 1
    return numbers

def sort_data(numbers, sort_type='bubble'):
    """
    Parameters
    ----------
    amount_data : int
    sort_type : string, optional

    Returns
    -------
    list of int
    """
    print('''
    0.compute
    1.bubble
    2.insertion\n''')
    
    user = (input('choose sort option: '))
    if user == '2':
        print(insertion_sort(numbers))
    elif user == "0":
        get_computing_time(numbers)
    else:
        print(bubble_sort(numbers))

def get_computing_time(numbers):   #, computing_type='import data'
    """
    Parameters
    ----------
    amount_data : int
    computing_type : string, optional

    Returns
    -------
    int
    """
    start = time.time()
    insertion_sort(numbers)
    end = time.time()
    result_insertion = end - start
    read_data()
    start = time.time()
    bubble_sort(numbers)
    end = time.time()
    result_bubble = end - start
    difference = (result_bubble-result_insertion)
    print(' bubble is:',result_bubble,'\n','insertion is:',result_insertion,'\n','differece:',difference)    

def print_computing_summary(result_bubble, result_insertion):
    """
    Parameters
    ----------
    computing_data : dict : { key : tuple of string, value : int }

    Returns
    -------
    None
    """


def main():
    numbers = read_data()
    sort_data(numbers)
    save_data(numbers)



if __name__ == "__main__":
    main()

