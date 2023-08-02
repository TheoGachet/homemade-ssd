#include <LiquidCrystal.h>

//réglages en fonction du matériel, des branchements
LiquidCrystal lcd(12, 11, 6, 5, 4, 3);
const int pinMoteurGauche = 7;
const int pinMoteurDroit  = 8;

//variables
double voltage;
String mot;
char lettre;
bool droite = true;

void setup()
{
  pinMode(pinMoteurGauche, OUTPUT);
  pinMode(pinMoteurDroit, OUTPUT);
  lcd.begin(16, 2);
  lcd.clear();
}

void loop()
{
  lettre = 65;
  mot = "";
  avancer();
  
    while (1)
    {
    for (int i = 0; i < 5; i++)
    {
  	  delay(500);
  	  lettre += recupererBit() * pow(2, i);
    }
    if (lettre == 91)
    {
  	afficherMot();
    arreter();
	break;
    }
    else
    {
	  mot += lettre;
	  tourner(droite);
	  droite = !droite;
    }
  }
}

void avancer()
{
  digitalWrite(pinMoteurDroit, HIGH);
  digitalWrite(pinMoteurGauche, HIGH);
}

void arreter()
{
  digitalWrite(pinMoteurDroit, LOW);
  digitalWrite(pinMoteurGauche, LOW);
}

void tourner(bool droite)
{
  if (droite)
  {
    digitalWrite(pinMoteurDroit, LOW);
	digitalWrite(pinMoteurGauche, HIGH);
  }
  else
  {
    digitalWrite(pinMoteurDroit, HIGH);
	digitalWrite(pinMoteurGauche, LOW);
  }
  delay(850);
}

bool recupererBit()
{
  voltage = 0;
  for (int i = 0; i < 3; i++)
  {
	voltage +=analogRead(A0);
	delay(5);
  }
  if (voltage == 0)
	  return 0;
  return 1;
}

void afficherMot()
{
  lcd.setCursor(0, 0);
  lcd.print(mot);
}
