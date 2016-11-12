from wtforms.form import Form as BaseForm
from wtforms import fields
from wtforms import validators
from wtforms import ValidationError


class Form(BaseForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request


class InformationForm(Form):
    first_name = fields.StringField('First Name')
    last_name = fields.StringField('Last Name')
    email = fields.StringField('Email', [
        validators.email()
    ])

class ContactForm(Form):
    contact_sport = fields.SelectField('Favorite Contact Sport', [
        validators.Required(),
    ], choices=[
        ('roller derby', 'Roller Derby'),
        ('rugby', 'Rugby'),
        ('lacrosse', 'Lacroasse'),
        ('quidditch', 'Quidditch'),
        ('water polo', 'Water Polo'),
        ('ice hockey', 'Ice Hockey'),
        ('not listed', 'Not Listed'),
        ('na', 'Contact sports suck')
    ])
    wears_contacts = fields.BooleanField('Do you wear contacts?')

class AddressForm(Form):
    street = fields.StringField('Street')
    city = fields.StringField('City')
    state = fields.StringField('State')
    postal = fields.StringField('Postal')
    
class ConfirmationForm(Form):
    confirmed = fields.BooleanField('This is all correct', [
        validators.Required()
    ])