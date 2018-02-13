import numpy as np
import matplotlib.pyplot as plt

class Data:
    """ The Data class is basically a container for an array that contains the raw voltage
        This class offers a method to plot the event using matplotlib

        Author: Stefan Bieschke
        Date: 02/12/2018
    """
    def __init__(self,dataArray,eventNumber):
        """ Constructor
            Initializes a new Data object with the raw data measured by a FADC given as parameter. Also sets an event number.

            Author: Stefan Bieschke
            Date: 02/12/2018

            Parameters
            ----------
            dataArray : array
                Array containing the raw voltage readings from the FADC
            eventNumber : int
                Number of the event
        """
        self.rawData = dataArray
        self.eventNumber = eventNumber
        
        
    def getDriftTime(self,threshold,calibrated):
        """ Returns the drift time of this event's Data in nanoseconds
            The DataSet must be calibrated prior to calculating the drift time.
            
            Author: Stefan Bieschke
            Date: 02/12/2018

            Parameters
            ----------
            threshold : float
                threshold in volts that must be undershot in order to find drift time

            calibrated : bool
                specifying if DataSet is calibrated

            Returns
            -------
            int
                Drift time in nanoseconds
        """
        #TODO: implement
        return 0
            
    def getArray(self):
        """ Getter method for the raw array

            Author: Stefan Bieschke
            Date: 02/12/2018

            Returns
            -------
            array
                Array containing the raw voltage
        """
        return self.rawData

    def plotData(self):
        """ Plot the Data
            Plots the event's voltage pulse form using matplotlib with time [ns] on the x-axis and voltage [V] on the y-axis.
            
            Author: Stefan Bieschke
            Date: 02/12/2018
        """
        #TODO: implement time calibration
        plt.title("Event #{} voltage".format(self.eventNumber))
        plt.xlabel("time [ns]")
        plt.ylabel("voltage [V]")
        plt.plot(self.rawData)
        plt.show()

class DataSet:
    """ A collection of Data objects. This class offers some methods to pull out
    events, to ask for the size and, most important, to perform a ground calibration
    """
    def __init__(self):
        """ Default constructor
            Initializes an empty DataSet object
            
            Author: Stefan Bieschke
            Date: 02/12/2018
        """
        self.nEvents = 0
        self.isCalibrated = False
        self.events = []

    def __init__(self,events):
        """ Constructor with an event list as parameter.
            Initializes a new DataSet object and sets the passed event list as its events. After construction, the DataSet size will be the same as the passed list's size.

            Author: Stefan Bieschke
            Date: 02/12/2018

            Parameters
            ----------
            events : list
                list of Data objects
        """
        self.nEvents = len(events)
        self.isCalibrated = False
        self.events = events

    def getEvent(self,eventNo):
        """ Returns the event specified by the parameter eventNo as Data class object if at least eventNo events exist in the DataSet.

            Author: Stefan Bieschke
            Date: 02/12/2018

            Parameters
            ----------
            eventNo : int
                number of the requested Data object. Must be smaller than self.nEvents.

            Returns
            -------
            Data
                Data object containing the event
        """
        if eventNo < self.nEvents:
            return self.events[eventNo]

    def getSize(self):
        """ Getter method for the size of the DataSet.
            Returns the size of the DataSet, thus the maximum number of an event that can be requested using the getEvent(...) method.
            
            Author: Stefan Bieschke
            Date: 02/12/2018

            Returns
            -------
            int
                Number of events stored in this DataSet object.
        """
        return self.nEvents

    def performGroundCalibration(self):
        """ Perform a ground calibration on all data in this DataSet.
            After the ground calibration, ground potential should read around 0.0 Volts.

            Author: Stefan Bieschke
            Date: 02/12/2018
        """        
        zero = 0
        #TODO implement
