# IT394-Rowe-Prairie-Project
## Link to Deployed Application

## Admin Info
### Project Team - *"No I.T."*
* CDT Prairie, Chase G. '20, Co. C1
  * Email: Chase.Prairie@WestPoint.edu
  * Cell: 253-279-1771
* CDT Rowe, Anton '21, Co. E4
  * Email: Anton.Rowe@WestPoint.edu
  * Cell: 404-453-3333

## Project Overview
This file details various things.
(*NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx *)
### Table of Contents
1. Problem Statement
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
When using the app, cadets will first select a barracks from a dropdown menu, 
select a floor from a dropdown menu, select a room from a dropdown menu, and select the date from a dropdown menu (with
the preset value for date being the current date).  Then, as cadets are inspecting rooms, they can simply scroll down a
checklist of standards, and select a checkmark or "X" mark if a room meets or does not meet a standard.  Cadets will then
click either "Submit" to submit the report, or "Return" to return to the previous page in the event that they 
selected one of the wrong criterion previously, or if they ran out of time to finish the inspection.
Furthermore, Every "X" mark constitutes a gig, so if a cadet submits a report with 3 or more "X"'s checked, the system
will automatically record the room as having failed inspection (or passed if less than 3 "X"'s are checked.

## Testing

## Known Issues

## Recommended Improvements

## Works Cited
* “Atom Beautify.” *Atom*, Atom Text Editor, https://atom.io/packages/atom-beautify.
    * *NOTE: Utilized Atom's Atom-Beautify package in order to format most or all HTML and python files and ensure that they adhere to PEP8 standards (to the best of my knowledge - not 100% sure that the way I ran Atom beautify formatted text to PEP8 standards, but I believe that it did).*

* CDT Prairie, Chase G. '20, Co. C1.  "PRAIRIE IT394 Project Proposal.docx"  28 FEB 2020. 
    * *NOTE: Some of the text for this file was taken from CDT Prairie, Chase '20, Co. C1 IT394 Project Proposal.docx*

* CDT Jenkins, Bernard ’20 Co. C1. (2020, February 28). Personal interview.

* “Django Tutorial - How to Add Bootstrap.” *YouTube.com*, Tech with Tim, 22 Apr. 2019, www.youtube.com/watch?v=0mCZdemSsbs.
    * *NOTE: Followed this tutorial to learn how to use bootstrap with Django*

* Otto, Mark, and Jacob Thornton. “Introduction.” · *Bootstrap*, https://getbootstrap.com/docs/4.0/getting-started/introduction/.
    * *NOTE: Utilized code from bootstrap to add style and aesthetics to the application.  Some code utilized in html pages was copied and pasted directly from this link*

* user2449798user2449798, and Simeon VisserSimeon Visser. “Could Not Parse the Remainder: '[0]' from 'Item[0]' Django.” *Stack Overflow*, 1 July 1963, https://stackoverflow.com/questions/19895894/could-not-parse-the-remainder-0-from-item0-django.
    * *NOTE: Utilized this source to learn how to reference list items in HTML using list.0 instead of list[0]*

* “Writing your first Django app (Tutorial).” *Django*, https://docs.djangoproject.com/en/3.0/intro/tutorial01/.
    * *NOTE: Followed this tutorial and utilized the Django web application development framework for a majority of the production of this web application.  Significant amounts of code utilized throughout this project in areas such as models, views, urls, templates, etc. follow this tutorial very closely.*

