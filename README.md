# Student Management System
Django REST API for Student Management System

## Local Setup Instructions:
* Create an empty folder folder for the project
* Create a virtual environment for this project using virtualenv or venv
* Clone this repo
* Activate your virtual environment and change directory to cloned repo
* Install dependencies `pip install -r requirements.txt`
* Migrate the models `python manage.py migrate`
* Create superuser `python manage.py createsuperuser`
* Access django admin using superuser credentials
* Run the project in your development machine `python manage.py runserver`

* APIs for creating Teacher are under construction, so create teachers using Django Admin Interface for the testing
* APIs to List, Create, Retreive, Update and Delete Students & StudentResults are available at 
  * http://127.0.0.1:8000/api/student/
  * http://127.0.0.1:8000/api/student/<id>
  * http://127.0.0.1:8000/api/student-result/
  * http://127.0.0.1:8000/api/student-result/<id>
  
### * Refer Swagger and Redoc Documentations for the complete details of API schema: 
  * http://127.0.0.1:8000/swagger/
  * http://127.0.0.1:8000/redoc/

----
### # TODO
* Add APIs for Teacher
* Add Permissions and Authentication
