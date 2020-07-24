from flask import Flask

app = Flask("31")

@app.route('/')
def main():
    return 'hello world!'