import os

from flask import Flask,render_template,request, redirect,url_for,jsonify

from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels={} #Dict of lists, key-channel-username, value-list of messages

@app.route("/",methods=['GET','POST'])
def index():
    log_in_message=''
    username=request.form.get('username')
    if username not in channels:
        channels[username]=[]
        return redirect(url_for('chat'))
    else:
        log_in_message='You need to enter valid username'
    return render_template ('index.html', log_in_message=log_in_message)

@app.route("/chat",methods=['GET','POST'])
def chat():
    return render_template ('chatroom.html',chats=channels)

@app.route("/my",methods=['GET','POST'])
def my():
    data=channels
    return render_template ('channel2.html',data=data) 

# @app.route("/posts",methods=['POST'])
# def posts():
#     username=request.get_json(force=True, silent=True)['username'] 
#     data=channels[username]
#     # return jsonify(data)
#     return render_template ('channel2.html', data=data) 
 

@socketio.on("new_messages")
def message(json,methods=['GET','POST']):
    username=json['username']
    message=json['message']
    channels[username].append(message)
    print(channels)
    socketio.emit('response',json,broadcast=True)
   
    
    