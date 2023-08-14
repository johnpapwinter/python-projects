from db import db
from model import CafeModel
from schema import CafeSchema, PageCafeSchema


def create_cafe(cafe_data):
    cafe = CafeModel(**cafe_data)

    try:
        db.session.add(cafe)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return {"message": "Created"}


def delete_cafe(cafe_id: int):
    cafe = CafeModel.query.get_or_404(cafe_id)

    try:
        db.session.delete(cafe)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return {"message": f"{cafe.id} deleted"}


def get_all_cafes(page: int, per_page: int) -> PageCafeSchema:
    cafes = CafeModel.query.order_by(CafeModel.id).paginate(page=page, per_page=per_page)

    cafe_schema = CafeSchema()
    serialized_items = [cafe_schema.dump(cafe) for cafe in cafes.items]
    result = {
        "page": cafes.page,
        "per_page": cafes.per_page,
        "pages": cafes.pages,
        "total": cafes.total,
        "items": serialized_items
    }

    page_schema = PageCafeSchema()
    return page_schema.dump(result)


def get_cafe(cafe_id: int) -> CafeSchema:
    cafe = CafeModel.query.get_or_404(cafe_id)

    cafe_schema = CafeSchema()
    return cafe_schema.dump(cafe)


def update_cafe(cafe_id: int, updated_data):
    cafe = CafeModel.query.get_or_404(cafe_id)

    if ('has_sockets' in updated_data) and ('has_sockets' != None):
        cafe.has_sockets = updated_data['has_sockets']
    if ('has_toilet' in updated_data) and ('has_toilet' != None):
        cafe.has_toilet = updated_data['has_toilet']
    if ('has_wifi' in updated_data) and ('has_wifi' != None):
        cafe.has_wifi = updated_data['has_wifi']
    if ('can_take_calls' in updated_data) and ('can_take_calls' != None):
        cafe.can_take_calls = updated_data['can_take_calls']
    if ('seats' in updated_data) and ('seats' != None):
        cafe.seats = updated_data['seats']
    if ('coffee_price' in updated_data) and ('coffee_price' != None):
        cafe.coffee_price = updated_data['coffee_price']

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return 500, str(e)

    return {"message": f"{cafe.id} updated"}
