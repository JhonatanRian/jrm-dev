
# Project Overview

This is a Django-based portfolio project. It is designed to showcase my work, skills, and projects. The project is also intended to be a platform for future development and experimentation.

detail: Always analyze whether GEMINI.md and the project are aligned.

## Tech Stack

* **Backend:** Django
* **Frontend:** Django Templates, HTML, CSS, JS
* **CSS Framework:** Tailwind CSS (via Standalone CLI v4)
* **Web Server:** uWSGI
* **Database:** SQLite (for development)
* **Dependency Management:** uv
* **Containerization:** Docker
* **Python Version:** 3.12+

## Project Structure

The project is organized into the following Django apps:

* `accounts`: Manages user authentication and registration.
* `core`: Contains core functionalities, base models, and utilities shared across the project.
* `portfolio`: Manages the content of the portfolio, including projects, skills, and personal information.

## Business Logic

### Accounts

* The `User` model is a custom user model that uses email as the username.
* It includes fields for `name`, `social_name`, and `email`.
* The `CustomUserManager` is used to handle user creation.

### Core

* `BaseModel`: An abstract model that provides `created_at` and `updated_at` fields.

### Portfolio

* `SectionHero`: A model for the hero section of the portfolio.
* `Stack`: A model to represent a technology or skill.
* `GroupStack`: A model to group related stacks.
* `Project`: A model to showcase a project, including its title, description, and repository URL.
* `Portfolio`: The main model that brings together all the portfolio components, including the hero section, about me, stacks, projects, and social links.

## How to run the project

1. **Build and run the Docker container:**

    ```bash
    docker-compose up -d --build
    ```

2. **Access the application:**
    Open your browser and go to [http://localhost:8000](http://localhost:8000)

3. **Compiling Tailwind CSS (Frontend Development):**
    To watch and automatically compile styles while developing locally, run:

    ```bash
    ./tailwindcss -i ./core/static/css/src/input.css -o ./core/static/css/app.css --watch
    ```

    To build and minify the CSS for production:

    ```bash
    ./tailwindcss -i ./core/static/css/src/input.css -o ./core/static/css/app.css --minify
    ```

## Style and Architecture Rules for URLs (Django)

When generating or modifying `urls.py` files or templates calling URLs, strictly follow the RESTful/CRUD patterns of the Django community:

1. **Always use trailing slashes:** Use `app_name/`, never `app_name`.
2. **Never use leading slashes in urls.py:** Use `path('app_name/', ...)` instead of `path('/app_name/', ...)`.
3. **Standard CRUD Mapping:**
    * List: `app_name/`
    * Create: `app_name/create/`
    * Details: `app_name/<int:pk>/` (or `<uuid:id>`)
    * Update: `app_name/<int:pk>/update/`
    * Delete: `app_name/<int:pk>/delete/`
4. **Namespaces and Nomenclature:** Every app's `urls.py` must define an `app_name`. Route names must be simple and action-focused (e.g., `name='list'`, `name='create'`). In templates/code, always invoke them as `app_name:action` (e.g., `{% url 'app_name:create' %}`).

## Views, Forms, Filters & Models Architecture

When creating core components (Views, Forms, Filters, Models), strictly follow this modular pattern:

1. **Component Organization:** Do not cram all elements into a single `views.py`, `forms.py`, `filters.py`, or `models.py`. Create a module/folder (e.g., `views/admin/`, `forms/`, `filters/`, `models/`) and place one `.py` file per resource (e.g., `stack_view.py`, `stack_form.py`, `stack_filter.py`, `stack.py`). Import these inside the module's `__init__.py` to expose them cleanly.
2. **Permissions Base Class:** All secure views must inherit from a base permission mixin (like `AdminPermissionMixin` or `SystemPermissionsBase`) that inherits from `LoginRequiredMixin` and `UserPassesTestMixin`. Do not apply login requirements randomly on a per-view basis.
3. **List Views Filtering:** When creating List views, prefer using `django-filter` and `django_filters.views.FilterView` to allow future scalability of search and filtering capabilities.
4. **Form Styling & Crispy Theme:** Since the project is configured to use the custom `crispy_neurobrutalist` template pack, forms rendered using crispy do not need manual CSS styling classes (e.g., `w-full p-2 border-2...`) injected on their fields or widgets in Python code. The crispy template tags automatically apply all required Neo-Brutalist styles to the rendered fields.

## Validations & QA

1. **Always Run Checks:** Always run `uv run manage.py check` after finishing any implementation or refactoring to catch missing imports and other configuration errors.

## Custom Rich Text Editor (TipTap) & Content Rendering

The project uses a custom TipTap-based rich text editor for writing post content and sections in the admin panel. 

### How it Works
1. **Interactive Node Views**: In the editor, elements like code blocks are rendered interactively (e.g., displaying language dropdowns, interactive layout wrappers, styling on-the-fly via Lowlight parser).
2. **HTML Serialization**: When content is saved, TipTap serializes the document tree to clean, semantic HTML (e.g. `<pre><code>...</code></pre>`, `<mark class="highlight-neo-green">...</mark>`, `<h2>...</h2>`).
3. **Database Storage**: The generated HTML string is stored directly in the text field of the database model.

### Styles and Effects
- **Mac-Style Terminal Code Blocks**: `<pre>` code containers render with a white title bar, mock macOS-style window controls (red/yellow/green circles), black background, JetBrains Mono font, and side-mounted action/copy buttons.
- **Custom Neo-Brutalist Highlights**: Text formatted as highlight uses `<mark class="highlight-neo-gray|yellow|green">` rendering bold text within a colored capsule block with a thick black border, complete with interactive 3D translation & rotation on hover.
- **Neo-Brutalist Blockquotes**: `<blockquote>` tags render with a thick left-border, italicised text, and Slate/Grey container backgrounds.
- **Headings & Body**: Aligned to use unified typography (Outfit for headings, Inter for body) and balanced neo-brutalist spacing/margins.

### Content Rendering Requirements
Any page displaying content generated by the custom rich text editor (such as the blog detail page or portfolio sections) must configure the following to ensure it renders correctly with all styling and effects:
1. **Apply the `.prose-neo` class wrapper**: The container rendering the HTML (e.g. `{{ post.content|safe }}`) must be wrapped in a container carrying the class `.prose-neo`. This activates the standardized neo-brutalist typography, headers, blockquotes, highlights, and code container CSS rules defined in [input.css](file:///home/jhonatan/projects/jrm_dev/core/static/css/src/input.css).
2. **Include Highlight.js**: Because syntax highlighting tokens (like keyword or comment classes) are not serialized inside the database, the rendering page must load Highlight.js via JavaScript to dynamically tokenize code blocks:
   ```html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
   ```
3. **Trigger Code Block Enhancements**: The template script must loop through all code blocks (`.prose-neo pre`) to call `hljs.highlightElement(code)` and optionally mount interactive controls like copy buttons.

