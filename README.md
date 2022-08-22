# Restaurant 

## Introduction

Welcome to a restaurant schoolproject website from Code Institute. This project the fourth of five Portfolio Projects
inline to be a Full Stack Software Developer. The project is buit with: 
- Django 
- Materialize  
and the data like pitchers and text information is stored with:
- Heroku Postgres, for text information
- Heroku Postgres, for image information  

This project is a Restaurant website where costumers can make online reservation and 
the staff can login and view the reservations.

## Aglie
To create this Restaurant website I have used the Agile strategy of working. In Agile working the
steakholders, project-leader or customers gives feedback or directives 
of what they want or what to improve. This information will be listed by prioritization and 
then worked on by that oredering. This strategy limits the working on:
- what I want to do   
to 
- What should be done  
and  
- what developers thinks is good  
to  
- what costumers, steakholders, project-leaders and developers thinks is good
  
In a team of one this strategy is still good but lacks the full potentaial. However
I set up User Storys on what to prioritize. This was:  
- set up a Django framework for the website
- create a good looking website
- create the ability to send reservation to Restaurant via the website
- beeing able the read the reservations
- restrict costumers from reading the reservations
- create documentation
  
I found that working with this strategy is beneficial in many ways.
A good example of this came to me today when I opened up the website for 
public use. One important feedback was that the form was not good enough, 
the timedate input is not functional on firefox and other overall complications
like that the successfully booking should not fade out etc. 
This however sound verry important but since the project should be submited tomorrow
and the documentation is not done jet. Once again, I would like to fix the best form posible
but I should first fix the documentation first.


## Django
Django is Python based framework that with a MVT structure.
- Model
- view
- template 

### template
The template is the basic html css and js informationer that get shown as a response by the request of the user.

### Model 
The Model handels the sql inforamtion, here you set up what type of inforamtion should be framed and under what table.
The information can have cross information with other tables and how this relationship is is set up in the Model. Django 
automaticly from the classes in the model set up sql code for the ability to talk to the database. 

### view 
The template and model information is summed up in the view, here the request, responce and redirect of data-logic is beeing used.
Example the decorator @login_required on the view for bookings restrict the responce from the user to see all the reservations without 
loggin in.  

## Materialize
This is a responsive website, meaning it works on all platforms.
Materialize like Bootstrap is a css and js helper that simplify 
flex wraping grids and ease of design. 
A grid spans from 12 to 1 where 12 is max width of the container and 
1 is 1/12 of the max width. 12 is used because the high number of partions.
s12 m6 mening in small devices use full with where medium size or bigger use half the width.
 
  
## Design
  
### Colour Scheme
There are alot of colors in this website, one beneficiary of Materialize us the color palette which is plenty.
In general the palette is at the brighter side and convey a feeling of freshness. Normaly red is used with food content 
becouse it tend to makes use more hungry. But I believe the overuse of big buisness in this skewness with focus on 
buisness strategy instead of product quality has reached its point and the new red is common color of nature.
Becouse health and nature is priceless, eg higher price by choice. 

### Image
The image comes from [Unsplash](https://unsplash.com/) and [Materialize](https://materializecss.com/).


## Features
### navbar
The contains of links to:
- [Home, Menu, Reservation, Bookings, Login/out]  
The links is stored in a collapsed navbar if size is mobile size. Some links are restricted to login authentication.

### index
The index page contains nothing information, extra links and parallax images. A big part of Materialize mentality is to 
present 3d illusion on a 2d plane and parallax helps to create the depth.

### Menu
The menu page contains three typs of menu, one  for breakfast, one for lunch and last for dinner. They are more estetical then functional.
On all sections are speedlinks that that autoscroll to breakfast, lunch or dinner. 

### booking 
This page contains of the reservation form. On the top messages will be presented if the form was submited successfully or not.
The form information get sent to the database and is later beeing used by staff to know when reservaton is. 

### Reservatons
In this page (restaurant) the staff can se what reservation is comming. If the reservation is today is will be colour light green 
and if the reservation contains extra information the will be a post-it container with that information.

### Login, Signout, 




