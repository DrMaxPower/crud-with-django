# Restaurant 
## Introduction
Welcome to a restaurant school project website from Code Institute. This project is the fourth of five Portfolio Projects inline to be a Full Stack Software Developer.
  
The project is built with: 
- Django 
- Materialize  
- Heroku Postgres
- cloudinary

This project is a Restaurant website where customers can make online reservations and 
the staff can log in and view the reservations.
## Agile
To create this Restaurant website I have used the Agile strategy of working. In Agile working the
stakeholders, project-leader, and customers give feedback or directives 
of what they want or what to improve. This information will be listed by prioritization and 
then worked on by that ordering. This strategy limits the working on:
- what I want to do   
to 
- **What should be done**  
and  
- what developers think is good  
to  
- **what customers, stakeholders, project leaders, and developers think are good**
  
In a team of one, this strategy is still good but lacks its full potential. However
I set up User Storys on what to prioritize. This was:  
- set up a Django framework for the website
- create a good-looking website
- create the ability to send reservations to Restaurants via the website
- being able the read the reservations
- restrict customers from reading the reservations
- create documentation
  
I found that working with this strategy is beneficial in many ways.
A good example came to me today when I opened the website for 
public use. One important feedback was that the form was not good enough, 
the timedate input is not functional on firefox, and other overall complications
like that the successfully booking should not fade out, etc. 
This, however, sound very important but since the project should be submitted tomorrow
and the documentation is not done yet. The documentation should be done first even doe I 
would like to fix the form.

## Django
Django is a Python-based framework with an MVT structure.
- Model
- View
- template 

### template
The template is the basic HTML CSS and js information that gets shown as a response to the request of the user.

### Model 
The Model handles the SQL information, here you set up what type of information should be framed and under what table.
The information can have cross information with other tables and how this relationship is set up in the Model. Django automatically from the classes in the model set up SQL code for the ability to talk to the database. 

### view 
The template and model information is summed up in the view, here the request, response, and redirect of data logic are being used.

## Materialize
This is a responsive website, meaning it works on all platforms.
Materialize like Bootstrap is a CSS and js helper that simplifies 
flex wrapping grids and ease of design. 
A grid spans from 12 to 1 where 12 is the max width of the container and 
1 is 1/12 of the max width. 12 is used because of the high number of partitions.
s12 m6 meaning in small devices uses full with where medium size or bigger use half the width.
 
  
## Design
  
### Colour Scheme
There are lots of colors on this website and one advantage of Materialize is the rich color palette. In general, the palette is on the brighter side and conveys a feeling of freshness to this website. Normally red is used with food content because it tends to make us more hungry. But I believe the overuse of red by big businesses, focusing on business strategy instead of product quality, has reached its endpoint. Now the "new red" is the brighter common color of nature. Because health and nature are priceless, eg higher price by choice. 

### Image
The image comes from [Unsplash](https://unsplash.com/) and [Materialize](https://materializecss.com/).

## Features
### navbar
Contains links to:
- [Home, Menu, Reservation, Bookings, Login/out]  
The links are stored in a collapsed navbar in mobile size. Some links are restricted to login authentication.

### Index
The index page contains nothing information, extra links, and parallax images. A big part of Materialize mentality is to present a 3D illusion on a 2D plane and parallax helps to create the depth.

### Menu
The menu page contains three types of menu, one for breakfast, one for lunch, and the last for dinner. They are more esthetical than functional.
On all sections are speed links that auto scroll to breakfast, lunch, or dinner. 

### Booking
This page contains the reservation form. On the top messages will be presented in the form submitted successfully or not.
The form information gets sent to the database and is later used by staff to know info about the reservation. 

### account 
Login, logout, and signup are generated from Django-all auth and designed with Materialize.
the decorator @login_required restricts a hacker uses to access /restaurant by adding it to the URL.

### Restaurant
This page contains all the bookings from today and into the future.
Bookings that has passed today is hidden by js function .hide(). If the booking is today the information block of that booking is displayed in green else white. The list is ordered by time.

## Feature to Implements
- add **Django-materializecss-form** especially for date-time function. right now this function is not ecstatic and not compatible with firefox. High prioritizing for a fully working form with no problems.
- Link booking info with a receipt for cross analyze
- add confirmation that the user has booking has been done successfully. Maby by sending an email or SMS confirmation.
- remove login/logout messages
- move all reservations past date to a new data-table
- restrict booking to opening hours
- restrict the guest number
- add an edit button on bookings for Employees
- add scroll spy from index to menu
- add real content and images
- semi-automated data cleaning for image-formating
- professional domain names

## Issues and Bugs
- firefox users cant select timedate
- on guests' input is sometimes being redirected to info input
- spellings... 
- some parts do not follow pip8

## Deployment
This website uses Django which is a Python-based framework. To host a website built on Python I used Heroku.
Heroku is a Platform as a Service (Paas). On Heroku, the connection to a database (Heroku Postgres) and Cloudinary is set in the config vars.  

In Django/settings the static files were redirected to Cloudinary and sweden-restaurant.herokuapp.com is an ALOWED_HOST. DEBUG = False will reject Django from putting out a small Bible every time something is wrong. This limit pirates from accessing sensitive content. easily.  

I then connected my GitHub project "crude-with-Django" to a Heroku app. Fortunately, my static files were less than the limit for compression and the build went fine.  

## Credits
Big up to Materialize for creating both CSS and js handlers and their templates.  
Code Institute made this website possible with overall setup and content inspiration.



