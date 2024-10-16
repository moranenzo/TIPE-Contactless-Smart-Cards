float messagerecubinaire;
void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
pinMode(13,OUTPUT);
}
void loop(){
if (Serial.available()>0){
    messagerecubinaire=Serial.read();//sinon Serial.parseInt() 
    //messagerecubinaire=messagerecubinaire - 48;

     
        ;if (messagerecubinaire=='0') {
          digitalWrite(13,LOW);
          delay(50);
      }
      
         else if (messagerecubinaire=='1'){
           digitalWrite(13,HIGH);
           delay(50);}


     digitalWrite(13,LOW);
    }}
     
  


    
