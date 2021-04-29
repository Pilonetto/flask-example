from flask import Flask, request, render_template, abort, url_for

app = Flask(__name__)

#Test server
@app.route("/",methods = ['GET'])
def index():
    return "Welcome to Flask Example"

#Simple get example
@app.route("/ping",methods = ['GET'])
def ping():
    return "pong"

#Test if get or post method
@app.route('/getorpost', methods=['GET', 'POST'])
def getorpost():
    if request.method == 'POST':
        return "This is a post"
    elif request.method == 'GET':
        return "This is a get"
    else:
        return ":("

#Get with parameters
@app.route("/sum/<float:num_a>/<float:num_b>", methods = ['GET'])
def sum(num_a, num_b):
    return '''The sum is %.2f ''' % (num_a * num_b)

#render template
@app.route('/page')
def page():
    return render_template('page.html')

#file upload
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('./uploads/uploaded_file.txt')    

# redirect example
@app.route('/redirect')
def _redirect():
    return redirect(url_for('ping'))

# 404 default
@app.errorhandler(404)
def page_not_found(error):
    return "page not found", 404    

#API with JSON
@app.route("/retjson")
def me_api():    
    return {
        "name": "Flask example",
        "document_type": "tutorial for using Flask",
        "created_by": "my",
    }

if __name__ == "__main__":
    app.run()    