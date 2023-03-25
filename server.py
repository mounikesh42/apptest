from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/save_info')
def save_info():
    id = request.args.get('id')
    failed = request.args.get('failed')

    if id is not None and failed == 'true':
        with open('info.txt', 'a') as f:
            f.write(f'{id}\t{failed}\n')

    return 'OK'

if __name__ == '__main__':
    app.run(host='192.168.0.20', port=5000)


    app.run()


# http://192.168.1.100:5000/save_info?id=h1&failed=true
