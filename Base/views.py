from SmartDjango import Excp, ErrorCenter
from django.views import View


class ErrorView(View):
    @staticmethod
    def get(r):
        """GET /base/errors"""
        return ErrorCenter.all()
