# This project is unfinished and the contents of this file are subject to change!!

# Auto-Service-Manager

The goal of this project is to create an app that can help auto repair shops manage their entire business.

This document will cover the issues this app can solve and its core functionalities.

## Users of this app

There are three types of users/roles of this app:

- **Administrator**,
- **Receptionist** and
- **Mechanic**.

**Administrator** uses this app to add employees, manage supplies of parts, access financial reports and delete data.		
**Receptionist** uses this app to register customers, schedule appointments and create work orders.	
**Mechanic** uses this app to see the assigned work orders, track the labor that's been done and parts that've been used and to mark the job as done.

Each user has to be registered and their data has to be authenticated.

## How is this app suppossed to be used?

Receptionist is tasked with finding customers and adding them and their car to the database. Then the receptionist books the appointment. The work order is created when customer's car arrives to the repair shop.	
Mechanic then recieves the work orders that's been assigned to them, makes a record of the problem and parts that have been used and sets the price of labor.	
An invoice gets created upon finishing the work and the car gets a record in the service history.