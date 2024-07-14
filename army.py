from flask import Flask, request, render_template
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

    def __init__(self, id, unit, damage, armor, skill):
        self.id = id
        self.unit = unit
        self.damage = damage
        self.armor = armor
        self.skill = skill


class MyForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    unit = StringField('unit', validators=[DataRequired()])
    damage = IntegerField('damage', validators=[DataRequired()])       
    armor = IntegerField('armor', validators=[DataRequired()]) 
    skill = IntegerField('skill', validators=[DataRequired()]) 


@app.route("/")
def hello():
    return 'Создай свою армию если не трус'


@app.route("/all_units", methods = ['GET', 'POST'])
def all_units():
    x = units.query.all()
    # for i in x:
    #     print (i.unit)
    return render_template('main.html', un = x )




















if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run()