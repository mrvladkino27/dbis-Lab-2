import time
from functools import wraps

time_result = 'Results/TimeResult.txt'

with open(time_result, 'w'):
    pass
def profile_time(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        with open(time_result, 'a') as profile_log:
            fn_kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
            profile_log.write(f'\n{fn.__name__}({fn_kwargs_str})\n')

            # Measure time
            t = time.perf_counter()
            retval = fn(*args, **kwargs)
            elapsed = time.perf_counter() - t
            profile_log.write(f'Time {elapsed:0.4} s\n')
            return retval
    return inner
