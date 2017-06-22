import sys

sc = None

def validate_scripts(script):
    sc = dict(**locals(), **globals())
    exec(script, sc, sc)
    pre_process(sc, 'test')

def pre_process(sc, method_name):
    method = sc[method_name]
    print(method.__code__.co_argcount)
    arguments = (method.__code__.co_varnames)
    args = [model.get(arg) for arg in arguments]
    values = method(*args)
    process(values)

def process(vals):
    print(vals)
    pass

def post_process():
    pass

if __name__ == "__main__":
    arg = sys.argv[1]
    validate_scripts(arg)
    pre_process('test')
    pre_process(sys.argv[2])

