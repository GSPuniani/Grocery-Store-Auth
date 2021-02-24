from sqlalchemy_utils import URLType
from flask_login import UserMixin
from grocery_app import db
from grocery_app.utils import FormEnum

class ItemCategory(FormEnum):
    """Categories of grocery items."""
    PRODUCE = 'Produce'
    DELI = 'Deli'
    BAKERY = 'Bakery'
    PANTRY = 'Pantry'
    FROZEN = 'Frozen'
    OTHER = 'Other'

class GroceryStore(db.Model):
    """Grocery Store model."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    items = db.relationship('GroceryItem', back_populates='store')
    # Add created_by field to see the user who added the store
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')

    # Include string representations for the drop-down menu
    def __str__(self):
        return f'<Grocery Store: {self.title}>'

    def __repr__(self):
        return f'<Grocery Store: {self.title}>'

class GroceryItem(db.Model):
    """Grocery Item model."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    category = db.Column(db.Enum(ItemCategory), default=ItemCategory.OTHER)
    photo_url = db.Column(URLType)
    store_id = db.Column(
        db.Integer, db.ForeignKey('grocery_store.id'), nullable=False)
    store = db.relationship('GroceryStore', back_populates='items')
    # Add created_by field to see the user who added the item
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_by = db.relationship('User')
    # Add many-to-many relationship between User and GroceryItem
    users_who_shopped = db.relationship(
        'User', secondary='shopping_list', back_populates='shopping_list_items')

# Create a User model with id, username, and password fields
class User(UserMixin, db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    # Add many-to-many relationship between User and GroceryItem
    shopping_list_items = db.relationship(
        'GroceryItem', secondary='shopping_list', back_populates='users_who_shopped')

    # Display username for created_by credits
    def __repr__(self):
        return f'<User: {self.username}>'


shopping_list_table = db.Table('shopping_list',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('grocery_item.id'))
)