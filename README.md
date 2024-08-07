### Energy Backend
- This project is designed to manage D0010 files that have meter reading data.The project contains a model that has meters and readings.It also includes a management command and an admin interface for managing data

Built with:
```shell
Python version 3
Django
```
#### Setting up the project

- Clone the project using git clone from Github: ```https://github.com/Marlinekhavele/energy_code_challenge```
- Enter the project directory i.e ```cd app```
- create virtual environment
```shell
virtualenv env -p python3.11 - use your local python
```
*Activate the virtual env with the below command
```shell
source env/bin/activate
```

##### Install deps:
```shell
pip install -r requirements.txt
```
##### To check django admin you need to create a user using the below command
- `python manage.py createsuperuser` 
```shell
- username: octopusenergy
- password: 12345

```
##### Ensure Database is on the same level
```
python manage.py makemigrations
python manage.py migrate
```
##### Run the project Locally with the below command 
```shell
python manage.py runserver
```

##### Running Tests Locally
```shell
python manage.py test

```
some environment variables you will use inside your `.env`file just copy this.
```shell
DB_USER=postgres
DB_HOST=localhost
DB_NAME=octopus_energy_app
DB_PASSWORD=password
```
##### what to  improve on  this project

- REST API: Implement a RESTful API to allow users to upload D0010 files via the web interface.

- Data Validation: Add data validation checks to ensure that imported D0010 files meet the expected format and standards.

- Error Handling: Implement error handling.

- Testing: write tests for models.

- System design:  see how the app will grow to handle traffic.

- Collaboration: include other engineers on how to improve the project.