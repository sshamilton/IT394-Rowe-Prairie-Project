# Project Overview
This file details related background information, fully describes the problem, current solutions, and the plan for solving it with a web application. This file also Addresses the relevance of the problem, and the scope of the project.
(*NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx *)
## Table of Contents
1. Background Information & Problem Relevance
2. The Problem
3. Current Solutions
4. Proposed Solution - AMI App Application
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

## Proposed Solution - AMI App Application
Our Distributed Application Development team, consisting of CDT Chase Prairie '20, Co. C1 and CDT Anton Rowe '21, Co. E4
believes that this problem can be solved with a web application that cadets could use on their phones and laptops.
Our team plans to develop a room inspection checklist app (web application) for facilitating inspecting AMI/SAMI 
(A.M. Inspection standards & Saturday A. M. Inspection standards) in a more organized and standardized manner that 
would generate useful data in the process.  The current plan for the app is a checklist app with a checklist of all
AMI or SAMI standards that a room must meet.  


## Architecture
### Model Diagram
<div align="center">
    <img src="Images/Model%20Diagram.png" width="550" />
</div>

## Application Structure Plan
Cadets utilizing this app have four main use cases.  First, cadets can enter an inspection based on the room inspected, the date, if the room passed or failed, all gigs received, and any comments that they wish to add.  Second, cadets can view inspection records for all rooms on record by pulling up a link to various cadet barracks, and then selecting any of the rooms from that barracks to view that room's inspection record.  Third, cadets can view the performance records of their subordinates by entering their own xNumber, which allows them to then view a list of their subordinates with each subordinates inspection pass rate, the number of times that the subordinate has been inspected so far, and the date of that subordinate's most recent inspection.  Fourth, Cadets can also view a list of recent inspections if they wish to simply explore other inspections that have recently taken place across the corps.

## The Scope of the Project
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The primary function of this project is to develop a web application that will allow cadets to efficiently record
room passes and failures, as well as number of gigs and gig details.  Potential additions that we hope to include in this app
are the ability for users to see data, such as how many rooms across their company/battalion/regiment/the corps have been 
checked off for AMI/SAMI that day, how many rooms are in PMI, room inspection pass rates by company/battalion/regiment/the corps,
and what the most common gigs are (for example, unclean floors, clothes left out, or unclean sinks).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We hope that this would incentivize companies to check AMI more frequently if they are able to see their inspection percentages 
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

1. “Atom Beautify.” *Atom*, Atom Text Editor, https://atom.io/packages/atom-beautify.
    * *NOTE: Utilized Atom's Atom-Beautify package in order to format most or all HTML and python files and ensure that they adhere to PEP8 standards (to the best of my knowledge - not 100% sure that the way I ran Atom beautify formatted text to PEP8 standards, but I believe that it did).*

2. BG Buzzard, Curtis A. *USCC Cadet SOP*. United States Military Academy, 2019.
    * *NOTE: Utilized the USCC Cadet SOP for development of the various Gigs that were implemeted under admin site access.  Our group could not find the current checklist that is hung on most barracks doors, but we utilized the AMI (A.M. Inspection period) information within the USCC SOP from 2019 in order to develop the list of gigs that we incorporated.  
    * *NOTE: We would have added a link to view the 2019 USCC SOP online, but I do not believe that there are any sites hosting the PDF at this time.  However, this SOP is relatively similar to the 2012 USCC SOP, which can be accessed here:* **[Link to 2012 USCC SOP](https://docplayer.net/25953931-Uscc-sop-september-2012.html "2012 USCC SOP")**

3. CDT Prairie, Chase G. '20, Co. C1.  "PRAIRIE IT394 Project Proposal.docx"  28 FEB 2020. 
    * *NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx*

4. CDT Jenkins, Bernard ’20 Co. C1. (2020, February 28). Personal interview.

5. “Django Tutorial - How to Add Bootstrap.” *YouTube.com*, Tech with Tim, 22 Apr. 2019, www.youtube.com/watch?v=0mCZdemSsbs.
    * *NOTE: Followed this tutorial to learn how to use bootstrap with Django*

6. Goodridge, Max. “Simple Introduction to Django Forms (Django Tutorial) | **Part 45**.” *YouTube.com*, Max Goodridge, 10 Feb. 2017, www.youtube.com/watch?v=b8RpVs7bSgo.

7. Goodridge, Max. “How to Receive Data From a Django Form Using a POST Request (Django Tutorial) | **Part 46**.” *YouTube.com*, Max Goodridge, 13 Feb. 2017, www.youtube.com/watch?v=wzZiONbtwiA.

8. Goodridge, Max. “How to Save Data Input through Form Using a Django Model Form (Django Tutorial) | **Part 47**.” *YouTube.com*, Max Goodridge, 17 Feb. 2017, www.youtube.com/watch?v=qwE9TFNub84.
    * ***NOTE: Followed three consecutive tutorial videos from Max Goodridge on YouTube (Part 45-47), and modified some of the code used for help in using Django forms and properly saving form data from ModelForms to Models.***

9. Otto, Mark, and Jacob Thornton. “Introduction.” · *Bootstrap*, https://getbootstrap.com/docs/4.0/getting-started/introduction/.
    * *NOTE: Utilized code from bootstrap to add style and aesthetics to the application.  Some code utilized in html pages was copied and pasted directly from this link*

10. Rehman, Abdul *(User)*, and Zaidfazil *(User)*. “POST Request Done Successfully but Data Not Saved in Database.” *Stack Overflow*, (Site Users) Abdul Rehman & Zaidfazil, 22 July 2017, https://stackoverflow.com/questions/45256493/post-request-done-successfully-but-data-not-saved-in-database.
    * *NOTE: Utilized this source to understand how to save data from a form properly using form.save(commit=False) and form.save(commit=True), as well as to help understand how to use and interpret GET and POST requests differently*

11. user2449798user2449798, and Simeon VisserSimeon Visser. “Could Not Parse the Remainder: '[0]' from 'Item[0]' Django.” *Stack Overflow*, 1 July 1963, https://stackoverflow.com/questions/19895894/could-not-parse-the-remainder-0-from-item0-django.
    * *NOTE: Utilized this source to learn how to reference list items in HTML using list.0 instead of list[0]*

12. “Writing your first Django app (Tutorial).” *Django*, https://docs.djangoproject.com/en/3.0/intro/tutorial01/.
    * *NOTE: Followed this tutorial and utilized the Django web application development framework for a majority of the production of this web application.  Significant amounts of code utilized throughout this project in areas such as models, views, urls, templates, etc. follow this tutorial very closely.*
