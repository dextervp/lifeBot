from flask import Flask
from flask import Flask,redirect

app = Flask(__name__)
redUrl = 'https://api.telegram.org/bot599314438:AAFLNLeqeIvyJtbqACQj2s4XUPbY9PDHn_c/sendMessage?chat_id=420358659&text=This is a LifeBot'

@app.route('/botCall')
def hello():
    return redirect(redUrl)


def main():
    app.run()


if __name__ == '__main__':
    main()