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
virtualenv env -p python3.11
```
- Activate the virtual env with the below command
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
```shell
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

##### Features

- Import D0010 flow files via management command
- Admin interface to search for readings by MPAN or meter serial number
- Model structure representing Meter Points, Meters


##### what to  improve on  this project

- REST API: Implement a RESTful API to allow users to upload D0010 files via the web interface.

- Data Validation: Add data validation checks to ensure that imported D0010 files meet the expected format and standards.

- Error Handling: Implement error handling.

- System design:  see how the app will grow to handle traffic.

- Collaboration: include other engineers on how to improve the project.





# Octopus Energy Technical Challenge

This project is a Django application for processing D0010 flow files containing meter reading information.

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

## Usage

To import a D0010 file:
```
python manage.py import_d0010 path/to/your/file.txt
```

Access the admin interface at http://localhost:8000/admin to view imported data.

## Running Tests

To run the test suite:
```
python manage.py test
```


1.Validation: Add more robust validation for each line type and field.
2.Logging: Implement detailed logging for better tracking of import processes.
3.Performance: For large files, consider using bulk_create() to improve import speed.
4.Configuration: Make the file structure and field mappings configurable for flexibility.
5Testing: Create unit tests to ensure the import process handles various scenarios correctly.


How does a correct data looks like 