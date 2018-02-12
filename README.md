# Drifttube-practicalCourse
Program skeleton for analyzing FADC read data from a drift tube particle detector. For teaching purposes only.
Note that this software is NOT a complete analysis tool.

# Purpose
The software provided in this repository was designed for teaching purposes only.
It is used in the particle physics internship for undergraduate students at the university of Hamburg for a teaching experiment regarding the properties of gaseous particle detectors.

# Data format
The raw data is read from a binary file. Its contents are as follows:
1.) First 8 bytes: Number of events in the binary file
2.) 800 * 64 bits: double precision floating point numbers containing the voltage for each of the 800 FADC bins
3.) Second point repeated as many times as coded in the file's first 8 bytes.

# Contact
For a fully implemented version of this software contact me via mail


