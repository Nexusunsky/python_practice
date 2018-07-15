import abc
import functools
import logging
import inspect

from tdp.constant.http_code import HttpCode
from tdp.exception.exceptions import TDPBaseException

ILLEGAL_EMPTY_ARGUMENTS = 'Illegal empty arguments'


class BaseChecker(abc.ABC):
    def __init__(self, required_args=None, actual_args=None):
        self.__required = required_args
        self.__actual = actual_args

    @property
    def required(self):
        return self.__required

    @property
    def actual(self):
        return self.__actual

    @abc.abstractmethod
    def checkout(self):
        pass


class Default(BaseChecker):
    def checkout(self):
        required_args = self.required
        args, kwargs = self.actual

        # required_args is empty
        if not required_args:
            return

        i = 0
        for arg in args:
            i += 1
            if not arg:
                self.handle_exception(arg_name=required_args[i])

        for key, value in kwargs.items():
            if not value:
                self.handle_exception(arg_name=key)

    @staticmethod
    def handle_exception(arg_name):
        logging.error('Invalid param: %s', arg_name)
        raise TDPBaseException(reason=ILLEGAL_EMPTY_ARGUMENTS, status=HttpCode.INTERNAL_SERVER_ERROR)


class Specified(BaseChecker):
    def checkout(self):
        required_args = self.required
        requests = self.actual.args

        for arg in required_args:
            if requests.get(arg) is None:
                raise TDPBaseException(status=HttpCode.BAD_REQUEST.value, reason=arg + ' is required')


def param_check(base_checker: BaseChecker = None):
    def decorator(func):
        checker = base_checker

        @functools.wraps(func)
        def target(*args, **kwargs):
            nonlocal checker
            if checker is None:
                checker = __get_default(args, kwargs)

            checker.checkout()
            return func(*args, **kwargs)

        def __get_default(args, kwargs):
            arg_spec = inspect.getfullargspec(func).args
            if 'self' in arg_spec:
                arg_spec = arg_spec[1:]
            return Default(required_args=arg_spec, actual_args=(args, kwargs))

        return target

    return decorator
