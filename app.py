from flask import Flask, render_template, send_from_directory, request, jsonify
import os
import sqlite3

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'sync_bookmarks.db')


# ============ قاعدة بيانات المزامنة ============
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookmarks (
        sync_code TEXT PRIMARY KEY,
        surah INTEGER NOT NULL,
        ayah INTEGER NOT NULL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

init_db()


# ============ الصفحة الرئيسية ============
@app.route('/')
def index():
    return render_template('index.html')


# ============ خدمة ملفات JSON من الجذر ============
@app.route('/<path:filename>')
def serve_data(filename):
    if not filename.endswith('.json'):
        return jsonify({'error': 'not found'}), 404
    filepath = os.path.join(BASE_DIR, filename)
    if os.path.exists(filepath):
        return send_from_directory(BASE_DIR, filename)
    return jsonify({'error': 'not found'}), 404


# ============ API المزامنة ============
@app.route('/api/sync_bookmark', methods=['POST'])
def save_bookmark():
    data = request.get_json(silent=True) or {}
    code = (data.get('sync_code') or '').strip().upper()
    surah = data.get('surah')
    ayah = data.get('ayah')

    if not code or len(code) < 8:
        return jsonify({'status': 'error', 'message': 'رمز المزامنة غير صالح'}), 400

    try:
        surah = int(surah)
        ayah = int(ayah)
    except (TypeError, ValueError):
        return jsonify({'status': 'error', 'message': 'بيانات غير صالحة'}), 400

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''INSERT INTO bookmarks (sync_code, surah, ayah, updated_at)
                 VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                 ON CONFLICT(sync_code) DO UPDATE SET
                     surah = excluded.surah,
                     ayah = excluded.ayah,
                     updated_at = CURRENT_TIMESTAMP''',
              (code, surah, ayah))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})


@app.route('/api/get_bookmark/<code>', methods=['GET'])
def get_bookmark(code):
    code = code.strip().upper()
    if len(code) < 8:
        return jsonify({'status': 'error'}), 400

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT surah, ayah FROM bookmarks WHERE sync_code = ?', (code,))
    row = c.fetchone()
    conn.close()

    if row:
        return jsonify({'status': 'success', 'surah': row[0], 'ayah': row[1]})
    return jsonify({'status': 'empty'})


@app.route('/api/delete_bookmark', methods=['POST'])
def delete_bookmark():
    data = request.get_json(silent=True) or {}
    code = (data.get('sync_code') or '').strip().upper()
    if not code or len(code) < 8:
        return jsonify({'status': 'error'}), 400

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM bookmarks WHERE sync_code = ?', (code,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
