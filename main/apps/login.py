from flask import Blueprint, views

login_bp = Blueprint("login", __name__, url_prefix="/api/v1/login/")


class LoginView(views.MethodView):
    def get(self):
        return {"data": 122}


login_bp.add_url_rule("", view_func=LoginView.as_view("LoginView"))
