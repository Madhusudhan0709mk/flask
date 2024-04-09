from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    res = ''
    if request.method == 'POST':
        name = str(request.form['name'])
        age = str(request.form['age'])
        res =  f' the result is {name} score is {age}'
    return render_template('index.html', res=res)

# @app.route('/submit',methods=['POST','GET'])
# def submit():
#     if request.method == 'POST':
#         name = str(request.form['name'])
#         age = str(request.form['age'])
#         res = f'my name is {name} and age is {age}'
#         return render_template('index.html',res=res)
        

# @app.route('/success/<int:score>')
# def success(score):
#     return "the person has passed and the marks is "+str(score)

# @app.route('/success/<int:score>')
# def fail(score):
#     return "the person has failed and the marks is "+str(score)

# @app.route('/success/<int:marks>')
# def result(marks):
#     if marks >=50:
#         result = "passed"
#     else:
#         result = "fail"
#     # return f' the result is {result} score is {score}'
#     return render_template('index.html', marks=marks, result=result)

if __name__ == '__main__':
    app.run(debug=True)