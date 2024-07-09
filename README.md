# Django my_store Project

This project is a simple e-commerce application built with Django. It includes functionality for managing products, users, shopping carts, and favorites.

## Features

- User authentication and registration
- Product listing and detail pages
- Shopping cart management
- Favorite products management
- Admin interface for managing products, users, and orders

## Technologies Used

- Django
- Django Rest Framework (DRF)
- unittest
- SQLite (default database, can be switched to PostgreSQL, MySQL, etc.)
- HTML/CSS for templating
- JavaScript (optional for frontend interactivity)

# Getting Started

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/imzanuda/my_store.git
   cd my_store

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source venv/bin/activate  # On Windows use ` source venv\Scripts\activate`

3. Install the required packages:

    ```bash
    pip install -r requirements.txt

4. Set up the database:

    ```bash
    python manage.py migrate

5. Create a superuser to access the Django admin:

    ```bash
    python manage.py createsuperuser

6. Run the development server:

    ```bash
    python manage.py runserver

7. Open your browser and go to http://127.0.0.1:8000 to see the application.

## Example Usage
To add a product to the cart:

Send a POST request to /api/cart/ with the following JSON body:

To view the cart items, send a GET request to /api/cart/.

<!-- ### Running Tests
    To run the tests, use the following command:

    ```bash
    python manage.py test -->

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
If you have any questions or suggestions, please open an issue or contact me at [yrslvb@gmail.com].


### Summary of the README File:

1. **Project Title and Description**: Provides a brief overview of the project and its functionality.
2. **Features**: Lists the main features of the project.
3. **Technologies Used**: Mentions the main technologies used in the project.
4. **Getting Started**:
   - Prerequisites: Lists the prerequisites for the project.
   - Installation: Provides step-by-step instructions on how to set up the project locally.
5. **Project Structure**: Describes the structure of the project directory.
6. **API Endpoints**: Lists the main API endpoints with brief descriptions.
7. **Example Usage**: Provides an example of how to use the API to add a product to the cart.
8. **Running Tests**: Instructions on how to run tests for the project.
9. **Contributing**: Guidelines for contributing to the project.
10. **License**: Specifies the license under which the project is released.
11. **Contact**: Provides contact information for questions or suggestions.

Feel free to customize the repository URL, contact email, and any other details specific to your project.
