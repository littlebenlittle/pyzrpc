
import pickle
import zmq

sock = zmq.Context().socket(zmq.REP)
sock.bind('tcp://*:9000')

while True:
    msg = sock.recv()

    try:
        fn, args = pickle.loads(msg)
        print(f'got {fn}, {args}')
        obj = fn(args)
        print(f'{obj}')
    except Exception as e:
        obj = e

    res = pickle.dumps(obj)
    sock.send(res)
