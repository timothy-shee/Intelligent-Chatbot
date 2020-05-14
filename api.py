import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='client/build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/api/time')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)