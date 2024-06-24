import re
from datetime import datetime
from app import db
from sqlalchemy import Index
from sqlalchemy import CheckConstraint



class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    id = db.Column(db.Integer, primary_key=True)
    Item_SKU = db.Column(db.String(50), unique=True, nullable=False)
    Item_Name = db.Column(db.String(100), nullable=False)
    Item_Description = db.Column(db.Text)
    Item_Price = db.Column(db.Float)
    Item_Qty = db.Column(db.Integer, default=0)
    def validate_price(self):
        """Validation method to ensure Item_Price is non-negative."""
        if self.Item_Price is None or self.Item_Price < 0:
            raise ValueError('Price must be non-negative.')
    __table_args__ = (
        CheckConstraint('Item_Price >= 0', name='check_item_price'),
        Index('idx_inventory_item_sku', 'Item_SKU'),
    )

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    c_ID = db.Column(db.String(50), unique=True, nullable=False)
    c_name = db.Column(db.String(100), nullable=False)
    c_email = db.Column(db.String(120), unique=True, nullable=False)
    c_contact = db.Column(db.String(20))
    def validate_email_format(self):
        """Validation method to ensure c_email is in a valid format."""
        if not re.match(r'^[\w\.-]+@[\w\.-]+$', self.c_email):
            raise ValueError('Invalid email format.')
    __table_args__ = (
        CheckConstraint("c_email ~* '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'", name='check_customer_email'),
        Index('idx_customer_email', 'c_email'),
    )

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    s_ID = db.Column(db.String(50), unique=True, nullable=False)
    s_name = db.Column(db.String(100), nullable=False)
    s_email = db.Column(db.String(120), unique=True, nullable=False)
    s_isAdmin = db.Column(db.Boolean, default=False)
    s_contact = db.Column(db.String(20))
    __table_args__ = (
        CheckConstraint('s_ID > 0', name='check_staff_id_positive'),
        Index('idx_s_email', 's_email')  # Example of creating an index on s_email
    )

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    t_ID = db.Column(db.String(50), unique=True, nullable=False)
    c_ID = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('transactions', lazy=True))
    t_date = db.Column(db.DateTime, default=datetime.utcnow)
    t_amount = db.Column(db.Float)
    t_category = db.Column(db.String(50))
    __table_args__ = (
        Index('idx_t_date', 't_date'),  # Example of creating an index on t_date
        Index('idx_t_category', 't_category')  # Example of creating an index on t_category
    )
