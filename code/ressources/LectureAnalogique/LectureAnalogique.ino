/*Lecture Analogique
Lecture Analogique : ce programme va lire une valeurCapteur(entre 0 et 5V) sur la broche analogique A0 à A5, 
la valeurCapteur sera aussitôt convertie en numérique sur 10 bits (entre 0 et 1023) puis affiché grace au 
moniteur série ou au grapheur série(Tools > Serial Plotter menu).
Remarque : l'affichage ne peut se faire que sur une des deux sorties, afficheur ou grapheur.
Initialisation d'une entrée analogique :
Les entrées analogiques A0 à A5 sont automatiquement paramétrées au démarrage du programme. 
Il n'y a donc rien à faire pour spécifier leur utilisation !!! 

Lecture d'une entrée analogique :
Pour pouvoir lire une entrée analogique, on peut utiliser le code suivant :
    int valeur;
    valeur = analogRead(A0 à A5); on peut aussi remplacer A0...A5 par 0...5

Par exemple, si on souhaite récupérer la valeur convertie de l'entrée A2 et l'afficher sur le moniteur série, les instructions sont les suivantes :

    int valeur;
    valeur = analogRead(A2);
    Serial.print("Valeur = ");
    Serial.println(valeur);
 */

// Entete déclarative

int valeurCapteur;

void setup() 
{
  // initialise la communication série à 9600 caractères par seconde:
  Serial.begin(9600);  
}

// la fonction loop va s'éxécuter en boucle indéfiniment
float last_valeur = 0; //stockage de l'ancienne valeur de la valeurCapteur
float epsilon = 10; //écart entre l'ancienne et la nouvelle valeurCapteur

void loop()
{
  // lecture de l'entrée analogique A0 (de 0V à 5V), converstion en valeur numérique codé sur 10 bits (de 0 à 1023) et stockage dans la la variable valeurCapteur. 
  valeurCapteur = analogRead(A3);
  
  if (valeurCapteur >= last_valeur + epsilon||valeurCapteur <= last_valeur - epsilon) //si abs(valeurCapteur-last_valeurCapteur) supérieur ou égal à epsilon :
  {
    last_valeur=valeurCapteur;
    Serial.print(" est de : "); 
    Serial.print(valeurCapteur);
    Serial.println(" volts");
  }
  delay(100);  /* Laisser cette valeur à 1000 pour le moniteur série, choisir 100 pour
  le traceur série */
}


/* Après avoir téléverser le programme vous pouvez observer l'évolution (menu Outils/Moniteur série) de la 
 *  valeur de la valeurCapteur en entrée sur la broche A0 en utilisant le moniteur série 
 *  (vérifier que le débit du moniteur série soit bien de 9600 bauds).
 *  Vous pouvez aussi voir les évolutions (penser à fermer le moniteur série !) en utilisant le traceur série 
 *  (menu Outils/Traceur série) en utilisant de préférence une valeur de delay à 100 
 */

/* MODIF 1 : 
 Modifier le programme pour obtenir l'affichage de l'image de la valeurCapteur sur 10 bits.
 Commentaire.
 */

/* MODIF 2 :
Modifier le programme pour obtenir l'affichage de la valeurCapteur (en volts) uniquement si celle ci change.
En pratique (voir commentaire de la question précédente) il faudra admettre un seuil de changement...

*/

/* MODIF 3 :
Modifier le programme pour obtenir l'affichage de la valeurCapteur (en volts) uniquement si celle ci change 
et lui associer le numéro de l'acquisition. Il faudra bien sûr conserver le seuil de changement.

*/ 

/* MODIF 4 :
Modifier le programme pour obtenir l'affichage de la valeurCapteur (en volts) uniquement si celle ci change 
et lui associer le numéro de l'acquisition. Il faudra bien sûr conserver le seuil de changement. 
La led branchée sur la sortie 5 devra s'allumer si la valeurCapteur est supérieure à 4,5 volts
*/ 
