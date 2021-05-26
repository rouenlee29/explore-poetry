import pendulum


def get_datetime_now():
    return pendulum.now().strftime("%Y-%m-%d")   
