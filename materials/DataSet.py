import numpy as np
import matplotlib.pyplot as plt

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
