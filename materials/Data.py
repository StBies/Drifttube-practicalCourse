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
