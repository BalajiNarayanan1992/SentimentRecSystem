import model
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def recommendations():
    if request.method == 'POST':
        username = request.form['username']
        dlist = [[]]
        title=['No.', 'Top Recommended Product']
        if len(username) > 0:
            info, dlist = model.recommend(username)
        return render_template('index.html', info=info, data=dlist, headings=title)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)