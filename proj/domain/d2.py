from domain import d1

def f():
    print('at d2')
    d1.f()
    print(__name__)
