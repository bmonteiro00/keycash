from . import home
from flask import render_template
from redis import Redis, RedisError

redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

@home.route("/", methods=['GET'])
def index():
    return render_template('home/index.html')

@home.route("/telaTipoImovel",  methods=['GET','POST'])
def telaTipoImovel():
    return render_template('home/telaTipoImovel.html')

@home.route("/telaEmail",  methods=['GET','POST'])
def telaEmail():
    return render_template('home/telaEmail.html')