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
        print('The message is cut off, please try again')
    else:
        return L[i:i+n]

recep_data = reception(cleaned_data, nb_val)
assert type(recep_data) == list

def voltage_to_binary(L:list)->list:
    """Converts the voltages (values between 0 and 1023) recorded in L
    and returns the corresponding binary values"""
    newL = []
    for elt in L:
        if elt > limit:
            newL.append(1)
        else:
            newL.append(0)
    return newL

binary_data = voltage_to_binary(recep_data)
print('binary_data : ', binary_data)


def binary_to_text(L:list)->str:
    """Converts a binary string and returns the corresponding text"""
    text = ""  # empty string that will contain the final text
    octets = [L[i:i+8] for i in range(0, len(L), 8)]  # split the list into 8-bit chunks

    for octet in octets:
        ascii_val = 0

        for i in range(8):
            ascii_val += octet[7-i] * (2**i)  # calculate the chunk value in base 10

        char = chr(ascii_val)  # convert the ASCII code to character
        text += char
    return text


message = binary_to_text(binary_data)
print('message : ', message)


write(binary_data)    # writing the values into data.txt

vals, temps = np.loadtxt("data.txt", delimiter=";", unpack=True)


"""Plotting values"""
plt.plot(temps, vals, "ob")
plt.show()
