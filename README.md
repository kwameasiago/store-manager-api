[![Build Status](https://travis-ci.org/SelaDanti/store-manager-api.svg?branch=develop)](https://travis-ci.org/SelaDanti/store-manager-api)
[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](https://github.com/SelaDanti/store-manager-api/pulls)
[![Coverage Status](https://coveralls.io/repos/github/SelaDanti/store-manager-api/badge.svg?branch=develop)](https://coveralls.io/github/SelaDanti/store-manager-api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/60c87ea49fd604c81112/maintainability)](https://codeclimate.com/github/SelaDanti/store-manager-api/maintainability)

**Store Manager**

Store Manager is a web application that helps store owners manage sales and product inventory 
records. This application is meant for use in a single store. 

**Motivation**

Store manager is an application that aims to easen the life of a store owner and attendants by keeping track of product and sales

**Code style**

The api is constructed using python flask and flask restplus

Testing is done using pytest

Test coverage is done using pytest-cov

**Installation**

Clone the repo to your local machine.

open using python run run.py

open localhost

**Features**

1. Store attendant can search and add products to buyer’s cart. 
2. Store attendant can see his/her sale records but can’t modify them. 
3. App should show available products, quantity and price. 
4. Store owner can see sales and can filter by attendants. 
5. Store owner can add, modify and delete products.
6. Store owner can give admin rights to a store attendant. 
7. Products should have categories. 
8. Store attendants should be able to add products to specific categories. 


**EndPoint Functionality**  					
| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| GET   | /products     | Fetch all products  Get all available products.   | 
| GET   | /products/productId     | Fetch a single product record   | 
| GET   | /sales     | Fetch all sale records  Get all sale records.  | 
| GET   | /sales/saleId     | Fetch a single sale record    | 
| POST   | /products     | Create a product    | 
| POST   | /sales      | Create a sale order    | 

	

**Authors**
Kwame Asiago
