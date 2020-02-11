# Internal_Hackathon
This was a project developed in the transfiNITTe intra-NIT hackathon 2020. The aim of the project was to use image processing integrated 
with a web app to detect the features of cars entering the NIT Trichy campus and to detect suspicious vehicles so as to prevent untoward
incidents from happening within the campus. 
This repo contains the code for the backend of the web-app, developed using Django.
The backend of the app interfaces with the ML model, getting it's output. Apart from this, it is also integrated with a third party 
fast2sms api which automatically sends an SMS to the security personnel in case of a new previously unrecorded vsitor entering
college premises.
The Django backend is developed using the Django-REST framework.
