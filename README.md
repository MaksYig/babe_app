# BABE_APP (Python Backend and React Frontend)
Python and React Pet managing app. 
BACKEND INSTALL:
1. Clone this repository to your PC
2. In the root folder create your VENV virtual environment folder and activate virtual environment
root/ - run  python -m venv --your venvname--
cd/--your venvname--/Scripts/activate.bat
after this, in root folder you will have 2 folders backend and venv
3. Go back to backend folder and install dependences :
  from root/backend/ *** (be sure that you install it when VENV is activated)
  pip install django pillow djangorestframework djoser corsheaders djangorestframework-gis==0.3
4. Need to create PostageSQL db. Change in settings.py username and password for you db.
In your PostageSQL db need to CREATE EXTENSION postgis 
5. From backend folder run migrations
6. after all backend modules successfully installed, you can runserver command.( it should run on 8000 port
FRONTEND INSTALL:
1. in the root folder, go to /frontend/
2. got to repository  https://github.com/MaksYig/babe_app-frontend and clone all files to Frontend folder
3. from frontend folder run ...../frontend/ npm install - it will install all frontend dependencies
4. ..../frontend/ npm start - for starting react project it should run on 3000 port

The backend side you can use as API, making requests to:
1. Create new user - POST - http://127.0.0.1:8000/api-auth-djoser/users/ (required fields: email, username, password,re_password)
2. Login user with jwt token - POST - http://127.0.0.1:8000/api-auth-djoser/token/login/ (required fields: username, password)- will receive TOKEN
3. Update user profile-PATCH - http://127.0.0.1:8000/api/user/profile/<int:id>/ (required header:Authorization Token ........)
4. Logout -POST- http://127.0.0.1:8000/api-auth-djoser/token/logout/ (required header:Authorization Token ........)
5. Get user Info -GET- http://127.0.0.1:8000/api-auth-djoser/users/me/ (required header:Authorization Token ........)
6. Get profile info by user ID - GET - http://127.0.0.1:8000/api/profiles/<int:id>/  (required header:Authorization Token ........)
7. Create pet member for authorized user - POST -  http://127.0.0.1:8000/api/listings/create/ (required header:Authorization Token ........)
8. Update pet member for authorized user - PATCH - http://127.0.0.1:8000/api/listings/update/<int:id>/  (required header:Authorization Token ........)
9. Delete pet member for authorized user - DELETE - http://127.0.0.1:8000/api/listings/delete/<int:id>/ (required header:Authorization Token ........)
10. See pet member information that includes user (owner) information - GET - http://127.0.0.1:8000/api/listings/info/<int:id>/
