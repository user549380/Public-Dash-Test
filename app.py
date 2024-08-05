from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    # Placeholder for logout functionality
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
