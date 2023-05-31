from flask.views import MethodView
from flask_smorest import Blueprint
from schema import CafeSchema, UpdateCafeSchema, PaginationSchema, PageCafeSchema
import service as service

blp = Blueprint("cafe", __name__)


@blp.route("/cafe")
class AllCafes(MethodView):
    @blp.arguments(PaginationSchema, location='query')
    @blp.response(200, PageCafeSchema)
    def get(self, pagination_params: PaginationSchema):
        page = pagination_params["page"]
        per_page = pagination_params["page_size"]

        return service.get_all_cafes(page=page, per_page=per_page)

    @blp.arguments(CafeSchema)
    @blp.response(201)
    def post(self, cafe_data: CafeSchema):

        return service.create_cafe(cafe_data)


@blp.route("/cafe/<int:cafe_id>")
class OneCafe(MethodView):
    @blp.response(200, CafeSchema)
    def get(self, cafe_id: int):

        return service.get_cafe(cafe_id)

    @blp.arguments(UpdateCafeSchema, location='json')
    @blp.response(200)
    def put(self, updated_data: UpdateCafeSchema, cafe_id: int):

        return service.update_cafe(cafe_id=cafe_id, updated_data=updated_data)

    @blp.response(200)
    def delete(self, cafe_id: int):

        return service.delete_cafe(cafe_id)
