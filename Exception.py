MINMUN_HOURLY_RATE=10

class PhoneError(Exception):
    """check is phone  equal 11 digits and starts with (01)"""
    pass

class EmailError(Exception):
    """check is the email like email pattern"""
    pass

class IdError(Exception):
    """check the ID equal 14 digits"""
    pass

class HourlyRateError(Exception):
    """check the hourlyRate  greater than MINMUN_HOURLY_RATE"""
    pass

class HourWorkError(Exception):
    """cher the hour Work greater than Zero"""
    pass