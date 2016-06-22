#Self explanatary form file that takes in a string and a boolean

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class BusinessForm(Form):
    last_name = StringField('last_name', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    address_of_car = StringField('address_of_car', validators=[DataRequired()])

    waterless_wash = BooleanField('waterless_wash', default=False)
    interior_clean = BooleanField('interior_clean', default=False)
    full_detail = BooleanField('full_detail', default=False)
    oil_change = BooleanField('oil_change', default=False)
    tire_rotation = BooleanField('tire_rotation', default=False)
    brakes = BooleanField('brakes', default=False)
    car_to_dealership = BooleanField('car_to_dealership', default=False)
    state_inspection = BooleanField('state_inspection', default=False)
    wiper_replacement = BooleanField('wiper_replacement', default=False)
    cabin_air_filter = BooleanField('cabin_air_filter', default=False)
    engine_air_filter = BooleanField('engine_air_filter', default=False)

    year = StringField('year', validators=[DataRequired()])
    make = StringField('make', validators=[DataRequired()])
    model = StringField('model', validators=[DataRequired()])
    engine_type = StringField('engine_type')
    license_plate = StringField('license_plate')
    color = StringField('color', validators=[DataRequired()])
    misc = StringField('misc')

class RegularForm(Form):
    last_name = StringField('last_name', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    personal_address = StringField('personal_address', validators=[DataRequired()])

    personal_driveway = BooleanField('personal_driveway', default=False)
    street = BooleanField('street', default=False)
    garage_closed = BooleanField('garage_closed', default=False)
    garage_open = BooleanField('garage_open', default=False)
    lot_closed = BooleanField('lot_closed', default=False)
    lot_open = BooleanField('lot_open', default=False)
    address_of_car = StringField('address_of_car', validators=[DataRequired()])

    waterless_wash = BooleanField('waterless_wash', default=False)
    interior_clean = BooleanField('interior_clean', default=False)
    full_detail = BooleanField('full_detail', default=False)
    oil_change = BooleanField('oil_change', default=False)
    tire_rotation = BooleanField('tire_rotation', default=False)
    brakes = BooleanField('brakes', default=False)
    car_to_dealership = BooleanField('car_to_dealership', default=False)
    state_inspection = BooleanField('state_inspection', default=False)
    wiper_replacement = BooleanField('wiper_replacement', default=False)
    cabin_air_filter = BooleanField('cabin_air_filter', default=False)
    engine_air_filter = BooleanField('engine_air_filter', default=False)

    year = StringField('year', validators=[DataRequired()])
    make = StringField('make', validators=[DataRequired()])
    model = StringField('model', validators=[DataRequired()])
    engine_type = StringField('engine_type')
    license_plate = StringField('license_plate')
    color = StringField('color', validators=[DataRequired()])
    misc = StringField('misc')