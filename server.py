#server.py file
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
#    print(url_for('static', filename='favicon.ico'))
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    # print(url_for('static', filename='favicon.ico'))
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{name},{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # delimiter tells it what to separate the fields with
            # quotechar tells what quote symbol should be used when storing quotes
                # quotechar='' means no quotes.
            # quoting=csv.QUOTE_MINIMAL means only quote when special character.
        csv_writer.writerow([name,email,subject,message])
            # writerow of each of the variables passed in as list.
            # The csv_writer we defined above formats the data.


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # If request method is post..which it is in the submit_form of the html
    if request.method == 'POST':
        #catch errors:
        try:
            # grab data from form into dict called data
            data = request.form.to_dict()
            write_to_csv(data)
            #print data
            print(data)
            #we need to return something:
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    #what if something goes wrong
    else:
        return 'Something went wrong. Please contact admin'

# @app.route('/index.html')
# def index():
#     # print(url_for('static', filename='favicon.ico'))
#     return render_template('index.html')
#
#
# @app.route('/elements.html')
# def elements():
#     return render_template('elements.html')
#
#
# @app.route('/generic.html')
# def generic():
#     return render_template('generic.html')

# @app.route('/')
# def hello_world():
#     return 'Hello, Dude!'


# @app.route('/blog/<username>/<int:post_id>')
# def blog(username=None, post_id=None):
#     return render_template('blog.html', name=username, post_id=post_id)