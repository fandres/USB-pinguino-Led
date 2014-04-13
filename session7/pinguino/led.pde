/*-----------------------------------------------------
Author:  --<fandres>
Date: 2014-04-13
Description: Lee del host un caracter, este es comparado 
 con l fin de encender o apagar los leds 5, 6 y 7 de la board pinguino

Programa PC python: https://github.com/fandres/USB-pinguino-Led/tree/master/session7/python
-----------------------------------------------------*/

u8 receivedbyte;
char buffer[64];

void setup()
{
    pinMode(7,OUTPUT);
    pinMode(6,OUTPUT);
    pinMode(5,OUTPUT);
}

void loop()
{
    receivedbyte=0;

    if(BULK.available()) 
      receivedbyte = BULK.read(buffer);   
    
    buffer[receivedbyte] = 0;

    if (receivedbyte > 0)
    {
      if (buffer[0] == '1') digitalWrite(7,HIGH);
      else if (buffer[0] == '2') digitalWrite(7,LOW);
      else if (buffer[0] == '3') digitalWrite(6,HIGH);
      else if (buffer[0] == '4') digitalWrite(6,LOW);
      else if (buffer[0] == '5') digitalWrite(5,HIGH);
      else if (buffer[0] == '6') digitalWrite(5,LOW);
      else {
          digitalWrite(7,LOW);
          digitalWrite(6,LOW);
          digitalWrite(5,LOW);
      }
    }
    
}
