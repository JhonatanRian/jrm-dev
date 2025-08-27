# jrm_dev

This is a personal portfolio project built with Django. It's designed to showcase my skills, projects, and experience.

## Features

*   **Dynamic Portfolio:** Easily update projects, skills, and personal information through the Django admin.
*   **User Authentication:** Secure user registration and login functionality.
*   **Integration Ready:** Includes a model for storing API keys for services like Jira and Gemini.

## Tech Stack

*   **Backend:** [Django](https://www.djangoproject.com/)
*   **Frontend:** HTML, CSS, JavaScript (with Django Templates)
*   **Database:** SQLite (for development)
*   **Dependency Management:** [uv](https://github.com/astral-sh/uv)
*   **Python Version:** 3.12+

## Getting Started

### Prerequisites

*   Python 3.12 or higher
*   `uv` installed (`pip install uv`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/jrm_dev.git
    cd jrm_dev
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```

3.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Project Structure

The project is organized into the following Django apps:

*   `accounts`: Manages user authentication and registration.
*   `core`: Contains core functionalities, base models, and utilities shared across the project.
*   `portfolio`: Manages the content of the portfolio, including projects, skills, and personal information.

## Contributing

Contributions are welcome! If you have any suggestions or find any bugs, please open an issue or submit a pull request.
