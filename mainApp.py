from flask import Flask

app = Flask(__name__)


@app.route('/botCall')
def hello():
    return 'Hello, bot!'


def main():
    app.run()


if __name__ == '__main__':
    main()