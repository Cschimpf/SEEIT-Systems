from PL2 import app
from flask import render_template, flash, redirect, request
from PL2.forms import ParkingLotForm
from PL2.parkinglot import ParkingLot, parkingSpot

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html') #can add a title here that will be sent to base.html

@app.route('/parkingform', methods=['GET', 'POST'])
def parkingform():
	parkform = ParkingLotForm()
	if parkform.validate_on_submit():
		p_lot = ParkingLot(request.form['parkingrows'], request.form['parkingcols'])
		p_lot.generateParkingGrid()
	return render_template('parkingform.html', title='Create Parking Lot', form=parkform)

# def ParkingLotGen():
# 	pass
# 	return render_template('parkinglot.html')