from pyowm import OWM
from pyowm.utils.config import get_default_config
from flask import Flask, request, session, redirect,url_for
config_dict = get_default_config()
config_dict['language'] = 'ro'  # your language here
owm = OWM('90fb3768dfb833e91fa99785c733f9cf')
V_post="Chisinau"
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        session['Oras'] = request.form['Oras']
        
        return redirect(url_for('result'))
    return '''
        <form method="post">
            <p><input type=text name=Oras>
            <p><input type=submit value=Submit>
        </form>
    '''


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        session['Oras'] = request.form['Oras']

        return redirect(url_for('result'))
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(session['Oras'])
    w = observation.weather
    answer="In "+session["Oras"]+" este "+str(w.detailed_status)+".\nTemperatura !!!(C): "+str(w.temperature('celsius')["temp"])+'''
        <form method="post">
            <p><input type=text name=Oras>
            <p><input type=submit value=Submit>
        </form>
    '''
    return answer


@app.route('/f_except', methods=['GET', 'POST'])
def f_except():
    session['Oras'] = "Chisinau"
    return redirect(url_for('result'))





"""
@app.route('/<oras>', methods=['GET', 'POST'])
def hello(oras):
    if request.method == 'POST':
        session['Oras'] = request.form['Oras']
        return redirect(url_for('hello'))
    
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(oras)
    w = observation.weather
    answer="In "+oras+" este "+str(w.detailed_status)+".\nTemperatura(C): "+str(w.temperature('celsius')["temp"])
    return answer
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
