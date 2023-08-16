from typing import List
from db import db
from model import ItemModel
from datetime import date


def add_item(item_data) -> int or str:
    item = ItemModel(**item_data)
    item.date = date.fromisoformat(date.today().isoformat())
    item.completed = False

    try:
        db.session.add(item)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return item.id


def get_all_items() -> List[ItemModel]:
    items = ItemModel.query.order_by(ItemModel.date.desc()).all()

    return items


def change_item_status(item_id: int) -> int or str:
    item = ItemModel.query.get_or_404(item_id)
    item.completed = not item.completed

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return item.id


def delete_item(item_id: int) -> int or str:
    item = ItemModel.query.get_or_404(item_id)

    try:
        db.session.delete(item)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return item.id

