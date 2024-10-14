const int tension_entree=A0; //port d'entrée utilisé
int data;
int dt = 1000; //écart de temps entre 2 mesures consécutives en secondes
int time=0;

//Initialisation de la liaison série
void setup()
{
  Serial.begin(9600); //permet de lancer une liaison série avec l'odinateur, VoltRate =9600  
}

//Acquisition des données
void loop()
{
  data = analogRead(tension_entree); //acquisition d'une valeur de tension
  Serial.println(String(data)+';'+String(time));
  delay(dt); //délai d'un seconde
  time += 1;
  Serial.flush(); //nettoie la liaison série
}
