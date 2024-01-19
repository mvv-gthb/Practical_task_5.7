from flask import Flask, request, render_template
from ceaser import shift
import click
import psycopg2

app = Flask(__name__)

db_host = '172.20.0.2'
db_port = '5432'
db_name = 'ceaser'
db_user = 'db_user'
db_password = '12345678'

conn = psycopg2.connect(host = db_host, port = db_port, dbname = db_name, user = db_user, password = db_password)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    message = request.form['message']
    key = int(request.form['key'])
    crypted_message = ''.join([shift(key, symbol) for symbol in message])
    cur = conn.cursor()
    cur.execute("INSERT INTO texts (clear, cipher) VALUES (%s, %s)", (message, crypted_message))
    conn.commit()
    cur.close()

    return render_template('write.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
