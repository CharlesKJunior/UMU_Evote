# app.py
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, Vote
from werkzeug.security import generate_password_hash, check_password_hash

#
from flask import Flask, render_template

#
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vote')
def vote():
    return render_template('vote.html')

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    candidate = request.form['candidate']
    # Process the vote (e.g., save to database)
    flash(f'You voted for {candidate}!', 'success')
    return redirect(url_for('vote'))

if __name__ == '__main__':
    app.run(debug=True)

#
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        if username == 'admin' and password == 'password':  # Example check
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/vote', methods=['GET', 'POST'])
@login_required
def vote():
    if request.method == 'POST':
        candidate = request.form.get('candidate')
        new_vote = Vote(user_id=current_user.id, candidate=candidate)
        db.session.add(new_vote)
        db.session.commit()
        flash('Vote cast successfully!')
        return redirect(url_for('results'))
    return render_template('vote.html')


#


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/vote')
def vote():
    return render_template('vote.html')

if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)
# Example static folder configuration
app.static_folder = 'static'

