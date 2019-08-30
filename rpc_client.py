
import sys
import pickle
import zmq


class RPCClient:

    started = False

    def __init__(self, context, addr):
        self.sock = context.socket(zmq.REQ)
        self.sock.connect(addr)
        
    def run(self, fn, args):
        if self.started:
            raise Exception('the client already sent a command!')
        msg = pickle.dumps((fn, args))
        self.started = True
        self.sock.send(msg)

    def get(self):
        if not self.started:
            raise Exception('the client has not sent any commands!')
        self.startd = False
        res = self.sock.recv()
        obj = pickle.loads(res)
        return obj

if __name__ == '__main__':
    client = RPCClient(zmq.Context(), 'tcp://localhost:9000')

    def f(x):
        return x+1

    client.run(f, 3)
    print(client.get())
