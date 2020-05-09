# IT394-Rowe-Prairie-Project
## Link to Deployed Application
https://gentle-scrubland-63769.herokuapp.com/AMIApp/

## Admin Info
### Project Team - *"No I.T."*
* CDT Prairie, Chase G. '20, Co. C1
  * Email: Chase.Prairie@WestPoint.edu
  * Cell: 253-279-1771
* CDT Rowe, Anton '21, Co. E4
  * Email: Anton.Rowe@WestPoint.edu
  * Cell: 404-453-3333

## Project Overview
(*NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx*)
### Table of Contents
1. [Problem Statement](problem.md)
2. Architecture
3. Testing
4. Known Issues
5. Recommended Improvements
6. Works Cited

## Problem Statement
* [Problem Statement](problem.md)
  * Includes Project Overview & Problem Information
    * Includes Background Information & Problem Relevance, The Problem, Current Solutions, Proposed Solution (AMI App Application), Application Structure Plan, Architecture, The Scope of the Project, Stakeholder (Potential User) Analysis, Contacts, and Works Cited.

## Architecture
### Model Diagram
<div align="center">
 <img src="Images/Model%20Diagram.png" width="550">
</div>

### Application Structure Plan
Cadets utilizing this app have four main use cases.  First, cadets can enter an inspection based on the room inspected, the date, if the room passed or failed, all gigs received, and any comments that they wish to add.  Second, cadets can view inspection records for all rooms on record by pulling up a link to various cadet barracks, and then selecting any of the rooms from that barracks to view that room's inspection record.  Third, cadets can view the performance records of their subordinates by entering their own xNumber, which allows them to then view a list of their subordinates with each subordinates inspection pass rate, the number of times that the subordinate has been inspected so far, and the date of that subordinate's most recent inspection.  Fourth, Cadets can also view a list of recent inspections if they wish to simply explore other inspections that have recently taken place across the corps.

## Testing
### Previously Conducted Testing
Most app testing was done internally through admin testing, which proved that foreign keys were functioning properly and that basic functionality was working.  Three basic test cases were also develop in order to make app testing easier.  Developed test cases included **(1)** testing that rooms were assigned to cadets properly and could be referenced correctly, **(2)** testing that inspections could be assigned to rooms properly and inspections could be referenced based on the room in question, and **(3)** testing that a cadet's inspections could be viewed based on that cadet's room, and the inspections that occurred on that room.
### Plan for Future Testing
While some basic testing has been done, the project team plans to test the app significantly in the future.  Initial future testing plans include testing that subordinate pass rates are registering correctly, as well as testing the app with uncleaned data.  While the basic functionality of the app works when data is input correctly, it still requires significant improvement in regard to internal data cleaning and formatting in order to allow for easier use by users.  The group plans to have other cadets test the app and identify what types of mistakes that users make when entering data.  Anticipated mistakes in entering data include entering xNumbers as "x00123" as opposed to "00123", entering barracks names as "Brad_Long" as opposed to "Brad Long", and not holding down the ctrl button in order to select multiple gigs (which would render the app to only select the last clicked gig as opposed to all clicked gigs).  Testing the functionality of the app when improperly formatted data is input is the main area of testing that the group plans for in the future.  Additionally, as new features are added to the application, such as viewing the average inspection pass rate of an entire barracks across all rooms, then the group will develop new tests in order to ensure the functionality of added features. 

## Known Issues
* **I.** While the basic functionality of the app appears to work, the app has significant room for improvement in several areas.  First, entering data incorrectly, such as "x00123" as opposed to "00123" will prevent the app from working properly, and these input errors are not fixed automatically within the app.  
* **II.** Additionally, while the app allows users to enter inspections, it does not currently allow users to delete or modify inspections that they have entered, and this could pose a significant challenge if cadets make mistakes while entering data or accidentally hit *enter* too early.  Fixing these issues will make the app significantly better and user friendly.

## Recommended Improvements
* **First**, the group plans to improve the app's internal handling of improperly formatted inputs, such as "x00123" instead of "00123"
* **Second**, the group plans to add the feature to edit or delete old inspections, because users will inevitably make mistakes during either inspecting of rooms or during the entering of inspection data
* **Third**, the group plans to implement new features to the app that expand the capabilites of the app, such as those listed below
  * **I.** Identifying the most common gigs across different barracks, in order to identify differences inspection standards between different companies/regiments.
  * **II.** Identifying the inspection performance of a cadet's entire chain of command
  * **III.** Identifying the different performance rates across different positions across the corps.  For example, one would expect that the First Captain, as well as Brigade Staff Cadets, would perform better than Team Leaders or Members of Squad (MOS)'s
  * **IV.** Adding a feature to show which cadet conducted an inspection, and a link to that cadet's inspection records.  This will help to ensure that cadets are not excessively enforcing standards that they themselves are not adhering to.
  * **V.** Identifying the number of times that different cadets have inspected rooms.  A higher number of inspections conducted by a cadet shows a higher level of involvement with subordinates.

