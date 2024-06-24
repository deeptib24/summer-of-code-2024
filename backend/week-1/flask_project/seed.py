from datetime import datetime, timezone
from app import db  
from app.models import InventoryItem, Customer, Transaction

def seed_inventory_items():
    items = [
        InventoryItem(Item_SKU='SKU001', Item_Name='Item 1', Item_Description='water bottle', Item_Price=15, Item_Qty=100),
        InventoryItem(Item_SKU='SKU002', Item_Name='Item 2', Item_Description='chips', Item_Price=10, Item_Qty=50),
        InventoryItem(Item_SKU='SKU003', Item_Name='Item 3', Item_Description='packaged noodles', Item_Price=20, Item_Qty=200)
    ]
    db.session.bulk_save_objects(items)
    db.session.commit()

def seed_customers():
    customers = [
        Customer(c_name='Prerna Gupta', c_email='prerna@example.com', c_contact='1234567890'),
        Customer(c_name='June Smith', c_email='june@example.com', c_contact='9876543210')
    ]
    db.session.bulk_save_objects(customers)
    db.session.commit()

def seed_transactions():
    transactions = [
        Transaction(c_ID=1, t_date=datetime.now(timezone.utc), t_amount=60, t_category='Sales'),
        Transaction(c_ID=2, t_date=datetime.now(timezone.utc), t_amount=30, t_category='Returns')
    ]
    db.session.bulk_save_objects(transactions)
    db.session.commit()

if __name__ == '__main__':
    seed_inventory_items()
    seed_customers()
    seed_transactions()
    print('Database seeding completed.')
