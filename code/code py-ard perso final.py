# Author: Enzo MORAN
# GitHub: github.com/moranenzo

""" Importing modules """
import serial
import time



def text_to_binary(text):
    binary_string = "" # Initialize an empty binary string
    
    for char in text:
        ascii_val = ord(char)  # Convert the character to its ASCII value
        binary_val = bin(ascii_val)[2:]  # Convert the ASCII value to binary

        while len(binary_val) < 8:
            binary_val = "0" + binary_val  # Add leading zeros if the binary value is less than 8 bits
            
        binary_string += binary_val  # Add the binary value to the binary string
        
    return binary_string


def text_to_arduino(text, port="COM8", baudrate=9600, timeout=1):
    try: 
        arduino = serial.Serial(port, baudrate=baudrate, timeout=timeout) # The initialization of the serial communication with the Arduino may fail if the Arduino is not properly connected or if the wrong port is used
        print(f"Connected to Arduino on port {port}")

        binary_string = text_to_binary(text).encode('utf-8')  # Convert text to binary string
        print(f"Binary string to send: {binary_string}")

        # Loop through the binary string and send each bit to the Arduino
        for i in range(len(binary_string)):
            try:                
                arduino.write(binary_string[i])
                time.sleep(0.1)  # Short delay to ensure proper communication timing
                
            except serial.SerialTimeoutException: # This exception is raised if the communication times out while trying to send data
                print("Error: Data send timed out.")
                break  # Stop the loop if a timeout occurs
                
            except serial.SerialException as e: # This exception handles any other serial communication errors, such as loss of connection
                print(f"Serial error while sending data: {e}")
                break  # Stop the loop if a serial error occurs

        print("Data successfully sent to Arduino.")

    except serial.SerialException as e: # This exception will handle an issue when initializing the serial connection (e.g., wrong port or device)
        print(f"Error connecting to Arduino: {e}")
        
    except Exception as e: # This generic exception catches any other unforeseen errors that may occur
        print(f"An unexpected error occurred: {e}")
        
    finally: # to ensure that the serial connection is closed properly even if an error occurred during the process
        if 'arduino' in locals() and arduino.is_open:
            arduino.close()  # Close the serial connection
            print("Serial connection closed.")
