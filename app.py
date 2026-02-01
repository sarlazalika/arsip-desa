from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os
from datetime import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_desa'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Pastikan folder upload ada
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def get_db_connection():
    conn = sqlite3.connect('arsip.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    # Tabel Arsip
    conn.execute('''
        CREATE TABLE IF NOT EXISTS archives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT,
            description TEXT,
            file_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabel User (Admin)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Cek apakah user admin sudah ada, jika belum buat default
    user = conn.execute('SELECT * FROM users WHERE username = "admin"').fetchone()
    if not user:
        # Default pass: 123
        hashed_pw = generate_password_hash('123')
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', hashed_pw))
    
    conn.commit()
    conn.close()

# Inisialisasi DB
init_db()

# Decorator untuk Login Required
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login berhasil! Selamat datang.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah.', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))

@app.route('/settings', methods=('GET', 'POST'))
@login_required
def settings():
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
        
        if not check_password_hash(user['password'], old_password):
            flash('Password lama salah.', 'danger')
        elif new_password != confirm_password:
            flash('Konfirmasi password baru tidak cocok.', 'danger')
        else:
            new_hashed = generate_password_hash(new_password)
            conn.execute('UPDATE users SET password = ? WHERE id = ?', (new_hashed, session['user_id']))
            conn.commit()
            flash('Password berhasil diubah!', 'success')
            
        conn.close()
        return redirect(url_for('settings'))
        
    return render_template('settings.html')

@app.route('/')
@login_required
def index():
    query = request.args.get('q', '')
    category_filter = request.args.get('category', '')

    sql = 'SELECT * FROM archives WHERE 1=1'
    params = []

    if query:
        sql += ' AND (title LIKE ? OR description LIKE ?)'
        params.extend([f'%{query}%', f'%{query}%'])

    if category_filter:
        sql += ' AND category = ?'
        params.append(category_filter)

    sql += ' ORDER BY created_at DESC'

    # Statistics & Pagination
    stats_conn = get_db_connection()
    
    # Pagination Config
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page
    
    # Get Total Count for Pagination (Filtering applied)
    count_sql = 'SELECT COUNT(*) FROM archives WHERE 1=1'
    count_params = []
    
    if query:
        count_sql += ' AND (title LIKE ? OR description LIKE ?)'
        count_params.extend([f'%{query}%', f'%{query}%'])
    if category_filter:
        count_sql += ' AND category = ?'
        count_params.append(category_filter)
        
    conn = get_db_connection()
    total_records = conn.execute(count_sql, count_params).fetchone()[0]
    import math
    total_pages = math.ceil(total_records / per_page)
    
    # Sort Config
    sort_order = request.args.get('sort', 'desc')
    
    # Executing search query with Limit
    # Update Order By based on sort param
    if sort_order == 'asc':
        sql = sql.replace('ORDER BY created_at DESC', 'ORDER BY created_at ASC')
        
    sql += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    
    archives = conn.execute(sql, params).fetchall()
    
    # Get Stats (Total Global)
    total_stats = conn.execute('SELECT COUNT(*) FROM archives').fetchone()[0]
    
    # Get Category Stats
    category_stats = conn.execute('SELECT category, COUNT(*) as count FROM archives GROUP BY category').fetchall()
    
    conn.close()
    
    return render_template('index.html', archives=archives, query=query, category_filter=category_filter, 
                           total_stats=total_stats, category_stats=category_stats,
                           page=page, total_pages=total_pages, total_records=total_records, sort_order=sort_order)

@app.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        file = request.files['file']
        
        file_path = None
        if file:
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path = filename

        conn = get_db_connection()
        conn.execute('INSERT INTO archives (title, category, description, file_path) VALUES (?, ?, ?, ?)',
                     (title, category, description, file_path))
        conn.commit()
        conn.close()
        flash('Data arsip berhasil ditambahkan!', 'success')
        return redirect(url_for('index'))

    return render_template('form.html', action='Add')

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
@login_required
def edit(id):
    conn = get_db_connection()
    archive = conn.execute('SELECT * FROM archives WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']
        file = request.files['file']
        
        new_file_path = archive['file_path']
        if file:
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_file_path = filename
            # Opsional: Hapus file lama jika ada

        conn.execute('UPDATE archives SET title = ?, category = ?, description = ?, file_path = ? WHERE id = ?',
                     (title, category, description, new_file_path, id))
        conn.commit()
        conn.close()
        flash('Data arsip berhasil diperbarui!', 'success')
        return redirect(url_for('index'))

    conn.close()
    return render_template('form.html', archive=archive, action='Edit')

@app.route('/delete/<int:id>', methods=('POST',))
@login_required
def delete(id):
    conn = get_db_connection()
    archive = conn.execute('SELECT * FROM archives WHERE id = ?', (id,)).fetchone()
    if archive and archive['file_path']:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], archive['file_path']))
        except:
            pass # File mungkin sudah tidak ada
            
    conn.execute('DELETE FROM archives WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Arsip berhasil dihapus!', 'danger')
    return redirect(url_for('index'))

@app.route('/download/<filename>')
@login_required
def download_file(filename):
    from flask import send_from_directory
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
