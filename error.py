PS C:\python_training> py.test test_add_group.py
================================================= test session starts =================================================
platform win32 -- Python 3.9.2rc1, pytest-7.3.1, pluggy-1.0.0
rootdir: C:\python_training
collected 2 items

test_add_group.py EE                                                                                             [100%]

======================================================= ERRORS ========================================================
_______________________________________ ERROR at setup of test_add_empty_group ________________________________________

request = <SubRequest 'app' for <Function test_add_empty_group>>

    @pytest.fixture()
    def app(request):
>       fixture = Application()

test_add_group.py:8:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
application.py:7: in __init__
    self.wd = webdriver.Firefox()
c:\python39\lib\site-packages\selenium\webdriver\firefox\webdriver.py:170: in __init__
    RemoteWebDriver.__init__(
c:\python39\lib\site-packages\selenium\webdriver\remote\webdriver.py:157: in __init__
    self.start_session(capabilities, browser_profile)
c:\python39\lib\site-packages\selenium\webdriver\remote\webdriver.py:252: in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
c:\python39\lib\site-packages\selenium\webdriver\remote\webdriver.py:319: in execute
    response = self.command_executor.execute(driver_command, params)
c:\python39\lib\site-packages\selenium\webdriver\remote\remote_connection.py:374: in execute
    return self._request(command_info[0], url, body=data)
c:\python39\lib\site-packages\selenium\webdriver\remote\remote_connection.py:397: in _request
    resp = self._conn.request(method, url, body=body, headers=headers)
c:\python39\lib\site-packages\urllib3\_request_methods.py:118: in request
    return self.request_encode_body(
c:\python39\lib\site-packages\urllib3\_request_methods.py:217: in request_encode_body
    return self.urlopen(method, url, **extra_kw)
c:\python39\lib\site-packages\urllib3\poolmanager.py:422: in urlopen
    conn = self.connection_from_host(u.host, port=u.port, scheme=u.scheme)
c:\python39\lib\site-packages\urllib3\poolmanager.py:303: in connection_from_host
    return self.connection_from_context(request_context)
c:\python39\lib\site-packages\urllib3\poolmanager.py:328: in connection_from_context
    return self.connection_from_pool_key(pool_key, request_context=request_context)
c:\python39\lib\site-packages\urllib3\poolmanager.py:351: in connection_from_pool_key
    pool = self._new_pool(scheme, host, port, request_context=request_context)
c:\python39\lib\site-packages\urllib3\poolmanager.py:265: in _new_pool
    return pool_cls(host, port, **request_context)
c:\python39\lib\site-packages\urllib3\connectionpool.py:196: in __init__
    timeout = Timeout.from_float(timeout)
c:\python39\lib\site-packages\urllib3\util\timeout.py:190: in from_float
    return Timeout(read=timeout, connect=timeout)
c:\python39\lib\site-packages\urllib3\util\timeout.py:119: in __init__
    self._connect = self._validate_timeout(connect, "connect")
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cls = <class 'urllib3.util.timeout.Timeout'>, value = <object object at 0x0000020541C38810>, name = 'connect'

    @classmethod
    def _validate_timeout(cls, value: _TYPE_TIMEOUT, name: str) -> _TYPE_TIMEOUT:
        """Check that a timeout attribute is valid.

        :param value: The timeout value to validate
        :param name: The name of the timeout attribute to validate. This is
            used to specify in error messages.
        :return: The validated and casted version of the given value.
        :raises ValueError: If it is a numeric value less than or equal to
            zero, or the type is not an integer, float, or None.
        """
        if value is None or value is _DEFAULT_TIMEOUT:
            return value

        if isinstance(value, bool):
            raise ValueError(
                "Timeout cannot be a boolean value. It must "
                "be an int, float or None."
            )
        try:
            float(value)
        except (TypeError, ValueError):
>           raise ValueError(
                "Timeout value %s was %s, but it must be an "
                "int, float or None." % (name, value)
            ) from None
E           ValueError: Timeout value connect was <object object at 0x0000020541C38810>, but it must be an int, float or None.

c:\python39\lib\site-packages\urllib3\util\timeout.py:156: ValueError
__________________________________________ ERROR at setup of test_add_group ___________________________________________

request = <SubRequest 'app' for <Function test_add_group>>

    @pytest.fixture()
    def app(request):
>       fixture = Application()

test_add_group.py:8:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
application.py:7: in __init__
    self.wd = webdriver.Firefox()
c:\python39\lib\site-packages\selenium\webdriver\firefox\webdriver.py:170: in __init__
    RemoteWebDriver.__init__(
c:\python39\lib\site-packages\selenium\webdriver\remote\webdriver.py:157: in __init__
    self.start_session(capabilities, browser_profile)
c:\python39\lib\site-packages\selenium\webdriver\remote\webdriver.py:252: in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
c:\python39\lib\site-packages\selenium\webdriver\remote\webdriver.py:319: in execute
    response = self.command_executor.execute(driver_command, params)
c:\python39\lib\site-packages\selenium\webdriver\remote\remote_connection.py:374: in execute
    return self._request(command_info[0], url, body=data)
c:\python39\lib\site-packages\selenium\webdriver\remote\remote_connection.py:397: in _request
    resp = self._conn.request(method, url, body=body, headers=headers)
c:\python39\lib\site-packages\urllib3\_request_methods.py:118: in request
    return self.request_encode_body(
c:\python39\lib\site-packages\urllib3\_request_methods.py:217: in request_encode_body
    return self.urlopen(method, url, **extra_kw)
c:\python39\lib\site-packages\urllib3\poolmanager.py:422: in urlopen
    conn = self.connection_from_host(u.host, port=u.port, scheme=u.scheme)
c:\python39\lib\site-packages\urllib3\poolmanager.py:303: in connection_from_host
    return self.connection_from_context(request_context)
c:\python39\lib\site-packages\urllib3\poolmanager.py:328: in connection_from_context
    return self.connection_from_pool_key(pool_key, request_context=request_context)
c:\python39\lib\site-packages\urllib3\poolmanager.py:351: in connection_from_pool_key
    pool = self._new_pool(scheme, host, port, request_context=request_context)
c:\python39\lib\site-packages\urllib3\poolmanager.py:265: in _new_pool
    return pool_cls(host, port, **request_context)
c:\python39\lib\site-packages\urllib3\connectionpool.py:196: in __init__
    timeout = Timeout.from_float(timeout)
c:\python39\lib\site-packages\urllib3\util\timeout.py:190: in from_float
    return Timeout(read=timeout, connect=timeout)
c:\python39\lib\site-packages\urllib3\util\timeout.py:119: in __init__
    self._connect = self._validate_timeout(connect, "connect")
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

cls = <class 'urllib3.util.timeout.Timeout'>, value = <object object at 0x0000020541C38810>, name = 'connect'

    @classmethod
    def _validate_timeout(cls, value: _TYPE_TIMEOUT, name: str) -> _TYPE_TIMEOUT:
        """Check that a timeout attribute is valid.

        :param value: The timeout value to validate
        :param name: The name of the timeout attribute to validate. This is
            used to specify in error messages.
        :return: The validated and casted version of the given value.
        :raises ValueError: If it is a numeric value less than or equal to
            zero, or the type is not an integer, float, or None.
        """
        if value is None or value is _DEFAULT_TIMEOUT:
            return value

        if isinstance(value, bool):
            raise ValueError(
                "Timeout cannot be a boolean value. It must "
                "be an int, float or None."
            )
        try:
            float(value)
        except (TypeError, ValueError):
>           raise ValueError(
                "Timeout value %s was %s, but it must be an "
                "int, float or None." % (name, value)
            ) from None
E           ValueError: Timeout value connect was <object object at 0x0000020541C38810>, but it must be an int, float or None.

c:\python39\lib\site-packages\urllib3\util\timeout.py:156: ValueError
=============================================== short test summary info ===============================================
ERROR test_add_group.py::test_add_empty_group - ValueError: Timeout value connect was <object object at 0x0000020541C38810>, but it must be an int, float or None.
ERROR test_add_group.py::test_add_group - ValueError: Timeout value connect was <object object at 0x0000020541C38810>, but it must be an int, float or None.


PySocks	1.7.1	1.7.1
async-generator	1.10	1.10
attrs	23.1.0	23.1.0
certifi	2023.5.7	2023.5.7
cffi	1.15.1	1.15.1
colorama	0.4.6	0.4.6
exceptiongroup	1.1.1	1.1.1
h11	0.14.0	0.14.0
idna	3.4	3.4
iniconfig	2.0.0	2.0.0
outcome	1.2.0	1.2.0
packaging	23.1	23.1
pip	23.1.2	23.1.2
pluggy	1.0.0	1.0.0
pycparser	2.21	2.21
pytest	7.3.1	7.3.1
selenium	3.141.0	4.9.1
setuptools	67.7.2	67.8.0
sniffio	1.3.0	1.3.0
sortedcontainers	2.4.0	2.4.0
tomli	2.0.1	2.0.1
trio	0.22.0	0.22.0
trio-websocket	0.10.2	0.10.2
urllib3	2.0.2	2.0.2
wheel	0.40.0	0.40.0
wsproto	1.2.0	1.2.0

