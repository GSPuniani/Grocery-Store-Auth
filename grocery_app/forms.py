from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
# Import the models
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField("Grocery Store Name", validators=[DataRequired()])
    address = StringField("Grocery Store Address", validators=[DataRequired()])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField("Item Name", validators=[DataRequired()])
    address = FloatField("Item Price", validators=[DataRequired()])
    category = SelectField("Item Category", choices=ItemCategory.choices())
    photo_url = StringField("Item Photo URL", validators=[URL()])
    store = QuerySelectField("Store", query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')
