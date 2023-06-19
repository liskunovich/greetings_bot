import os

from flask_app import create_app, db
app = create_app()


if __name__ == '__main__':
    host = os.environ.get('FLASK_IP', '0.0.0.0')
    port = os.environ.get('FLASK_PORT', 8000)
    app.run(host=host, port=port)



