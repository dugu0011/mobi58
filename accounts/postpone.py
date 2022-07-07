from threading import Thread
from django.db import connection

# Logger for Thread
class LogThread(Thread):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._real_run = self.run
        self.run = self._wrap_run

    def _wrap_run(self):
        try:
            self._real_run()
        except Exception as e:
            print(e)

def postpone(function):
    def decorator(*args, **kwargs):
        t = LogThread(target=function, args=args, kwargs=kwargs)
        t.setName('Generic Thread')
        t.daemon = True
        t.start()

    return decorator

