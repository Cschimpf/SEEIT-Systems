from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ParkingLotForm(FlaskForm):
	parkingrows = IntegerField('Number of Parking Rows', validators=[DataRequired()])
	parkingcols = IntegerField('Number of Parking Columns', validators=[DataRequired()])
	submitLot = SubmitField('Generate')

