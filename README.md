# Django Blog Site

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Django](https://img.shields.io/badge/django-3.2%2B-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This is a Django Blog project where users can create, read, update, and delete blog posts.

## Features

- User authentication and authorization
- Create, read, update, and delete (CRUD) operations for blog posts

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default database, can be changed)

## Installation

Follow these steps to get a development environment running.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jaman-dci/django-blog-site.git
   cd django-blog-site
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate

   # On Windows use
   venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Running the Server

To start the server, use:

```bash
python manage.py runserver
```

### Admin Interface

You can access the admin interface at `http://127.0.0.1:8000/admin` using the superuser credentials you created during installation.

### Main Application

Access the main application at `http://127.0.0.1:8000/`. Here, you can read blog posts, create new ones, and interact with the content.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

Please ensure your code adheres to the project's coding conventions and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Feel free to customize this template according to the specifics of your Django Blog project.