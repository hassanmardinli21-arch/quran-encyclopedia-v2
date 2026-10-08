from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

DB_PATH = 'sync.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookmarks (
        sync_code TEXT PRIMARY KEY,
        surah INTEGER,
        ayah INTEGER,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS special_bookmarks (
        id TEXT PRIMARY KEY,
        sync_code TEXT,
        label TEXT,
        surah INTEGER,
        ayah INTEGER,
        created INTEGER
    )''')
    conn.commit()
    conn.close()

# ✅ إصلاح حرج: نُشغّل init_db عند تحميل الملف وليس فقط عند التشغيل المباشر
init_db()

# --- خدمة الملفات الثابتة من مجلد static ---
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# --- API المزامنة ---
@app.route('/api/sync_bookmark', methods=['POST'])
def sync_bookmark():
    try:
        data = request.get_json()
        code = data.get('sync_code')
        surah = data.get('surah')
        ayah = data.get('ayah')
        if not code:
            return jsonify({'status': 'error', 'message': 'missing code'}), 400
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''INSERT OR REPLACE INTO bookmarks (sync_code, surah, ayah, updated_at)
                     VALUES (?, ?, ?, CURRENT_TIMESTAMP)''', (code, surah, ayah))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/get_bookmark/<code>', methods=['GET'])
def get_bookmark(code):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT surah, ayah FROM bookmarks WHERE sync_code = ?', (code,))
        row = c.fetchone()
        conn.close()
        if row:
            return jsonify({'status': 'success', 'surah': row[0], 'ayah': row[1]})
        return jsonify({'status': 'empty'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/delete_bookmark', methods=['POST'])
def delete_bookmark():
    try:
        data = request.get_json()
        code = data.get('sync_code')
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM bookmarks WHERE sync_code = ?', (code,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/special_bookmarks', methods=['POST'])
def save_special():
    try:
        data = request.get_json()
        code = data.get('sync_code')
        bookmarks = data.get('bookmarks', [])
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM special_bookmarks WHERE sync_code = ?', (code,))
        for b in bookmarks:
            c.execute('''INSERT OR REPLACE INTO special_bookmarks (id, sync_code, label, surah, ayah, created)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (str(b.get('id')), code, b.get('label'),
                       b.get('surah'), b.get('ayah'), b.get('created', 0)))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/special_bookmarks/<code>', methods=['GET'])
def get_special(code):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT id, label, surah, ayah FROM special_bookmarks WHERE sync_code = ?', (code,))
        rows = c.fetchall()
        conn.close()
        bookmarks = [{'id': r[0], 'label': r[1], 'surah': r[2], 'ayah': r[3]} for r in rows]
        return jsonify({'status': 'success', 'bookmarks': bookmarks})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
