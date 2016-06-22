from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from .forms import BusinessForm, RegularForm
from .models import BusinessRequest, RegularRequest

#Handlers that respond to requests. Each function is a different URL

@app.route('/')
@app.route('/index')
def index():
    reqs = BusinessRequest.query.all()
    for re in reqs:
      flash('Job %s: <br /><br /> Name: %s %s <br /> E-mail: %s <br /><br /> Year: %s <br /> Make: %s <br /> Model: %s <br /> Engine Type: %s <br /> License Plate: %s <br /> Color: %s <br /> Misc Comments: %s <br /><br /> Waterless Wash: %s <br /> Interior Clean: %s <br /> Full Detail: %s <br /> Oil Change: %s <br /> Tire Rotation: %s <br /> Brakes: %s <br /> Car to Dealership: %s <br /> State Inspection: %s <br /> Wiper Replacement: %s <br /> Cabin Air Filter: %s <br /> Engine Air Filter: %s <br /><br />' %
            (re.id, re.first_name, re.last_name, re.email,re.year, re.make, re.model, re.engine_type, 
              re.license_plate, re.color,re.misc, re.waterless_wash, re.interior_clean,
              re.full_detail, re.oil_change, re.tire_rotation, re.brakes, re.car_to_dealership,
              re.state_inspection, re.wiper_replacement, re.cabin_air_filter, re.engine_air_filter, 
              ))

    reqs = RegularRequest.query.all()
    for r in reqs:
      flash('Job %s: <br /><br /> Name: %s %s <br /> E-mail: %s <br /> Address: %s <br /><br /> Personal Driveway: %s <br /> Street: %s <br /> Closed Garage: %s <br /> Open Garage: %s <br /> Closed Lot: %s <br /> Open Lot: %s <br /> Address of Car: %s <br /><br />  Year: %s <br /> Make: %s <br /> Model: %s <br /> Engine Type: %s <br /> License Plate: %s <br /> Color: %s <br /> Misc Comments: %s <br /><br /> Waterless Wash: %s <br /> Interior Clean: %s <br /> Full Detail: %s <br /> Oil Change: %s <br /> Tire Rotation: %s <br /> Brakes: %s <br /> Car to Dealership: %s <br /> State Inspection: %s <br /> Wiper Replacement: %s <br /> Cabin Air Filter: %s <br /> Engine Air Filter: %s <br /><br />' %
            (r.id, r.first_name, r.last_name, r.email, r.personal_address, r.personal_driveway,
             r.street, r.garage_closed, r.garage_open, r.lot_closed, r.lot_open,
             r.address_of_car, r.year, r.make, r.model, r.engine_type, 
              r.license_plate, r.color, r.misc, r.waterless_wash, r.interior_clean,
              r.full_detail, r.oil_change, r.tire_rotation, r.brakes, r.car_to_dealership,
              r.state_inspection, r.wiper_replacement, r.cabin_air_filter, r.engine_air_filter, 
              ))

    #Renders a template, with the rest of the arguments matching the variable names in the index.html template
    return render_template('index.html',
                           title='Jobs')