## Works Cited
1. “Atom Beautify.” *Atom*, Atom Text Editor, https://atom.io/packages/atom-beautify.
    * *NOTE: Utilized Atom's Atom-Beautify package in order to format most or all HTML and python files and ensure that they adhere to PEP8 standards (to the best of my knowledge - not 100% sure that the way I ran Atom beautify formatted text to PEP8 standards, but I believe that it did).*

2. BG Buzzard, Curtis A. *USCC Cadet SOP*. United States Military Academy, 2019.
    * *NOTE: Utilized the USCC Cadet SOP for development of the various Gigs that were implemeted under admin site access.  Our group could not find the current checklist that is hung on most barracks doors, but we utilized the AMI (A.M. Inspection period) information within the USCC SOP from 2019 in order to develop the list of gigs that we incorporated.  
    * *NOTE: We would have added a link to view the 2019 USCC SOP online, but I do not believe that there are any sites hosting the PDF at this time.  However, this SOP is relatively similar to the 2012 USCC SOP, which can be accessed here:* **[Link to 2012 USCC SOP](https://docplayer.net/25953931-Uscc-sop-september-2012.html "2012 USCC SOP")**

* CDT Prairie, Chase G. '20, Co. C1.  "PRAIRIE IT394 Project Proposal.docx"  28 FEB 2020. 
    * *NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx*

* CDT Jenkins, Bernard ’20 Co. C1. (2020, February 28). Personal interview.

* “Django Tutorial - How to Add Bootstrap.” *YouTube.com*, Tech with Tim, 22 Apr. 2019, www.youtube.com/watch?v=0mCZdemSsbs.
    * *NOTE: Followed this tutorial to learn how to use bootstrap with Django*

* Goodridge, Max. “Simple Introduction to Django Forms (Django Tutorial) | **Part 45**.” *YouTube.com*, Max Goodridge, 10 Feb. 2017, www.youtube.com/watch?v=b8RpVs7bSgo.

* Goodridge, Max. “How to Receive Data From a Django Form Using a POST Request (Django Tutorial) | **Part 46**.” *YouTube.com*, Max Goodridge, 13 Feb. 2017, www.youtube.com/watch?v=wzZiONbtwiA.

* Goodridge, Max. “How to Save Data Input through Form Using a Django Model Form (Django Tutorial) | **Part 47**.” *YouTube.com*, Max Goodridge, 17 Feb. 2017, www.youtube.com/watch?v=qwE9TFNub84.
    * ***NOTE: Followed three consecutive tutorial videos from Max Goodridge on YouTube (Part 45-47), and modified some of the code used for help in using Django forms and properly saving form data from ModelForms to Models.***

* Otto, Mark, and Jacob Thornton. “Introduction.” · *Bootstrap*, https://getbootstrap.com/docs/4.0/getting-started/introduction/.
    * *NOTE: Utilized code from bootstrap to add style and aesthetics to the application.  Some code utilized in html pages was copied and pasted directly from this link*

* Rehman, Abdul *(User)*, and Zaidfazil *(User)*. “POST Request Done Successfully but Data Not Saved in Database.” *Stack Overflow*, (Site Users) Abdul Rehman & Zaidfazil, 22 July 2017, https://stackoverflow.com/questions/45256493/post-request-done-successfully-but-data-not-saved-in-database.
    * *NOTE: Utilized this source to understand how to save data from a form properly using form.save(commit=False) and form.save(commit=True), as well as to help understand how to use and interpret GET and POST requests differently*

* user2449798user2449798, and Simeon VisserSimeon Visser. “Could Not Parse the Remainder: '[0]' from 'Item[0]' Django.” *Stack Overflow*, 1 July 1963, https://stackoverflow.com/questions/19895894/could-not-parse-the-remainder-0-from-item0-django.
    * *NOTE: Utilized this source to learn how to reference list items in HTML using list.0 instead of list[0]*

* “Writing your first Django app (Tutorial).” *Django*, https://docs.djangoproject.com/en/3.0/intro/tutorial01/.
    * *NOTE: Followed this tutorial and utilized the Django web application development framework for a majority of the production of this web application.  Significant amounts of code utilized throughout this project in areas such as models, views, urls, templates, etc. follow this tutorial very closely.*
