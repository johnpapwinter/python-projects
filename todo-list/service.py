from db import db
from model import ItemModel
from datetime import date


def add_item(item_data):
    item = ItemModel(**item_data)
    item.date = date.fromisoformat(date.today().isoformat())

    try:
        db.session.add(item)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return {"id": item.id}


def get_all_items():
    items = ItemModel.query.order_by(ItemModel.id)


def change_item_status(item_id: int, new_status: bool):
    item = ItemModel.query.get_or_404(item_id)
    item.completed = new_status

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return {"updated": item.id}


def delete_item(item_id: int):
    item = ItemModel.query.get_or_404(item_id)

    try:
        db.session.delete(item)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return {"deleted": item.id}

