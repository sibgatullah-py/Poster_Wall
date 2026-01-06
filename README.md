# Poster_Wall

Poster_Wall is a Django web application for posting, viewing, and managing tweets with image support. It features user authentication (register, login, logout), Tailwind CSS styling, and a clean, responsive UI.

## Features

- User registration, login, and logout
- Create, edit, and delete your own tweets
- Upload images with tweets
- Responsive design with Tailwind CSS
- Only authenticated users can create, edit, or delete tweets

## Tech Stack

- Python 3
- Django 6.0
- Tailwind CSS (via django-tailwind)
- SQLite (default, easy to switch to PostgreSQL/MySQL)
- Pillow (for image uploads)

## Setup

1. **Clone the repository:**
	```bash
	git clone < https://github.com/sibgatullah-py/Poster_Wall.git >
	cd Poster_Wall
	```

2. **Install dependencies:**
	```bash
	pip install -r PosterWall/requirements.txt
	```

3. **Apply migrations:**
	```bash
	python PosterWall/manage.py migrate
	```

4. **Create a superuser (optional, for admin access):**
	```bash
	python PosterWall/manage.py createsuperuser
	```

5. **Run the development server:**
	```bash
	python PosterWall/manage.py runserver
	```

6. **Access the app:**
	- Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register a new account or log in.
- Create, edit, or delete your tweets.
- Upload images with your posts.
- Only your own tweets can be edited or deleted.

## License

This project is for educational purposes.