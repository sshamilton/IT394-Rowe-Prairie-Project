# Project Overview
This file details related background information, fully describes the problem, current solutions, and the plan for solving it with a web application. This file also Addresses the relevance of the problem, and the scope of the project.
(*NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx *)
1. Background Information & Problem Relevance
2. The Problem
3. Current Solutions
4. Proposed Solution - iRoom Inspector Web Application
5. Application Structure Plan
6. The Scope of the Project
7. Stakeholder (Potential User) Analysis
8. Contacts
9. Works Cited

## Background Information & Problem Relevance
Every day of the week, cadets at the Untied States Military Academy are tasked with inspecting the rooms of their peers and 
subordinates to ensure that they are cleaned and kept organized according to the standards for rooms at West Point.
When rooms are inspected, they receive a various number of "gigs" for deficient aspects of their room.  Rooms that receive 3 or
more gigs fail inspection, and are required to fix their gigs and then keep their room to standard for the remainder of the day, 
until 2330.  The record of a room's pass/fail inspection history, how many gigs they received, and what gigs they received, is kept 
hung up on a paper sheet that hangs outside their rooms.  Although this allows
for some degree of evaluating how well that roommates have kept their room to standard over the course of the semester, it requires
superiors to manually check the sheets of all their subordinates.  Additionally, if roommates wanted to, they could simply print
a new inspection sheet and effectively "clear the history" of their past room inspections, which prevents superiors from having an 
efficient way to compare the performance of their subordinates in regards to room standards.
Printing a new inspection sheet and thorwing away your old sheet is not encouraged, but it is also not currently unauthorized.

## The Problem
There is currently no efficient system for cadet superiors to compare the performance of their subordinates in regards to room
standards.  Additionally, when cadets check rooms, they must refer back to a printed sheet that has a list of standards
that a room must meet.  Also, there is currently no efficient way to quantitatively analyze the performance of cadets across different
squads, battalions, companies, battalions, regiments, and as a whole corps.  

## Current Solutions
In the past, as far as our team is aware, there have not been any proposed solutions to attempting to gather data on cadet room standard performance
across different levels above the company level. However, there have been recent attempts by various companies, such as Company C1, to 
have record cadet room standard performance data.
### *** Excel on Microsoft Teams - Company C1 ***
I asked CDT Bernard Jenkins ’20 Co. C1, who was in charge of the Excel sheet that my company (C1) tried to use last semester 
to record AMI pass and fail rates, about his thoughts on the Excel sheet.  CDT Jenkins said that our company tried to use a 
Microsoft Teams’ Excel sheet to record AMI passes and failures initially, but cadets stopped recording pass/fail rates 
almost altogether after about a few weeks.  CDT Jenkins hypothesized that the complexity and size of the spreadsheet, which 
had a significant number of rooms as well as dates for the semester, made it difficult to navigate and use, and that this 
was why cadets stopped using it.  

## Proposed Solution - iRoom Inspector Web Application
Our Distributed Application Development team, consisting of CDT Chase Prairie '20, Co. C1 and CDT Anton Rowe '21, Co. E4
believes that this problem can be solved with a web application that cadets could use on their phones and laptops.
Our team plans to develop a room inspection checklist app (web application) for facilitating inspecting AMI/SAMI 
(A.M. Inspection standards & Saturday A. M. Inspection standards) in a more organized and standardized manner that 
would generate useful data in the process.  The current plan for the app is a checklist app with a checklist of all
AMI or SAMI standards that a room must meet.  

## Application Structure Plan
When using the app, cadets will first select a barracks from a dropdown menu, 
select a floor from a dropdown menu, select a room from a dropdown menu, and select the date from a dropdown menu (with
the preset value for date being the current date).  Then, as cadets are inspecting rooms, they can simply scroll down a
checklist of standards, and select a checkmark or "X" mark if a room meets or does not meet a standard.  Cadets will then
click either "Submit" to submit the report, or "Return" to return to the previous page in the event that they 
selected one of the wrong criterion previously, or if they ran out of time to finish the inspection.
Furthermore, Every "X" mark constitutes a gig, so if a cadet submits a report with 3 or more "X"'s checked, the system
will automatically record the room as having failed inspection (or passed if less than 3 "X"'s are checked.

## Model Diagram
<div align="center">
    <img src="Images/Model%20Diagram.png" width="550" />
</div>

## The Scope of the Project
The primary function of this project is to develop a web application that will allow cadets to efficiently record
room passes and failures, as well as number of gigs and gig details.  Potential additions that we hope to include in this app
are the ability for users to see data, such as how many rooms across their company/battalion/regiment/the corps have been 
checked off for AMI/SAMI that day, how many rooms are in PMI, room inspection pass rates by company/battalion/regiment/the corps,
and what the most common gigs are (for example, unclean floors, clothes left out, or unclean sinks).  
We hope that this would incentivize companies to check AMI more frequently if they are able to see their inspection percentages 
compared to other companies.  Altogether, we hope this app could help standardize room inspection rates and standards across the 
corps, as well as make military grades (which are often significantly influenced by room cleanliness) more objective, rather than 
subjective.  If possible, we will try to code an app for publication on the IOS and/or android app store so that this app will 
truly be easy to use in daily cadet life, as well as likely to be adopted for routine use.  However, our primary goal is to develop 
a functioning Django Web App that cadets can use to facilitate and track data on AMI/SAMI inspections. 
(*NOTE: Text taken from CDT Prairie, Chase '20 Project Proposal)

## Stakeholder (Potential User) Analysis
I asked CDT Bernard Jenkins, '20, Co. C1 about his thoughts on this app. 
CDT Jenkins thought that if people could use an app on their phones or a simple app on their 
laptops to more easily select a room number from a drop down menu, select the date, and select pass/fail (and possibly 
check various gigs from a checklist), that the app would be much easier to use and there is a chance it could be adopted 
for regular use across the corps.

## Contacts
* CDT Prairie, Chase G. '20, Co. C1
  * Email: Chase.Prairie@WestPoint.edu
  * Cell: 253-279-1771
* CDT Rowe, Anton '21, Co. E4
  * Email: Anton.Rowe@WestPoint.edu
  * Cell: 404-453-3333

## Works Cited
* CDT Prairie, Chase G. '20, Co. C1.  "PRAIRIE IT394 Project Proposal.docx"  28 FEB 2020. 
*NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx

* CDT Jenkins, Bernard ’20 Co. C1. (2020, February 28). Personal interview.

