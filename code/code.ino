const int tension = A0;
int current_tension;

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  current_tension = analogRead(tension);
  Serial.println(current_tension);
  delay(500);
}

  115
  1013
  118
  116
  1015
  1020
  110
  1019

  