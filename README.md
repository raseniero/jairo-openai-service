GitHub Copilot: Here's a sample Django Rest Framework README file:

# Project Name

This is a project for OpenAI interface.

## Installation

1. Clone the repository: `git clone https://github.com/raseniero/jairo-openai-service.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Upgrade pip: `pip install --upgrade pip`
6. Create the initial migration files: `python manage.py makemigrations`
7. Run the migrations: `python manage.py migrate`
8. Create a superuser with the following info username is admin, email is admin@email.com and password is adminpass123: `python manage.py createsuperuser`
9. Create a user with the following username is user, email is user@email.com and password is userpass123: `python manage.py createsuperuser`
10. Start the development server: `python manage.py runserver`

## Usage

The API has the following endpoints:

- `http://127.0.0.1:8000/`: Endpoint

To access the endpoints, send HTTP requests to the corresponding URLs using a tool like `curl` or a REST client like Postman.

## References

- `https://djangoforapis.com/initial-setup/` : Django for APIs Initial Setup
- `https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners` : Django Rest Framework Tutorial

## Testing

To run the unit tests, use the following command: `python manage.py test`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
