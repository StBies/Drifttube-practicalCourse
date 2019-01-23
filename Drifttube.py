import numpy as np
import matplotlib.pyplot as plt

class Data:
    """ The Data class is basically a container for an array that contains the raw voltage
        This class offers a method to plot the event using matplotlib

        Author: Stefan Bieschke
        Date: 02/12/2018
    """
    def __init__(self,data_array,event_number):
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
        self._raw_data = data_array
        self._event_number = event_number
        
        
    def get_drift_time(self,threshold,calibrated):
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
            
    def get_array(self):
        """ Getter method for the raw array

            Author: Stefan Bieschke
            Date: 02/12/2018

            Returns
            -------
            array
                Array containing the raw voltage
        """
        return self._raw_data

    def plot_data(self):
        """ Plot the Data
            Plots the event's voltage pulse form using matplotlib with time [ns] on the x-axis and voltage [V] on the y-axis.
            
            Author: Stefan Bieschke
            Date: 02/12/2018
        """
        #TODO: implement time calibration
        plt.title("Event #{} voltage".format(self._event_number))
        plt.xlabel("time [ns]")
        plt.ylabel("voltage [V]")
        plt.plot(self._raw_data)
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
        self._n_events = 0
        self._is_calibrated = False
        self._events = []

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
        self._n_events = len(events)
        self._is_calibrated = False
        self._events = events

    def get_event(self,event_no):
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
        if event_no < self._n_events:
            return self._events[event_no]

    def get_size(self):
        """ Getter method for the size of the DataSet.
            Returns the size of the DataSet, thus the maximum number of an event that can be requested using the getEvent(...) method.
            
            Author: Stefan Bieschke
            Date: 02/12/2018

            Returns
            -------
            int
                Number of events stored in this DataSet object.
        """
        return self._n_events

    def is_calibrated(self):
        """ Returns the status of the calibration
            True if calibration was already performed, False else

            Returns
            -------
                bool
                    True if calibrated, False else

        """
        return self._is_calibrated

    def perform_ground_calibration(self):
        """ Perform a ground calibration on all data in this DataSet.
            After the ground calibration, ground potential should read around 0.0 Volts.

            Author: Stefan Bieschke
            Date: 02/12/2018
        """        
        zero = 0
        #TODO implement

    def calculateEfficiency(self,threshold):
        """ Calculate the detection efficiency for a given threshold voltage.

            Author: Stefan Bieschke
            Date: 02/19/2018

            Parameters
            ----------
            threshold : float
                Threshold in volts for that the efficiency is calculated.
                Must be smaller than zero.

            Returns
            -------
                float, float
                    Efficiency [0,1], error [0,1]
                    
        """
        efficiency, error = 0, 0
        #TODO implement
        return efficiency, error


#----------------------------------------------------------------------
#                           Begin program execution
#----------------------------------------------------------------------
file = open("event2.npy",'rb') #read binary mode
events = []

#Read first 8 Bytes
n_events = np.fromfile(file,np.int64,1)[0]
n_bins = np.fromfile(file,np.int32,1)[0]

#Read events from binary file
for i in range(n_events):
    data = np.fromfile(file,np.float64,n_bins)
    events.append(Data(data,i))

#Build DataSet object from events read above
dataset = DataSet(events)


dataset.perform_ground_calibration()

#print(dataset.get_size())
dataset.get_event(1).plot_data()

#TODO: Create drift time spectrum
drifttimes = []
#for i in range(dataset.get_size()):
#    drifttimes.append(dataset.get_event(i).get_drift_time(-0.25,dataset.is_calibrated()))

for event in dataset._events:
    drifttimes.append(event.get_drift_time(-0.25,dataset.is_calibrated()))

#TODO: Create rt-relation

#TODO: Drift time spectrum and rt-relation for several threshold voltages

plt.hist(drifttimes,bins=500)
plt.show()
