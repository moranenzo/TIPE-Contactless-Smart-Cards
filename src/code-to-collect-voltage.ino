// Plug the Arduino to the capacitor of the reader (left circuit)

const int voltagePin = A0; // A0 is the pin where the voltage is connected
int currentVoltage;

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 bps
  pinMode(13, OUTPUT); // Sets pin 13 as output
}

void loop() {
  currentVoltage = analogRead(voltagePin); // Read the voltage from the A0 pin
  Serial.println(currentVoltage); // Send the voltage value to Python via the Serial link
  delay(500); // Delay for 500 milliseconds
}
