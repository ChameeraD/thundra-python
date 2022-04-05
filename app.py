from flask import Flask
app = Flask(__name__)

from pathlib import Path
from dotenv import load_dotenv
from users import user_api
from posts import post_api

app.register_blueprint(user_api)
app.register_blueprint(post_api)

env_path = Path("example.env").resolve()
load_dotenv(dotenv_path=env_path)

try:
    import tracepointdebug
    tracepointdebug.start()
except ImportError as e:
    print(e)

@app.route('/')
def welcome():
    return '<h1>Hello World!</h1>'


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')