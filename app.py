import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, g
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '1f0ec8fcad355ef57a9b1bdf77bf4c19' # Change this to a strong, random key!

# --- Database Functions ---
def get_db_connection():
    """Establishes a connection to the SQLite database."""
    # Using g (global application context) to manage database connection per request
    if 'db' not in g:
        g.db = sqlite3.connect(
            os.path.join(app.root_path, 'instance', 'database.db'), # Path to database.db
            detect_types=sqlite3.PARSE_DATES
        )
        g.db.row_factory = sqlite3.Row # Allows accessing columns by name
    return g.db

@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database connection at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Initializes the database schema."""
    with app.app_context(): # Run within Flask app context
        db = get_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_post(post_id):
    """Fetches a single post by its ID."""
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    if post is None:
        flash('Post not found!', 'error')
        return None
    return post

# --- Routes ---

@app.route('/')
def index():
    """Displays all blog posts."""
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created DESC').fetchall()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=('GET', 'POST'))
def create():
    """Handles creating new blog posts."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!', 'error')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    """Handles editing existing blog posts."""
    post = get_post(id)
    if post is None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!', 'error')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ? '
                         'WHERE id = ?',
                         (title, content, id))
            conn.commit()
            flash('Post updated successfully!', 'success')
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    """Handles deleting blog posts."""
    post = get_post(id)
    if post is None:
        return redirect(url_for('index'))

    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    flash(f"Post '{post['title']}' deleted successfully!", 'success')
    return redirect(url_for('index'))

# --- Run the Application ---
if __name__ == '__main__':
    # Ensure the 'instance' directory exists for the database
    if not os.path.exists(os.path.join(app.root_path, 'instance')):
        os.makedirs(os.path.join(app.root_path, 'instance'))
    
    # Initialize the database if it doesn't exist or is empty
    db_path = os.path.join(app.root_path, 'instance', 'database.db')
    if not os.path.exists(db_path) or os.path.getsize(db_path) == 0:
        print("Initializing database...")
        init_db()
        print("Database initialized.")
    
    app.run(debug=True) # debug=True is good for development, set to False for production