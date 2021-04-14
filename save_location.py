#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
import Adafruit_CharLCD as LCD

db = mysql.connector.connect(
  host="localhost",
  user="picker",
  passwd="pi",
  database="orderpickingdb"
)

cursor = db.cursor()
reader = SimpleMFRC522()
lcd = LCD.Adafruit_CharLCD(4, 24, 23, 17, 18, 22, 16, 2, 4);

try:
  while True:
    lcd.clear()
    lcd.message('assign location')
    id, text = reader.read()
    cursor.execute("SELECT id FROM items WHERE rfid_uid="+str(id))
    cursor.fetchone()

    if cursor.rowcount >= 1:
      lcd.clear()
      lcd.message("Overwrite\nexisting location?")
      overwrite = input("Overwite (Y/N)? ")
      if overwrite[0] == 'Y' or overwrite[0] == 'y':
        lcd.clear()
        lcd.message("Overwriting location.")
        time.sleep(1)
        sql_insert = "UPDATE items SET location = %s WHERE rfid_uid=%s"
      else:
        continue;
    else:
      sql_insert = "INSERT INTO items (location, rfid_uid) VALUES (%s, %s)"
    lcd.clear()
    lcd.message('Enter new location')
    new_location = input("Location: ")

    cursor.execute(sql_insert, (new_location, id))

    db.commit()

    lcd.clear()
    lcd.message("Location " + new_location + "\nSaved")
    time.sleep(2)

    
finally:
  GPIO.cleanup()
