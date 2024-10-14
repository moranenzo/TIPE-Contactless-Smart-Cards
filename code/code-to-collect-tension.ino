"Plug the arduino to the condensator of the lector (left circuit)"

const int tension = A0; "A0 is the pin where the tension is plugged"
int current_tension; 

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  current_tension = analogRead(tension);
  Serial.println(current_tension); "transmission of the tension to Python by the Serial link"
  delay(500);
}
