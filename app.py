from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask import Flask,request,url_for,redirect,render_template
app = Flask(__name__,static_url_path='/fakenews/static')
#app.secret_key = config.get('flask', 'secret_key')

@app.route('/fakenews/',methods=['GET'])
def index():
    return render_template('homepage.html')

@app.route('/fakenews/login',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/fakenews/experiment',methods=['GET'])
def experiment():
    return render_template('experiment.html')

@app.route('/fakenews/sign_up',methods=['GET','POST'])
def sign_up():
    return render_template('register.html')

@app.route('/fakenews/dashboard',methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/fakenews/profile', methods=['GET'])
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8521)
