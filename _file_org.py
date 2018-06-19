"""Organize project
    * create project directory if it doesn't exist
    * save data to file
"""
#tjdim, Cambridge MA 2018
import os
import datetime
import csv

def _return_dir(path):
    """Returns directory and creates dir if it doesn't exist
       Args
       ----
           path (str) : name of directory (folder name)
       Returns
       -------
           path (str): name of directory (folder name)
           creates project directory if it does not already exist
    """
    #creates new directory
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print "Directory already token. All changes will be added to existing directory."
    return path



def _save_dat_to_file(keyword, data, tmp_data=True, csv_file=False):
    """Appends text data to an existing file or creates a file and adds data

        Args
        ----
            keyword (str) : use keyword to create file name
            data (str) : save source code to file

        Calls
        -----
            return_dir (function)

        Returns
        -------
            creates txt file with data
    """
    location = _return_dir('dat')
    if csv_file:
        file_extension = '.csv'
    else:
        file_extension = '.txt'

    time_stamp = '{:%Y_%m_%d_%H_%M_%s}'.format(datetime.datetime.now())
    #if temporary data add time stamp to file name
    if tmp_data:
        file_name = keyword + ' ' + time_stamp + file_extension
    else:
        file_name = keyword + file_extension
    file_loc = location  + '/' + file_name
    #append to file if file exists
    if os.path.exists(file_loc):
        file_mode = 'a'
    else:
        file_mode = 'w'
    if type(data) == list:
        #with open automatically closes file outside 'with' block
        with open(file_loc, file_mode) as outfile:
            if csv_file:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerow(data)
            else:
                for item in data:
                    outfile.write(item)
                    outfile.write('\n')
