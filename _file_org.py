""" Organize project
    * create project directory
    * save data to file
"""
#author tjdim, Cambridge MA 2018
import os
import datetime

def return_dir(path):
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



def save_dat_to_file(keyword, data, tmp_data=True):
    """ Appends text data to an existing file or adds data to a new .txt file

        Args
        ----
            location (str) : directory name
            keyword (str) : use keyword to create file name
            data (str) : save source code to file

        Output
        -------
            creates txt file with data
    """
    location = return_dir('dat')
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
    with open(file_loc, file_mode) as txtfile:
        txtfile.write(data)
    outfile = open(file_loc, 'w')
    outfile.write(str(data))
    outfile.close()
