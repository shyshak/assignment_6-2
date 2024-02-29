Convertor application

This is a simple application that takes data from csv file and provides conversion to a single UOM.

SCV Structure can be find in input.csv. Data can be adjusted there.

To run the conversion:
1. From the folder location run main.py <conversion_type> where conversion_type is one of 
* c to convert temprerature to celcius, 
* f to convert temprerature to fahrenheit, 
* m to convert distance to meters, 
* ft to ocnvert distance to ft
Only one parameter at a time is allowed (for now)
2. See the output result in the out folder in a newly created file. For each conversion type a new file will be added fo visibility