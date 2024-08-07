### Marline Khavele

# Octopus Energy Challenge

###### This project is designed to manage D0010 files that have meter reading data.The project contains a model that has meters and readings It also includes a management command plus an admin interface for managing data


##### How to run the project 
- This project is not on github, just a zipped folder how to install it is quite easy just unzip the project and rub the below comand 
'''
pip install -r requirements.txt
'''

- Set up database migration 
'''
python manage.py migrate 
'''

- To ensure the project is running locally use this command
'''
python manage.py runserver
'''

- Login to the django admin 

'''
username: octopusenergy
password: 12345
'''

- To run test
'''
python manage.py test

'''

##### what to  improve on  this project

- REST API: Implement a RESTful API to allow users to upload D0010 files via the web interface.

- Data Validation: Add data validation checks to ensure that imported D0010 files meet the expected format and standards.

- Error Handling: Implement error handling.

- Testing: write tests for models.

- System design:  see how the app will grow to handle traffic.

- Collaboration: include other engineers on how to improve the project.