""" Task Details: Reading data from file and filtering it using map and filter function
and then sorting the data according to age."""


# Formatting data
def format_data(s):
    s = s[:-1]
    op = s.split(',')
    return op


# Reading data from text file
def read_data(file_name):
    try:
        with open(file_name, 'r') as initial_data:
            full_data = initial_data.readlines()
            return full_data
    except:
        print("Exception in read_data function")


# Format data using map function
def map_data(data):
    try:
        data_list = list(map(format_data, data))
        return data_list
    except:
        print("Exception in map_data function")


# Removing people under age 18
def filter_data(full_data):
    try:
        filtered_data = list(filter(lambda x: int(x[-1]) > 17, full_data[1:]))
        return [full_data[0]] + filtered_data
    except:
        print("Exception in filter_data function")


try:
    data = read_data("data.txt")
    mapped_data = map_data(data)

    # Removing header (id, name, age) for easy manipulation of data
    headers = [mapped_data[0]]

    filtered_data = filter_data(mapped_data[1:])

    # Sorting the data according to age
    filtered_data.sort(key=lambda x: int(x[-1]))

    # Attaching header to final data
    final_data = headers + filtered_data

    # Creating new file and writing the output to that file
    with open("output.txt", 'a') as file:
        for lst in final_data:
            s = ",".join(lst)
            file.write(s + "\n")
except:
    print("Exception in main code")
finally:
    print("Data Extraction Done")
