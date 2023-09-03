import requests

class UrchinAPI:

    def say_hello():
        return "Hello World";

    def get_price_usd(self):
        raise NotImplementedError

    @staticmethod
    def generic_unothorized_request(request_method, url, **kwargs):
        return getattr(requests, request_method)(url, **kwargs)
