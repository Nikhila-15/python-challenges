Emergency Resource Dispatch Analyzer

SRM University AP
Department of Computer Science and Engineering
Course Code CSE205
Subject Hands on Python
Challenge Code2Xplore 60 Days Challenge Day 5
Concerned Faculty Dr Yasir Afaq


---Project Description---
This project is developed as part of the Code2Xplore 60 Days Challenge.
The program analyzes emergency resource requests received from different zones during a disaster drill.
The system identifies invalid values, categorizes valid requests into demand levels, and applies a personalized filtering rule based on the student's name length.

---Problem Statement---
The program accepts a list of integer values representing resource requests.
Each request is classified using conditional statements and processed using a for loop.
The program must
Accept a list of integers
Classify each request
Apply Personalized Logic Identifier PLI
Generate a final dispatch report

---Base Classification Rules---
If request is less than 0 it is Invalid Request
If request is equal to 0 it is No Demand
If request is between 1 and 20 it is Low Demand
If request is between 21 and 49 it is Moderate Demand
If request is 50 or above it is High Demand

---Personalization Logic---

L equals length of full name excluding spaces
PLI equals L mod 3
If PLI equals 0 apply Rule A.Rule A removes all Low Demand requests
If PLI equals 1 apply Rule B.Rule B removes all High Demand requests
If PLI equals 2 apply Rule C.Rule C keeps only Moderate Demand requests

---Program Output---

The program displays
Invalid requests
Low demand list
Moderate demand list
High demand list
Total number of valid requests
Number of requests removed due to PLI
Length of name L
PLI value
Applied rule

---My Personalization Details---
Name Length L
Write your actual name length here
PLI Value
Write your actual PLI value here 
Applied Rule
Write Rule A or Rule B or Rule C according to your PLI

---Constraints Followed---
Used list
Used for loop
Used conditional statements
Did not use list comprehension
Did not use dictionaries or sets
Did not use max min sum
Did not use sorting functions
No hard coded output

---How to Run---
Save the program as dispatch_analyzer.py
Open terminal or command prompt
Run the command python dispatch_analyzer.py


