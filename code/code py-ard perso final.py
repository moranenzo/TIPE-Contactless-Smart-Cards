# Créé par Raphael, le 20/01/2023 en Python 3.7


def texte_vers_binaire(text):
    # Initialise une chaine binaire vide
    binary_string = ""

    # Itère sur chaque caractère du texte
    for car in text:
        # Convertit le caractère en sa valeur ASCII
        ascii_val = ord(car)
        # Convertit l'ASCII en binaire
        binary_val = bin(ascii_val)[2:]

        # ajoute des zéros si la valeur binaire est de moins de 8 bits
        while len(binary_val) < 8:
            binary_val = "0" + binary_val

        # ajoute la valeur binaire à la chaine binaire
        binary_string += binary_val

    return binary_string

import serial
def texteversArduino(text):
    chaine_binaire=texte_vers_binaire(text).encode('utf-8')
    print(chaine_binaire)
    arduino=serial.Serial("COM8",baudrate=9600,timeout=.1)       #etablit la communication entre arduino et l'ordinateur ; timeout=delai entre les envois sur arduino
    for i in range (len(chaine_binaire)):                           # deuxieme façon d'envoyer

        arduino.write((chaine_binaire[i]))



####arduino.write(chaine_binaire) #premiere façon d'envoyer
##
##
##
##
##
### Example usage
####binary_string = "0100100001101111011011110110111001110100111001101101001011011100110011100100001"
####print(binary_to_text(binary_string))
##
###Arduino
##'''
##const int sensorPin = A0; // Pin connected to the sensor
##const int threshold = 500; // Maximum value for the sensor
##int sensorValue = 0; // Variable to store the sensor value
##
##void setup() {
##  pinMode(sensorPin, INPUT); // Configure sensor pin as input
##  Serial.begin(9600); // Start the serial communication
##}
##
##void loop() {
##  sensorValue = analogRead(sensorPin); // Read sensor value
##
##  if (sensorValue > threshold) { // Check if the value is greater than the threshold
##    Serial.write(1); // Send 1 in binary
##  } else {
##    Serial.write(0); // Send 0 in binary
##  }
##  delay(1000); // Wait for 1 second
##}
##'''

