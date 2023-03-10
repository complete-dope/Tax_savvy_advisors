from flask import Flask , render_template , redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html') 


@app.route('/contactUs')
def contactus():
    return render_template('contact_us.html')

@app.errorhandler(404)
def unavailable():
    return redirect('home.html')


if __name__ == '__main__':
    app.run(debug = True)
