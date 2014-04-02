/*----------------------------------------------------- 
Author:  --<fAnDrEs>
Date: Wed Mar 26 14:38:10 2014
Description:

-----------------------------------------------------*/
float f=0; 

void setup()
{
    int n = 0;
}
 
void loop()
{
    if (USB.available()) 
    {
    unsigned char a;
    unsigned char buffer[2];
    //char received_char;
    a = USB.read(buffer[1]);
    
    if (a == '1') toggle(USERLED);   
    //if (buffer == 69) toggle(USERLED);

    USB.send(a, 1);
    //USB.send(buffer[0], 1);
    //USB.send(buffer[0], 1);
    }
}