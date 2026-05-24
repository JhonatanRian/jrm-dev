
# Project Overview

This is a Django-based portfolio project. It is designed to showcase my work, skills, and projects. The project is also intended to be a platform for future development and experimentation.

detail: Always analyze whether GEMINI.md and the project are aligned.

## Tech Stack

*   **Backend:** Django
*   **Frontend:** Django Templates, HTML, CSS, JS
*   **CSS Framework:** Tailwind CSS (via Standalone CLI v4)
*   **Web Server:** uWSGI
*   **Database:** SQLite (for development)
*   **Dependency Management:** uv
*   **Containerization:** Docker
*   **Python Version:** 3.12+

## Project Structure

The project is organized into the following Django apps:

*   `accounts`: Manages user authentication and registration.
*   `core`: Contains core functionalities, base models, and utilities shared across the project.
*   `portfolio`: Manages the content of the portfolio, including projects, skills, and personal information.

## Business Logic

### Accounts

*   The `User` model is a custom user model that uses email as the username.
*   It includes fields for `name`, `social_name`, and `email`.
*   The `CustomUserManager` is used to handle user creation.

### Core

*   `BaseModel`: An abstract model that provides `created_at` and `updated_at` fields.

### Portfolio

*   `SectionHero`: A model for the hero section of the portfolio.
*   `Stack`: A model to represent a technology or skill.
*   `GroupStack`: A model to group related stacks.
*   `Project`: A model to showcase a project, including its title, description, and repository URL.
*   `Portfolio`: The main model that brings together all the portfolio components, including the hero section, about me, stacks, projects, and social links.

## How to run the project

1.  **Build and run the Docker container:**
    ```bash
    docker-compose up -d --build
    ```
2.  **Access the application:**
    Open your browser and go to [http://localhost:8000](http://localhost:8000)

3.  **Compiling Tailwind CSS (Frontend Development):**
    To watch and automatically compile styles while developing locally, run:
    ```bash
    ./tailwindcss -i ./core/static/css/src/input.css -o ./core/static/css/app.css --watch
    ```
    To build and minify the CSS for production:
    ```bash
    ./tailwindcss -i ./core/static/css/src/input.css -o ./core/static/css/app.css --minify
    ```
