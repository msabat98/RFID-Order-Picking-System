# RFID-Order-Picking-System
This project investigates which IoT technologies currently exist in warehouses and how  they can be adapted to propose a solution which will automate and improve the order picking  process. The basis of this investigation will focus on using a WMS which integrates IoT  technology which will optimise order picking through automating inventory locating, standard  routing policies to find the optimal picking route and providing a warehouse simulation model  for a hand-held device tool which is used by warehouse employees aiming to enhance the speed  of the picking process, and provide the most efficient picking route to complete an order. 


# Technologies used:

Technical Requirements:

linux OS
Apache/NGINX server (open-source web servers to handle HTTP traffic, NGINX preferred due to architecture)
Python3 
MySQL 
HTML, CSS
PHP (phpMyAdmin for database management)


Hardware Requirements:

A raspberry Pi 3b+ was used for this project along witht he necessary RFID components which enable the Raspbverry Pi to interact with the RFID Module.


Potentiometer A variable resistor used to control the LCD 
screen brightness and contrast levels 
LCD Screen (Liquid Crystal Display) The LCD screen is 16x2 size (16 characters
in 2 lines). Module programmed to display 
text output to the order picker to aid with 
picking tasks.
RFID MFRC522 13.56MHz module used to read and write 
data to RFID tags. The primary component 
used to replicate an RFID scanner 
functionality
RFID Tags Passive tags (power supplied by RFID 
MFRC522 reader) which are attached to 
items; each item is uniquely identified.
Figure 7: Hardware Architecture26
Raspberry Pi 3b+ Small computer which has GPIO (General 
Purpose Input/Output) pins to install the 
hardware components. Used to replicate a 
handheld RFID device and run the WMS.
Display Monitor Used to remotely access the Raspberry Pi Interface 


# Functional Requirements 

FR001 Reading RFID tags for order items 
FR002 Writing data to RFID tags for items 
FR003 Storing data for the RFID tags
FR004 Provide a visual interface for order picker to follow 
commands
FR005 Provide a visual interface to view items and location 
FR006 The system should allow new item entries to be made and be 
allocated an RFID tag
