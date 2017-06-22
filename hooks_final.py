import sys

exec(sys.argv[1])


def pre_process():
    method1 = globals()[sys.argv[2]]
    process(method1)


def process(method):
    x = method(1,2)
    print(x)
    method2 = globals()[sys.argv[3]]
    post_process(method2)


def post_process(method):
    y = method(2,3)
    print(y)
    


res = pre_process()
print(res)
