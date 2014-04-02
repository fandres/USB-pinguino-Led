/*----------------------------------------------------- 
Author:  --<fAnDrEs>
Date: Mon Mar 24 12:05:24 2014
Description:

-----------------------------------------------------*/


void setup() {
    //run once:
    int n = 0;
    }

void loop() {
  	USB.send("0", 1);// send 10 bytes on usb bus ("",n) n = exacto != basura
		toggle(USERLED);		                    // blinked user led for visual debug
		delay(1000);			                      // wait for 1 sec. before next sending
    }