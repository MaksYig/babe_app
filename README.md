# BABE_APP (Python Backend and React Frontend)
Python and React Pet managing app. 
BACKEND INSTALL:
1. Clone this repository to your PC
2. In the main folder create your VENV folder and activate it
3. Go back to backend folder and install dependences :
  from mainroot/backend/ *** (be sure that you install it when VENV is activated)
  pip install django pillow djangorestframework djoser 
5. From backend folder run migrations
6. after all backend modules successfully installed, you can runserver command.( it should run on 8000 port
FRONTEND INSTALL:
1. in the root folder, go to /frontend/
2. got to repository  https://github.com/MaksYig/babe_app-frontend and clone all files to Frontend folder
3. from frontend folder run ...../frontend/ npm install - it will install all frontened dependencies
4. ..../frontend/ npm start - for starting react project it should run on 3000 port

The backend side you can use as API by making requests for
:
1.create new user - POST - http://127.0.0.1:8000/api-auth-djoser/users/ (required fields: email, username, password,re_password)
3. Login user with jwt token - POST - http://127.0.0.1:8000/api-auth-djoser/token/login/ (required fields: username, password)- will receive TOKEN
3.update user profile 
4. Logout -POST- http://127.0.0.1:8000/api-auth-djoser/token/logout/ (required header:Authorization Token ........)
5. Get user Info -GET- http://127.0.0.1:8000/api-auth-djoser/users/me/ (required header:Authorization Token ........)
6. Get profile info by user ID - GET - http://127.0.0.1:8000/api/profiles/<int:id>/  (required header:Authorization Token ........)
4.create pet member for authorized user 
5.update and delete pet member for authorized user
6.see pet member information that includes user (owner) information 
