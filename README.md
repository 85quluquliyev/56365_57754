# Domain Reviews

Domain Reviews is a simple Django application that allows users to leave reviews on website domains and see reviews left by others.

## Features

- Add new domains
- Search for domains
- Add reviews to domains
- List reviews for domains
- Pagination for domain listing

## Requirements

- Python 3.6+
- Django 3.2.7
- Bootstrap 4.5.2 (preloaded CSS and JS files)

## Installation

1. Clone the project:

    ```
    git clone https://github.com/85quluquliyev/domain_review.git
    cd domain_review
    ```

2. Create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # Linux and macOS
    venv\Scripts\activate  # Windows
    ```

3. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:

    ```
    python manage.py runserver
    ```

6. Open your web browser and go to:

    ```
    http://127.0.0.1:8000/
    ```
