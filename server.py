from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
#enter debug: flask --app server.py run --debug
#set flask variable: $env:FLASK_APP = "server.py"
#run VS: python -m flask run

@app.route('/')
def my_home():
    return render_template('/index.html')

# @app.route('/<username>/<int:post_id>')
# def hello(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


# @app.route('/<username>')
# def hello(username=None, post_id=None):
#     return render_template('index.html', name=username)

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/generic.html')
# def generic_page():
#     return render_template('generic.html')
#
# @app.route('/elements.html')
# def elements_page():
#     return render_template('elements.html')

# @app.route('/favicon.ico')
# def blog():
#     return 'this is my blog'


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form(name=None):
    if request.method == 'POST':
        try:
            name = request.form['name']
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('/generic.html', name=name)
        except:
            return 'was not able to save to database'
    else:
        return 'Something went wrong, try again'


def write(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f'\n{email},{name},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,name,message])