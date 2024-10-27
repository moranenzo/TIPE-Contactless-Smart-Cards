float binaryMessage;

void setup() {
  Serial.begin(9600); // Opens serial port, sets data rate to 9600 bps
  pinMode(13, OUTPUT); // Sets pin 13 as output
}

void loop() {
  if (Serial.available() > 0) {
    binaryMessage = Serial.read(); // Reads incoming serial data from Python

    if (binaryMessage == '0') {
      digitalWrite(13, LOW); // Turns off the LED if message is '0'
      delay(50);
    }
    else if (binaryMessage == '1') {
      digitalWrite(13, HIGH); // Turns on the LED if message is '1'
      delay(50);
    }

    digitalWrite(13, LOW); // Turns off the LED after processing the message
  }
}
