# f = open("demofile.txt", "r")

# while True:
#     txt = f.readline()
#     if txt == '':
#         break
#     print(txt.strip())



from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

print("Now you see it")
with suppress_stdout():
    print("Now you don't")
print("asdfasd")