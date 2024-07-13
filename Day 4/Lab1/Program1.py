# Author : Ashwith Madikonda
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source.
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# As we did not cover exception handling yet, 
# input validation is not performed in the source code.

# Negative weight loss inidcated weight gain
# Inputs should be given in requested format only 

import datetime

patientName = input("Enter Name of patient : ")
newPatient = input("Has the patient been here before? (Y/N): ")
patientHeight = int(input("What is the patient’s height (in cm)? : "))
patientCurrentWeight = float(input("What is the patient’s weight (in kg)? : "))
patientsHealthScore = 0
dateFormat = f'%Y-%m-%d %H:%M:%S'


if(newPatient == 'N' or newPatient == 'n'):
    patientPreviousWeightDate = '1/1/200'
    changeInweight = -1
if(newPatient == 'Y' or newPatient == 'y'):
    patientPreviousWeight = float(input("What is the patient’s previous weight (in kg)? : "))
    patientPreviousWeightDate  = input("What is the patient’s previous weighed date(YYYY-MM-DD format): ")
    patientPreviousWeightDate = patientPreviousWeightDate + " 00:00:00"
    patientPreviousWeightDate  = datetime.datetime.strptime(patientPreviousWeightDate,dateFormat)
    changeInweight = patientPreviousWeight - patientCurrentWeight



practitionerScore = int(input("Practitioner’s overall assessment of the patient’s health (-5=very poor to +5=excellent, 0 for neutral) "))

bmi = round((patientCurrentWeight/(patientHeight**2)) * 10000,1)

if((bmi > 30) or (bmi < 17)):
    patientsHealthScore = 0
elif((bmi <= 29.9 and bmi >= 25) or (bmi >= 17 and bmi <= 18.4)):
    patientsHealthScore = 3
else:
    patientsHealthScore = 5

if((newPatient == 'N' or newPatient == 'n') and patientsHealthScore == 3):
   patientsHealthScore += 1
if((newPatient == 'Y' or newPatient == 'Y') and (changeInweight < 1 and changeInweight > -1) and patientsHealthScore == 3):
   patientsHealthScore -= 1
if((newPatient == 'Y' or newPatient == 'Y') and bmi >= 17 and bmi <= 18.4):
    if(changeInweight > 0):
        patientsHealthScore -= 3
    if(changeInweight < -1):
        patientsHealthScore += 2
if((newPatient == 'Y' or newPatient == 'Y') and bmi <= 17):
    if(changeInweight > 0):
        patientsHealthScore -= 5
    if(changeInweight < -1):
        patientsHealthScore += 5
if((newPatient == 'Y' or newPatient == 'Y') and bmi >= 25 and bmi <= 29.9):
    if(changeInweight < 0):
        patientsHealthScore -= 3
    if(changeInweight > -1):
        patientsHealthScore += 2
if((newPatient == 'Y' or newPatient == 'Y') and bmi >= 30):
    if(changeInweight > 0):
        patientsHealthScore -= 5
    if(changeInweight < -1):
        patientsHealthScore += 5



patientsHealthScore = patientsHealthScore + practitionerScore 
print(" \n \t \t \t  \t Melanie Diet Clinic \n")
print("\t \t \t *------------------------------------------* \n")
print("\t \t \t \t Receipt for patient name: ", patientName,"\n")
print("\t \t \t \t Patient weight: ", patientCurrentWeight,"\n")
if(newPatient == 'Y' or newPatient == 'y'):
    print("\t \t \t \t Patient weight loss: ", changeInweight,"\n")
    print("\t \t \t \t Day since last visit", (datetime.datetime.now()-patientPreviousWeightDate).days,"\n")
if(newPatient == 'N' or newPatient == 'n'):
    print("\t \t \t \t New Patient","\n")
    print("\t \t \t \t First visit","\n")
print("\t \t \t  -------------------------------------------- ","\n")
print("\t \t \t \t BMI: ",bmi,"\n")
print("\t \t \t \t Health: ",patientsHealthScore,"\n")
print("\t \t \t  ---------------------------------------------- ","\n")
if(patientsHealthScore > 5):
    print("\t \t \t \t Overall : Great condition!","\n")
if(patientsHealthScore <= 5 and patientsHealthScore >= 3):
    print("\t \t \t \t Overall : Need a little work","\n")
if(patientsHealthScore <= 3 and patientsHealthScore >= 1):
    print("\t \t \t \t Overall : Need a lot work","\n")
if(patientsHealthScore < 1):
    print("\t \t \t  \t Overall : At risk!","\n")


   
    
