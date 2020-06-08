# Cattlea

## Django web application for an online shop

Features
========

* Shoes and Accessories products
* Registration with email
* Adding default shipping address
* Adding products to shopping cart with custom quantity
* Removing or changing the quantity of items in shopping cart
* Placing an order with the addres to ship to
* Tracking the status of the order
* Marking the order as recieved
* Emails upon registration, placing order, recieving order


Django apps
===========

* **[authentication](https://github.com/VaheAvetikyan/cattlea/tree/master/cattlea/apps/authentication)**
    * **registration**: With custom User model, custom register form
    * **login**: Custom login form
    * **adding address**: Custom address form
    * **account**: Password change, address change
* **[core](https://github.com/VaheAvetikyan/cattlea/tree/master/cattlea/apps/core)**
    * models of Shoes, Accessories which inherites from Products model, with Size and Color models for extending properties
    * index, product views
* **[carts](https://github.com/VaheAvetikyan/cattlea/tree/master/cattlea/apps/carts)**
    * Cart model which includes different items of CartItem model
    * adding to cart and removing from cart done with AJAX requests
* **[orders](https://github.com/VaheAvetikyan/cattlea/tree/master/cattlea/apps/orders)**
    * Order model which includes different items of OrderItem model
* **[emails](https://github.com/VaheAvetikyan/cattlea/tree/master/cattlea/apps/emails)**
    * emails is simple app that generates and sends emailes with functions for different purposes

Translation
===========

Translations done with Django **gettext** module.  
Models are translated with third party app **modeltranslation**  

Style
=====

CSS styles are made with **Bootstrap**

Build
=====

Builds are done with **[Travis](https://travis-ci.org/)**  
Tests written with extension of Django **TestCase**  


Static assets
=============

Served from static folder  


Warning
=======

For proper functionality email settings to be provided in the enviroment

cmd
```
set EMAIL_HOST_USER=''
set EMAIL_HOST_PASSWORD=''
```
or linux
```
export EMAIL_HOST_USER=''
export EMAIL_HOST_PASSWORD=''
```
