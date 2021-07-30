from time import time
from contextlib import contextmanager

HEADER = "this is the header \n"
FOOTER = "\nthis is the footer \n"

@contextmanager
def new_log_file(name):
    try:
        longname = name
        f = open(longname,'w')
        f.write(HEADER)
        yield f
    finally:
        f.write(FOOTER)
        print("Log File Created")
        f.close()


with new_log_file('logfile') as file:
    file.write('this is the body')



