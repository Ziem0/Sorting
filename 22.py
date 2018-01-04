import csv


def read_data(amount_data):
    """
   Parameters
   ----------
   amount_data : file with unsorted numbers
   Returns
   -------
   number_list : list with unsorted numbers
   """

    input_file = None
    numbers_list = []

    if amount_data == 1000:
        input_file = 'data_to_sort/one_thousand.csv'
    elif amount_data == 10000:
        input_file = 'data_to_sort/ten_thousand.csv'
    elif amount_data == 50000:
        input_file = 'data_to_sort/fifty_thousand.csv'
    elif amount_data == 100000:
        input_file = 'data_to_sort/one_hundred_thousand.csv'
    elif amount_data == 500000:
        input_file = 'data_to_sort/five_hundred_thousand.csv'
    elif amount_data == 1000000:
        input_file = 'data_to_sort/one_million.csv'
    elif amount_data == 3000000:
        input_file = 'data_to_sort/three_million.csv'

    with open(input_file, "r") as f:
        input_file = f.readlines()

        for line in input_file:
            numbers_list.append(int(line.strip()))
            
    return numbers_list


def save_data(numbers):
    """
   Parameters
   ----------
   numbers : list of integers
   Returns
   -------
   None
   """

    with open('data_to_sort/sorted_file.csv', 'w') as file:
        writer = csv.writer(file)
        for number in numbers:
            writer.writerow([number])


def bubble_sort(numbers):
    """
   Parameters
   ----------
   numbers : list of int
   Returns
   -------
   list with sorted integers
   """

    length = len(numbers) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if numbers[i] > numbers[i+1]:
                sorted = False
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    return numbers


def insertion_sort(numbers):
    """
    Parameters
    ----------
    numbers : list of int
    Returns
    -------
    list with sorted integers
    """
    
    for index in range(1, len(numbers)):
        while index > 0 and numbers[index] < numbers[index - 1]:
            numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
            index -= 1

    return numbers 


   # for i in range(1,len(numbers)):
        
    
    #     current_number = numbers[i]
    #     index = i 
         
    #     while((index > 0) and (numbers[index-1] > current_number)):
    #         numbers[index] = numbers[index-1]
    #         index = index-1
             
    #     if index != i:
    #         numbers[index] = current_number 
    
    # return numbers

def sort_data(amount_data, sort_type='bubble'):
    """
   Parameters
   ----------
   sort_type : string, optional
   amount_data : int
   Returns
   -------
   list with sorted integers
   """

    if sort_type == 'bubble':
        print(bubble_sort(amount_data))
    elif sort_type == 'insertion':
        print(insertion_sort(amount_data))


def get_computing_time(amount_data, computing_type='import data'):
    """
    Parameters
    ----------
    amount_data : int
    computing_type : string, optional

    Returns
    -------
    int
    """
    pass


def print_computing_summary(computing_data):
    """
    Parameters
    ----------
    computing_data : dict : { key : tuple of string, value : int }

    Returns
    -------
    None
    """
    pass


def main():
    
    amount_data = int(input('Choose an amount of data: '))
    sort_type = input('What type of sort do you prefer(bubble is default): ')
    numbers_list = read_data(amount_data)
    sort_data(numbers_list)
    numbers = bubble_sort(numbers_list)
    numbers = insertion_sort(numbers_list)
    save_data(numbers)



if __name__ == '__main__':
    main()