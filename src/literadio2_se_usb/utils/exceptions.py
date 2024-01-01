class CustomException(Exception):
    message = 'An error occurred'

    def __init__(self, *args, **kwargs):
        if not args:
            args = (self.message,)
        super().__init__(*args, **kwargs)


class DeviceNotFound(CustomException):
    message = 'Cannot find the device'


class InvalidEndpointAddress(CustomException):
    message = 'The endpoint address is None. Did you run the "setup()" method?'
