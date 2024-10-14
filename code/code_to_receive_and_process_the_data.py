# Author : Enzo MORAN 
# github : github.com/moranenzo

""" Importing modules """
import serial # arduino/python communication
import numpy as np
import matplotlib.pyplot as plt # to plot : voltage = f(time)


"""Opening the serial connection"""
port = "COM6"      # COM6 is the port used by our Arduino to communicate the voltage values

try : arduino = serial.Serial(port,timeout=1)
except: print('Check the port used')


"""Variable initialization"""
voltage_max = 5     # maximum voltage value recorded by the Arduino
voltage_low = 0     # voltage value when the voltage is low
voltage_mid = 3.5   # voltage value separating low and high voltage

limit = int(voltage_mid * 1023/voltage_max) # converting voltage_mid to a value between 0 and 1023

nb_acq = 40 # number of values recorded
nb_val = 8  # number of bits to be processed

rawdata = []        # raw data
compt = 0


"""Receiving data"""
arduino.readline()  # discard the first data point which is empty in our case

while compt < nb_acq:
    rawdata.append(str(arduino.readline()))
    compt += 1

#print('rawdata : ', rawdata)

arduino.close()


"""Data cleaning and storage"""

def clean(L:list)->list:
    '''
    elements of L are supposed to be of the form: "b'xxx\\r\\n'"
    i.e. L=["b'xxx\\r\\n'", "b'xxx\\r\\n'", ...]

    this function keeps only xxx (x is an integer)
    i.e. cleanL=[xxx, xxx, ...]
    '''
    cleanL = []
    for elt in L:
        temp = elt[2:-5]  # "b'xxx;y\\r\\n'" -> "xxx;yy"
        cleanL.append(int(temp))  # ["xxx", "yy"] -> [xxx, yy]
    return cleanL

cleaned_data = clean(rawdata)
print('cleaned_data : ', cleaned_data)

def write(L:list):
    '''If L is of the form [xxx, xxx, ...]
    Then write writes in the file:
        xxx
        xxx
        ...
    '''
    compt = 0
    file = open("data.txt", mode="w")
    for elt in L:
        compt += 1
        temp = str(elt)
        file.write(temp + ';' + str(compt) + '\n')
    file.close()

'''
write(cleaned_data)    # write values into data.txt file

vals, temps = np.loadtxt("data.txt", delimiter=";", unpack=True)


"""Plotting values"""
plt.plot(temps, vals)
plt.show()
'''


"""Data processing"""
                
def reception(L:list, n:int)->list:
    '''
    the received message is of the form [0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0]
    
    the first 1 is signaling the start of the message
    n is the number of bits received
    '''
    i = 0
    while L[i] == 0 and i < len(L):  # removing initial 0s
        i += 1
    i += 1  # removing the signal bit (the first 1)
    if i + n > len(L):
        print('The message is cut off, please try
