/*
  SD card read/write

  This example shows how to read and write data to and from an SD card file
  The circuit:
   SD card attached to SPI bus as follows:
 ** MOSI - pin 11
 ** MISO - pin 12
 ** CLK - pin 13
 ** CS - pin 4 (for MKRZero SD: SDCARD_SS_PIN)

  created   Nov 2010
  by David A. Mellis
  modified 9 Apr 2012
  by Tom Igoe

  This example code is in the public domain.

*/

#include <SPI.h>
#include <SD.h>

File myFile, myFile2;
unsigned long waktu = 0 ;
unsigned long array_waktu[100] ;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Open serial communications and wait for port to open:
  Serial.print("Initializing SD card...");

  if (!SD.begin(4)) {
    Serial.println("initialization failed!");
    while (1);
  }
  Serial.println("initialization done.");
  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  myFile = SD.open("isi_SD.txt", FILE_WRITE);

  // if the file opened okay, write to it:
  if (myFile) {
    Serial.print("Writing to isi_SD.txt...");
    for (int i = 0 ; i < 100 ; i ++) {
      waktu = millis ();
      delay(1);
      array_waktu [i] = waktu;
    }
    for (int i = 0 ; i < 100 ; i++) {
      String waktu_string = String (array_waktu[i]);
      myFile.println(waktu_string);
    }
    // close the file:
    myFile.close();

    Serial.println("done.");
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening isi_SD.txt");
  }
  // re-open the file for reading:
  myFile2 = SD.open("isi_SD.txt");
  if (myFile2) {
    // read from the file until there's nothing else in it:
    while (myFile2.available()) {
      Serial.write(myFile2.read());
    }
    // close the file:
    myFile2.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening isi_SD.txt");
  }
}
