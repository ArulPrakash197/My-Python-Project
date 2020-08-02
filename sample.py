from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register_details', methods=['GET','POST'])
def register_details():
    if request.method == 'POST':
     return redirect(url_for('index'))

    return render_template('register_details.html')


@app.route('/welcome', methods=['GET','POST'])
def welcome():
    return render_template('register_details.html')


if __name__ == "__main__":
    app.run(debug=True)


