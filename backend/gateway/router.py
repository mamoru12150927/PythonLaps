from flask import Flask , redirect , url_for ,jsonify

app = Flask(__name__)

# 初回はログインを促すためログインページにリダイレクト
@app.route('/')
def index(methods=['GET']) :
    logOn = True 
    url = '/index' if logOn == True else '/redirect'
    app.logger.info('リダイレクトしました。')# 絶対いらない…
    return redirect(url_for('/login'))

@app.route('/login')
def login(methods=['POST', 'GET']) :
    return jsonify({'message': 'please login!'})

@app.route('/auth')
def auth(methods=['POST', 'GET']) :
    return jsonify({'message': 'login OK!'})

@app.route('/userData')
def userData(methods=['POST', 'GET' , 'PUT' , 'DELETE']) :
    return jsonify({'id': '1' , 'userName': 'mamoru12150927' })

@app.route('/rank')
def rank(methods=['POST', 'GET' , 'PUT' , 'DELETE']) :
    return jsonify({'id': '1' , 'userName': 'No1User' })

@app.route('/trend')
def trend(methods=['POST', 'GET' , 'PUT' , 'DELETE']) :
    return jsonify({'id': '1' , 'userName': 'TrendUser' })
