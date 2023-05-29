import numpy as np

def mean_datasets(file_list):
    # Read the first CSV file to determine the dimensions
    first_file = file_list[0]
    data = np.loadtxt(first_file, delimiter=',')
    num_rows, num_cols = data.shape

    # Initialize the array to store the sum of each cell
    sum_array = np.zeros((num_rows, num_cols))

    # Iterate over the file list and accumulate the sum of each cell
    for file_name in file_list:
        data = np.loadtxt(file_name, delimiter=',')
        sum_array += data

    # Calculate the mean by dividing the sum by the number of files
    mean_array = sum_array / len(file_list)

    # Round the entries to one decimal place
    mean_array = np.round(mean_array, decimals=1)

    return mean_array
  
  if __name__ == "__main__":
    mean_datasets(['data1.csv', 'data2.csv', 'data3.csv'])
  """ 
  Output:
  array([[ 11.   11.9  13. ]
       [  9.5   6.8   9.4]
       [  7.2  11.1  12.5]
       [  8.8   7.3   9.2]
       [ 16.6  10.6  10.3]])
  """
