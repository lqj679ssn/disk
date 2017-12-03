import base64
from functools import wraps

from django.views.decorators import http

from Base.common import deprint
from Base.response import *

require_post = http.require_POST
require_get = http.require_GET


def require_get_params(r_params):
    """
    需要获取的参数是否在request.GET中存在
    """
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            for require_param in r_params:
                if require_param not in request.GET:
                    return error_response(Error.REQUIRE_PARAM, append_msg=require_param)
            request.POST = request.GET
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def require_params(r_params, decode=True):
    """
    需要获取的参数是否在request.POST中存在
    """
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            for r_param in r_params:
                if r_param in request.POST:
                    if decode:
                        x = request.POST[r_param]
                        try:
                            c = base64.decodebytes(bytes(x, encoding='utf8')).decode()
                        except:
                            return error_response(Error.REQUIRE_BASE64)
                        request.POST[r_param] = c
                else:
                    return error_response(Error.REQUIRE_PARAM, append_msg=r_param)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def require_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.body:
            try:
                request.POST = json.loads(request.body.decode())
            except:
                pass
            return func(request, *args, **kwargs)
        else:
            return error_response(Error.REQUIRE_JSON)
    return wrapper


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        deprint('BGN -- ', func.__name__)
        rtn = func(*args, **kwargs)
        deprint('END --', func.__name__)
        return rtn
    return wrapper


def decorator_generator(verify_func, error_id):
    """
    装饰器生成器
    """

    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if verify_func(request):
                return func(request, *args, **kwargs)
            return error_response(error_id)
        return wrapper
    return decorator


def require_login_func(request):
    jwt_str = request.POST.get('token')
    from Base.jtoken import jwt_d

    ret = jwt_d(jwt_str)
    if ret.error is not Error.OK:
        deprint(ret.error)
        return False
    d = ret.body
    try:
        user_id = d['user_id']
        from User.models import User
        ret = User.get_user_by_id(user_id)
        if ret.error is not Error.OK:
            deprint(ret.error)
            return False
        o_user = ret.body
    except:
        return False
    request.user = o_user
    return True
    # return load_session(request, 'user', once_delete=False) is not None

require_login = decorator_generator(require_login_func, Error.REQUIRE_LOGIN)