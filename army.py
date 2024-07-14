from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fighter.db'
db = SQLAlchemy(app)
class units(db.Model):
    __tablename__ = 'all_units'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    unit = db.Column(db.String(20))
    damage = db.Column(db.Integer)
    armor = db.Column(db.Integer)
    skill = db.Column(db.String(100))

    def __init__(self, unit, damage, armor, skill):
        self.unit = unit
        self.damage = damage
        self.armor = armor
        self.skill = skill


class MyForm(FlaskForm):
    unit = StringField('unit', validators=[DataRequired()])
    damage = IntegerField('damage', validators=[DataRequired()])       
    armor = IntegerField('armor', validators=[DataRequired()]) 
    skill = StringField('skill', validators=[DataRequired()]) 


@app.route("/")
def start():
    return render_template('start_p.html')


@app.route("/all_units", methods = ['GET', 'POST'])
def all_units():
    x = units.query.all()
    return render_template('main.html', un = x )


@app.route("/new", methods = ['GET', 'POST'])
def new():
    form = MyForm()
    if form.validate_on_submit():
        res_unit = form.data['unit']
        res_damage = form.data['damage']
        res_armor = form.data['armor']
        res_skill = form.data['skill']
        new_user = units(res_unit, res_damage, res_armor, res_skill)
        db.session.add(new_user)
        db.session.commit()
        x = units.query.all()
        return render_template('main.html', un = x )
    return render_template('wtf.html', form = form)

















if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()