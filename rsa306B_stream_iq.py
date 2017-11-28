"""

Stream IQ data to file at several center frequency values.

Syntax
>>python rsa_306B_stream_iq.py <acquisition_time> <center_frequency_list> <ref_level> <bandwidth> <save_path>

acquisition_time - acquisition time in milliseconds at each center frequency
center_frequency_list - comma separated list of center frequency values in units of Hz
ref_level - reference level in db
bandwidth - bandwidth in units of Hz; max value is 40e6 for the RSA306B
save_path - save path

Example usage:
>>python rsa_306B_stream_iq.py 75000 2.42e9, -20 40e6 C:\Users\jkwong\Documents\data\tek_python\20171115

John Kwong


OLD readme

Tektronix RSA_API Example
Author: Morgan Allison
Date created: 6/15
Date edited: 5/17
Windows 7 64-bit
RSA API version 3.9.0029
Python 3.6.0 64-bit (Anaconda 4.3.0)
NumPy 1.11.3, MatPlotLib 2.0.0
Download Anaconda: http://continuum.io/downloads
Anaconda includes NumPy and MatPlotLib
Download the RSA_API: http://www.tek.com/model/rsa306-software
Download the RSA_API Documentation:
http://www.tek.com/spectrum-analyzer/rsa306-manual-6

YOU WILL NEED TO REFERENCE THE API DOCUMENTATION
"""

from RSA_API import *
from rsa_api_full_example import iq_stream_time_limit

import ast, sys, os

# C:\Tektronix\RSA_API\lib\x64 needs to be added to the
# PATH system environment variable
# chdir("C:\\Tektronix\\RSA_API\\lib\\x64")
# rsa = cdll.LoadLibrary("RSA_API.dll")
# rsa = cdll.LoadLibrary(os.path.join("C:\\Tektronix\\RSA_API\\lib\\x64", "RSA_API.dll"))

dir_path = os.path.dirname(os.path.realpath(__file__))
dll_fullfilename = os.path.join(dir_path, "RSA_API.dll")
print(os.path.exists(dll_fullfilename))
rsa = cdll.LoadLibrary(dll_fullfilename)

def main(time_limit, center_frequency_list, ref_level, bandwidth, save_path):

    # uncomment the example you'd like to run
    # spectrum_example()
    # block_iq_example()
    # dpx_example()
    # if_stream_example()
    for center_frequency_index, center_frequency in enumerate(center_frequency_list):
        print('{}, f_center = {}'.format(center_frequency_index, center_frequency))
        iq_stream_time_limit(duration=time_limit,center_frequency=center_frequency,refLevel=ref_level,bandwidth=bandwidth,save_path=save_path)

if __name__ == '__main__':

    time_limit = int(ast.literal_eval(sys.argv[1]))
    center_frequency_list = ast.literal_eval(sys.argv[2])
    ref_level = ast.literal_eval(sys.argv[3])
    bandwidth = ast.literal_eval(sys.argv[4])
    save_path = sys.argv[5]
    main(time_limit,center_frequency_list,ref_level,bandwidth,save_path)
