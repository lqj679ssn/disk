""" Adel Liu 180111

用户API处理函数
"""

from Base.decorator import require_login, require_get, require_delete, require_root
from Base.error import Error
from Base.jtoken import jwt_e
from Base.response import response, error_response

from User.models import User


def get_token_info(o_user):
    ret = jwt_e(dict(user_id=o_user.pk))
    if ret.error is not Error.OK:
        return error_response(ret)
    token, dict_ = ret.body
    dict_['token'] = token
    dict_['avatar'] = o_user.get_avatar_url()
    return dict_


@require_get()
@require_login
def get_my_info(request):
    """ GET /api/user/

    获取我的信息
    """
    o_user = request.user
    return get_user_info(request, o_user.username)


@require_get()
def get_user_info(request, username):
    """ GET /api/user/@:username

    获取用户信息
    """
    ret = User.get_user_by_username(username)
    if ret.error is not Error.OK:
        return error_response(ret)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)
    return response(body=o_user.to_dict())


@require_delete()
@require_root
def delete_user(request, username):
    """ DELETE /api/user/@:username

    删除用户
    """

    ret = User.get_user_by_username(username)
    if ret.error is not Error.OK:
        return error_response(ret)
    o_user = ret.body
    if not isinstance(o_user, User):
        return error_response(Error.STRANGE)
    o_user.delete()
    return response()
