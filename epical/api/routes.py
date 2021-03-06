from flask import Blueprint
from flask_restful import Api

from .resources.covid_epidemiology import (
    CovidSeaichurDResource,
    CovidSeirDResource,
    CovidSirDResource,
)
from .resources.department import DepartmentListResource
from .resources.district import DistrictListResource
from .resources.province import ProvinceListResource
from .resources.user import (
    UserForgotPasswordResource,
    UserListResource,
    UserLoginResource,
    UserResetPasswordResource,
    UserSendEmail,
    UserVerifyAccount,
)

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")
api_rest = Api(api_bp)


api_rest.add_resource(CovidSirDResource, "/sird")
api_rest.add_resource(CovidSeirDResource, "/seird")
api_rest.add_resource(CovidSeaichurDResource, "/seaichurd")
api_rest.add_resource(UserListResource, "/users")
api_rest.add_resource(UserLoginResource, "/user/login")
api_rest.add_resource(UserForgotPasswordResource, "/user/forgot-password")
api_rest.add_resource(UserResetPasswordResource, "/user/reset-password")
api_rest.add_resource(UserSendEmail, "/user/resend-email")
api_rest.add_resource(DepartmentListResource, "/departments")
api_rest.add_resource(
    ProvinceListResource, *["/provinces", "/<int:department_id>/provinces"]
)
api_rest.add_resource(
    DistrictListResource, *["/districts", "/<int:province_id>/districts"]
)
api_rest.add_resource(UserVerifyAccount, "/user/verify-account")