@app.route('/form', methods=['GET', 'POST'])
def login():
    form = BusinessForm()
    #validate_on_submit processes the data
    if form.validate_on_submit():
        first_namer = form.first_name.data
        last_namer = form.last_name.data
        emailr = form.email.data
        address_of_carr = form.address_of_car.data

        waterless_washr = form.waterless_wash.data
        interior_cleanr = form.interior_clean.data
        full_detailr = form.full_detail.data
        oil_changer = form.oil_change.data
        tire_rotationr = form.tire_rotation.data
        brakesr = form.brakes.data
        car_to_dealershipr = form.car_to_dealership.data
        state_inspectionr = form.state_inspection.data
        wiper_replacementr = form.wiper_replacement.data
        cabin_air_filterr = form.cabin_air_filter.data
        engine_air_filterr = form.engine_air_filter.data

        yearr = form.year.data
        maker = form.make.data
        modelr = form.model.data
        engine_typer = form.engine_type.data
        license_plater = form.license_plate.data
        colorr = form.color.data
        miscr = form.misc.data

        r = BusinessRequest(first_name = first_namer,last_name = last_namer, email = emailr, address_of_car = address_of_carr,
                            waterless_wash = waterless_washr, interior_clean=interior_cleanr,
                            full_detail = full_detailr, oil_change = oil_changer, tire_rotation = tire_rotationr,
                            brakes = brakesr, car_to_dealership = car_to_dealershipr, state_inspection = state_inspectionr,
                            wiper_replacement = wiper_replacementr, cabin_air_filter = cabin_air_filterr, 
                            engine_air_filter = engine_air_filterr, year = yearr, make = maker, model = modelr, 
                            engine_type = engine_typer, license_plate = license_plater, color = colorr, misc = miscr
                            )

        #db.drop_all()                                                                                                                               
        #db.create_all()
        app.logger.info(r.id)
        db.session.add(r)
        db.session.commit()
        app.logger.info(r.id)

        flash('Here is the summary of you submission: <br /> Name: %s %s <br /> E-mail: %s <br /><br /> Address of Car: %s <br /> Year: %s <br /> Make: %s <br /> Model: %s <br /> Engine Type: %s <br /> License Plate: %s <br /> Color: %s <br /> Misc Comments: %s <br /><br /> Waterless Wash: %s <br /> Interior Clean: %s <br /> Full Detail: %s <br /> Oil Change: %s <br /> Tire Rotation: %s <br /> Brakes: %s <br /> Car to Dealership: %s <br /> State Inspection: %s <br /> Wiper Replacement: %s <br /> Cabin Air Filter: %s <br /> Engine Air Filter: %s <br /><br />' %
            (r.first_name, r.last_name, r.email, r.address_of_car, r.year, r.make, r.model, r.engine_type, 
              r.license_plate, r.color, r.misc, r.waterless_wash, r.interior_clean,
              r.full_detail, r.oil_change, r.tire_rotation, r.brakes, r.car_to_dealership,
              r.state_inspection, r.wiper_replacement, r.cabin_air_filter, r.engine_air_filter, 
              ))

        return redirect('/finished')
    #Just need to make sure that you pass in the objects that are used in the template
    return render_template('login.html', 
                           title='Super Valued Customer',
                           form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegularForm()
    #validate_on_submit processes the data
    if form.validate_on_submit():
        first_namer = form.first_name.data
        last_namer = form.last_name.data
        emailr = form.email.data
        personal_addressr = form.personal_address.data
        address_of_carr = form.address_of_car.data

        personal_drivewayr = form.personal_driveway.data
        streetr = form.street.data
        garage_closedr = form.garage_closed.data
        garage_openr = form.garage_open.data
        lot_closedr = form.lot_closed.data
        lot_openr = form.lot_open.data

        waterless_washr = form.waterless_wash.data
        interior_cleanr = form.interior_clean.data
        full_detailr = form.full_detail.data
        oil_changer = form.oil_change.data
        tire_rotationr = form.tire_rotation.data
        brakesr = form.brakes.data
        car_to_dealershipr = form.car_to_dealership.data
        state_inspectionr = form.state_inspection.data
        wiper_replacementr = form.wiper_replacement.data
        cabin_air_filterr = form.cabin_air_filter.data
        engine_air_filterr = form.engine_air_filter.data

        yearr = form.year.data
        maker = form.make.data
        modelr = form.model.data
        engine_typer = form.engine_type.data
        license_plater = form.license_plate.data
        colorr = form.color.data
        miscr = form.misc.data

        r = RegularRequest(first_name = first_namer,last_name = last_namer, email = emailr, personal_address=personal_addressr,
                            personal_driveway = personal_drivewayr, street = streetr, garage_closed = garage_closedr,
                            garage_open = garage_openr, lot_closed = lot_closedr, lot_open = lot_openr, address_of_car = address_of_carr,
                            waterless_wash = waterless_washr, interior_clean=interior_cleanr,
                            full_detail = full_detailr, oil_change = oil_changer, tire_rotation = tire_rotationr,
                            brakes = brakesr, car_to_dealership = car_to_dealershipr, state_inspection = state_inspectionr,
                            wiper_replacement = wiper_replacementr, cabin_air_filter = cabin_air_filterr, 
                            engine_air_filter = engine_air_filterr, year = yearr, make = maker, model = modelr, 
                            engine_type = engine_typer, license_plate = license_plater, color = colorr, misc = miscr
                            )

        #db.drop_all()                                                                                                                               
        #db.create_all()
        app.logger.info(r.id)
        db.session.add(r)
        db.session.commit()
        app.logger.info(r.id)

        flash('Here is the summary of you submission: <br /><br /> Name: %s %s <br /> E-mail: %s <br /> Address: %s <br /><br /> Personal Driveway: %s <br /> Street: %s <br /> Closed Garage: %s <br /> Open Garage: %s <br /> Closed Lot: %s <br /> Open Lot: %s <br /> Address of Car: %s <br /><br />  Year: %s <br /> Make: %s <br /> Model: %s <br /> Engine Type: %s <br /> License Plate: %s <br /> Color: %s <br /> Misc Comments: %s <br /><br /> Waterless Wash: %s <br /> Interior Clean: %s <br /> Full Detail: %s <br /> Oil Change: %s <br /> Tire Rotation: %s <br /> Brakes: %s <br /> Car to Dealership: %s <br /> State Inspection: %s <br /> Wiper Replacement: %s <br /> Cabin Air Filter: %s <br /> Engine Air Filter: %s <br /><br />' %
            (r.first_name, r.last_name, r.email, r.personal_address, r.personal_driveway,
             r.street, r.garage_closed, r.garage_open, r.lot_closed, r.lot_open,
             r.address_of_car, r.year, r.make, r.model, r.engine_type, 
              r.license_plate, r.color, r.misc, r.waterless_wash, r.interior_clean,
              r.full_detail, r.oil_change, r.tire_rotation, r.brakes, r.car_to_dealership,
              r.state_inspection, r.wiper_replacement, r.cabin_air_filter, r.engine_air_filter, 
              ))

        return redirect('/finished')
    #Just need to make sure that you pass in the objects that are used in the template
    return render_template('signup.html', 
                           title='Super Valued Customer',
                           form=form)

@app.route('/')
@app.route('/finished')
def finished():
    #Renders a template, with the rest of the arguments matching the variable names in the index.html template
    return render_template('finished.html',
                           title='Thank you!')

#loads a users from the database
def load_request(id):
    return BusinessRequest.query.get(int(id))




