from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Vote, Candidate
import os
from sqlalchemy.exc import IntegrityError
#from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "voting.db")}'
db.init_app(app)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('home.html')

#
def calculate_winner():
    from sqlalchemy import func
    results = db.session.query(
        Candidate.name, func.count(Vote.id).label('votes')
    ).join(Vote).group_by(Candidate.name).order_by(func.count(Vote.id).desc()).all()
    winner = results[0] if results else None
    print(f'The current winner is {winner[0]} with {winner[1]} votes.')

#scheduler = BackgroundScheduler()
#scheduler.add_job(func=calculate_winner, trigger='interval', hours=24)
#scheduler.start()
#

#@app.route('/register', methods=['GET', 'POST'])
#def register():
 #   if request.method == 'POST':
  #      username = request.form.get('username')
   #     password = request.form.get('password')
    #    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
     #   #hashed_password = generate_password_hash(password, method='sha256')
      #  new_user = User(username=username, password=hashed_password)
       # db.session.add(new_user)
        #db.session.commit()
        #flash('Registration successful!')
        #return redirect(url_for('login'))
    #return render_template('register.html')
    
#
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))
    return render_template('register.html')
#

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

#@app.route('/vote', methods=['GET', 'POST'])
#@login_required
#def vote():
 #   if request.method == 'POST':
  #      candidate = request.form.get('candidate')
   #     new_vote = Vote(user_id=current_user.id, candidate=candidate)
    #    db.session.add(new_vote)
     #   db.session.commit()
   #     flash('Vote cast successfully!')
    #    return redirect(url_for('results'))
    #return render_template('vote.html')
    
@app.route('/vote', methods=['GET', 'POST'])
@login_required
def vote():
    candidates = Candidate.query.all()
    if request.method == 'POST':
        candidate_id = request.form.get('candidate')
        existing_vote = Vote.query.filter_by(user_id=current_user.id, candidate_id=candidate_id).first()
        if existing_vote:
            flash('You have already voted for this candidate.')
            return redirect(url_for('vote'))
        new_vote = Vote(user_id=current_user.id, candidate_id=candidate_id)
        db.session.add(new_vote)
        db.session.commit()
        flash('Vote cast successfully!')
        return redirect(url_for('results'))
    return render_template('vote.html', candidates=candidates)

    #
@app.route('/results')
@login_required
def results():
    from sqlalchemy import func
    results = db.session.query(
        Candidate.name, func.count(Vote.id).label('votes')
    ).join(Vote).group_by(Candidate.name).order_by(func.count(Vote.id).desc()).all()
    
    return render_template('results.html', results=results)

    #

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    candidate = request.form['candidate']
    # Process the vote (e.g., save to database)
    flash(f'You voted for {candidate}!', 'success')
    return redirect(url_for('vote'))



if __name__ == '__main__':
    app.run(debug=True)
