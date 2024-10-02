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

1. Validation: Add more robust validation for each line type and field.
2. Logging: Implement detailed logging for better tracking of import processes.
3. Performance: For large files, consider using bulk_create() to improve import speed.
4. Configuration: Make the file structure and field mappings configurable for flexibility.



