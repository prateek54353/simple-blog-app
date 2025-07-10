# Simple Blog Application

A minimalist full-stack blog application built with Python's Flask framework, SQLite for the database, and traditional HTML, CSS, and JavaScript for the frontend. This project demonstrates core web development concepts, including CRUD operations, database interaction, templating, and handling HTTP requests.

## Features

-   **View Blog Posts:** Browse all existing blog posts on the homepage.
-   **Create New Posts:** Add new blog entries with a title and content.
-   **Edit Existing Posts:** Modify the title and content of published posts.
-   **Delete Posts:** Remove posts from the blog.
-   **Persistent Data:** All blog posts are stored in an SQLite database, ensuring data is saved between application runs.
-   **Flash Messages:** Provides user feedback for successful operations or errors.

## Technologies Used

-   **Backend:** Python (Flask)
-   **Database:** SQLite 3
-   **Frontend:** HTML5, CSS3, Jinja2 (templating)



## Setup and Running

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/simple-blog-app.git](https://github.com/YOUR_USERNAME/simple-blog-app.git)
    cd simple-blog-app
    ```
    (Remember to replace `YOUR_USERNAME` with your actual GitHub username once you upload it)

2.  **Create a Python Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install Flask
    ```

5.  **Initialize the Database:**
    The database (`instance/database.db`) will be automatically created and initialized with the `posts` table schema when you run `app.py` for the first time. If you ever need to reset it, you can delete the `instance/database.db` file.

6.  **Run the Application:**
    ```bash
    python app.py
    ```
    The application will typically run on `http://127.0.0.1:5000/`. Open this URL in your web browser.

## How It Works

-   **`app.py`**: The core of the application. It defines routes, handles HTTP requests (GET for displaying pages, POST for form submissions), interacts with the SQLite database, and renders HTML templates.
-   **`schema.sql`**: A simple SQL script that creates the `posts` table in the SQLite database, defining its columns (`id`, `created`, `title`, `content`).
-   **`templates/`**: Contains Jinja2 HTML files. `base.html` provides the common layout, and `index.html`, `create.html`, `edit.html` extend it to provide specific page content.
-   **`static/css/style.css`**: Provides basic styling for the web pages to make them visually appealing.
-   **`instance/database.db`**: The SQLite database file where blog posts are stored persistently.

