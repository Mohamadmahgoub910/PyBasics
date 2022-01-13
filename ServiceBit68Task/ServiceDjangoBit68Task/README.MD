# Service-site using Django Framework

this task is a project for applying django in creating product and users can see a list of products
including for authors, only if we made filter the user can only see his products.
So, i made first crud on products to make sure it works you can remove hashes and see simple data
Then I made a serializer using rest frame works and api view and checked them they work

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

You need

- Django framework
- python > 3
- MYSQL || Postgres

###Usage

You could browse the website by running the server using the following command(you need to be in the same folder with manage.py)

```
python manage.py runserver
```

Then you could access the websit by typing
1- http://localhost:8000/api/products ==> get all products with user number who create that product
2- http://localhost:8000/api/product/8 ==> get the product with user_id
3- http://localhost:8000/api/createProduct ==> create product made
4- http://127.0.0.1:8000/api/products/updateProduct/8 ==> update product using id
5- http://127.0.0.1:8000/api/products/deleteProduct/8 ==> delete product using confirmation

<!-- ///////////////////////////////////////////////////////////////////////////////////////// -->
<!-- i should here make a view for users but there is no time for now  -->

6- http://127.0.0.1:8000/api/registerU/ ==> Register User Serializer made
7- http://127.0.0.1:8000/api/getUsers/ ==> get all users who we created
8- http://127.0.0.1:8000/api/getUser/2/ ==> get the user by id

###Future works

## Built With

- [Django Framework]()

## Author

- [ MoMa7goub]
