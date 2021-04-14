#!/usr/bin/env python
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

lcd = LCD.Adafruit_CharLCD(4, 24, 23, 17, 18, 22, 16, 2, 4);# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


print ("Welcome to the Order Picking system")
print ("Scan your item now")

try:
  while True:
    lcd.clear()
    lcd.message('Place tag to\nregister item')
    id, text = reader.read()
    cursor.execute("SELECT id FROM items WHERE rfid_uid="+str(id))
    cursor.fetchone()

    if cursor.rowcount >= 1:
      lcd.clear()
      lcd.message("Overwrite\nexisting item?")
      overwrite = input("Overwite (Y/N)? ")
      if overwrite[0] == 'Y' or overwrite[0] == 'y':
        lcd.clear()
        lcd.message("Overwriting Item.")
        time.sleep(1)
        sql_insert = "UPDATE items SET name = %s WHERE rfid_uid=%s"
      else:
        continue;
    else:
      sql_insert = "INSERT INTO items (name, rfid_uid) VALUES (%s, %s)"
    lcd.clear()
    lcd.message('Enter new Item')
    new_name = input("Name: ")

    cursor.execute(sql_insert, (new_name, id))

    db.commit()

    lcd.clear()
    lcd.message("Item " + new_name + "\nSaved")
    time.sleep(2)
    
finally:
  GPIO.cleanup()