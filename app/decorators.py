from threading import Thread

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(targets=f, arg=args, kwargs=kwargs)
        thr.start()
    return wrapper