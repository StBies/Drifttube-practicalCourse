# Drifttube-practicalCourse
Program skeleton for analyzing FADC read data from a drift tube particle detector. For teaching purposes only.
Note that this software is NOT a complete analysis tool.

# Purpose
The software provided in this repository was designed for teaching purposes only.
It is used in the particle physics internship for undergraduate students at the university of Hamburg for a teaching experiment regarding the properties of gaseous particle detectors.

The aim is to teach students the importance as well as implementation basics of automated analysis for large sets of data. In the laboratory course, students learn about basic principles of particle detection in gaseous detectors and use NIM hardware.

After understanding signal discrimination, triggering and timing, data is recorded using a Flash Analog to digital converter (FADC) and the data read using it is analyzed in software.

The principles learned in the lab should then be applied to digitized waveforms. Therefore, algorithms need to be developed and implemented, in particular for a ground level calibration and the calculation of a drift time. Additionally, a software representation of a disciminator is to be developed.

Last, algorithms for numerical integration are discussed and used for calculating the relation between drift distance and drift time. 
# Data format
The raw data is read from a binary file. Its contents are as follows:

1.) First 8 bytes: Number of events in the binary file

2.) 4 bytes: Number of entries per event called "n_bins"

3.) n_bins * 64 bits: double precision floating point numbers containing the voltage for each of the 800 FADC bins

4.) Second point repeated as many times as coded in the file's first 8 bytes.

# Code conventions
Writing this code I tried following the PEP 8 coding conventions found at https://www.python.org/dev/peps/pep-0008

# Contact
For a fully implemented version of this software contact me via mail


