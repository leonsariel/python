import time
import zmq

def mt4():
    context = zmq.Context()
    send_socket = context.socket(zmq.PUSH)
    send_socket.bind("tcp://127.0.0.1:5557")
    rev_socket = context.socket(zmq.PULL)
    rev_socket.connect("tcp://127.0.0.1:5558")
    # Start your result manager and workers before you start your producers

    while True:
        send_socket.send("this is server")
        now = time.time()
        msg = rev_socket.recv()
        current = time.time()
        print(round(current-now)*1000)
        time.sleep(1)



    # for num in xrange(20000):
    #     work_message = { 'num' : num }
    #     send_socket.send_json(work_message)

mt4()