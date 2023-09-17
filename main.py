from flask import Flask, request, jsonify, redirect, render_template, session, url_for
from flask_oauthlib.client import OAuth

app = Flask(__name__,template_folder='template',static_url_path='', static_folder='template/css')
app.secret_key = 'GnpKreY9Yhpar5TE'

oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='595265502942-ivqc9gu67s3dcjp6b9v7e6kg3btuqueu.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/')
def index():
    #return function.test_user()
    return redirect('/login')

@app.route('/login')
def login_page():
	return render_template("login_page.html",**locals())

@app.route('/login/google')
def login_google():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/google/authorized')
def authorized():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={0} error={1}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )

    session['access_token'] = response['access_token']
    user_info = google.get('userinfo')
    
    # 將用戶的信息存儲到session
    session['user_info'] = user_info.data

    # 如果認證成功，重定向到chat_page
    return redirect(url_for('chat_page'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('access_token')

@app.route('/guest')
def guest_page():
	return render_template("guest_page.html",**locals())

@app.route('/chat')
def chat_page():
    # 從session中提取email
    user_email = session['user_info'].get('email', '默认邮箱或留空')
    
    return render_template("chat_page.html", email=user_email,**locals())

@app.route('/character')
def character_select_page():
	return render_template("character_select_page.html",**locals())




@app.route('/Project',methods =['POST'])
def login_post():	
	#username = request.form.get('username')
	email = request.form.get('email')
	password = request.form.get('password')
	user = function.login_check(email,password)
	if(user == -1):
		return jsonify({'status':'login_fail'})
	else:
		user_id = user[0]
		username = user[1]
		return jsonify({'status':'login_success','user_id':user_id,'username':username})

if __name__ == "__main__":
    app.run()

