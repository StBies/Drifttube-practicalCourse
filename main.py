import numpy as np
import matplotlib.pyplot as plt
import materials.Data as Data
import materials.DataSet as DataSet

#----------------------------------------------------------------------
#                           Begin program execution
#----------------------------------------------------------------------
file = open("event.npy",'rb') #read binary mode
events = []

#Read first 8 Bytes
nEvents = np.fromfile(file,np.int64,1)[0]

#Read events from binary file
for i in range(nEvents):
    data = np.fromfile(file,float,800)
    events.append(Data(data,i))

#Build DataSet object from events read above
dataset = DataSet(events)


dataset.performGroundCalibration()

#print(dataset.getSize())
#dataset.getEvent(1).plotData()

#Create drift time spectrum
drifttimes = []
for event in dataset.events:
    drifttimes.append(event.getDriftTime(-0.25,dataset.isCalibrated),)

plt.hist(drifttimes,bins=500)
plt.show()
