<div align="center">
  <img src="https://media.giphy.com/media/MfnJATkfrAIBG/giphy.gif" width="100"/>
  
</div>

<h1><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>Secure Channels Hub</h1>

This is a full-stack project built with Vue.js and Django Rest Framework. The project implements web sockets using Django Channels for real-time communication. The backend provides JWT authentication and RESTful APIs for user authentication (login, register, logout). Redis is used as a backing storage for caching and session management.

## Features

- JWT authentication for secure user login and registration
- RESTful APIs for user authentication
- Web socket implementation using Django Channels
- Real-time communication between clients
- Automatic connection management and heartbeat functionality to ensure active connections
- Custom middleware for authentication and request processing
- Redis for caching and session management


## Technologies used

<div style="display:flex">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
  <img src="https://img.shields.io/badge/Python-1572B6?style=for-the-badge&logo=python&logoColor=F7DF1E" />
  <img src="https://img.shields.io/badge/Django-323330?style=for-the-badge&logo=django&logoColor=F7DF1E" />
  <img src="https://img.shields.io/badge/Redis-white?style=for-the-badge&logo=redis&logoColor=red" />
  <img src="https://img.shields.io/badge/Pinia-orange?style=for-the-badge&logo=pinia&logoColor=red" />
  <img src="https://img.shields.io/badge/Pinia_Persistent-yellow?style=for-the-badge&logo=pinia&logoColor=red&color=orange" />
  <img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />  
  <img src="https://img.shields.io/badge/Django_Channels-blue?style=for-the-badge&logo=django&logoColor=yellow&color=blue" />  
</div>

<h2><img  width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0115.gif" border="0" alt="animated-television-image-0115" />
  Screenshots</h2>


<h2><img width="30px" src="https://www.animatedimages.org/data/media/318/animated-computer-smiley-image-0080.gif" border="0" alt="animated-computer-smiley-image-0080" />  Setup:</h2>


## Backend Setup

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the backend directory: `cd backend`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Start the Django development server: `python manage.py runserver`

## Frontend Setup

1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start the development server: `npm run serve`

## Usage

1. Access the application at [http://localhost:8080](http://localhost:8080)
2. Register a new user or login with an existing account
3. After logging in, you will be redirected to the home page
4. Enter a room name to connect to
5. Start sending messages and see real-time updates from other connected clients


## Contributors

- [Abdul Mueed Shahbaz]([https://github.com/your-username](https://github.com/Abdul-Mueed-Shahbaz))

## License

This project is licensed under the [MIT License](LICENSE).

