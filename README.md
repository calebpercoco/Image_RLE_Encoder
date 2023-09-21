# Image_RLE_Encoder
Attached is the Python script for encoding and decoding data using Run-Length Encoding (RLE) and
hexadecimal strings. Below is a detailed explanation of the code's functionality:

**count_runs(flatData)** calculates the number of runs in a flat data sequence. It iterates through the input 'flatData' and counts runs where consecutive elements are equal. 
If a run exceeds 15 consecutive elements, it's counted as multiple runs, then the function returns the total count of runs.

**to_hex_string(data)** converts a list of numerical data into a hexadecimal string representation. It processes each element in the 'data' list and converts it to its hexadecimal 
equivalent. It handles special cases for values 10 to 15, representing them as 'a' to 'f' in the resulting string.

**encode_rle(flat_data)** encodes data using RLE by taking 'flat_data' as input and produces a compressed RLE representation. It iterates through the data, identifies runs, and creates
a list 'code' that sotres the run lenth and value pairs.

**get_decoded_length(rle_data)** calculates the length of the decoded data from its RLE representation. It iterates through the RLE data and sums up the run lengths to determine the 
length of the decoded data.

**decode_rle(rle_data)** decodes RLE data back to its original form. It takes the RLE data as input and produced the decoded data. It repeats each value in the RLE data according to 
its run length.

**string_to_data(data_string)** converts a hexadecimal string 'data_string' into a list of integers.

**to_rle_string(rleData)** converts RLE data into a hexadecimal string representation. It processes the RLE data and creates a string in the formal 'run_length:value' for each run,
separated by colons.

**string_to_rle(rleString)** converts a string representation of RLE data into a list of integers, reversing the process of 'to_rle_string'.

The script is used to interactively perform various actions related to encoding, decoding, and displaying images or data using the RLE. It provides a menu-driven interface for users to 
load data, manipulate it, and display it in different formats. This code uses external functions and data from the 'console_gfx' module, which is not provided here. The functionality of 
that module is assumed to be related to displaying graphics on a console interface.
