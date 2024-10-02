### Energy Backend
- This project is designed to manage D0010 files that have meter reading data.The project contains a model that has meters and readings.It also includes a management command and an admin interface for managing data

1. ### Built with:
```shell
Python3.11
Django
```
2. ### Setting Up PostgreSQL Database

1. #### Install PostgreSQL:
   ```shell
   # Ubuntu
   - sudo apt-get update
   - sudo apt-get install postgresql postgresql-contrib
   # macOS
   - brew install postgresql

  # Switch to the PostgreSQL user
  - sudo -i -u postgres

  # Open PostgreSQL shell
  -  psql

  # Create a new user 
  - CREATE USER postgres WITH PASSWORD 'password';

  # Create the database
  - CREATE DATABASE octopus_energy_app;

  # Grant privileges to the user
  - GRANT ALL PRIVILEGES ON DATABASE octopus_energy_app TO postgres;

  # Exit the PostgreSQL shell
   - \q
```

3. #### Setting up the project

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
1. Import D0010 flow files via management command
2. Admin interface to search for readings by MPAN or meter serial number
3. Model structure representing Meter Points, Meters and Reading

##### what to  improve on  this project
1. Validation: Add more robust validation for each line type and field.
2. Logging: Implement detailed logging for better tracking of import processes.
3. Performance: For large files, consider using bulk_create() to improve import speed.
4. Configuration: Make the file structure and field mappings configurable for flexibility.



