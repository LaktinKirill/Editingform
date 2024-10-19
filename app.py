from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']


        return redirect(url_for('edit_profile'))

    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)