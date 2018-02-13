#property copyright "Copyright 2016, Li Ding"
#property link      "dingmaotu@hotmail.com"
#property version   "1.00"

#include <Zmq/Zmq.mqh>
//+------------------------------------------------------------------+
//| Hello World server in MQL                                        |
//| Binds REP socket to tcp://*:5555                                 |
//| Expects "Hello" from client, replies with "World"                |
//+------------------------------------------------------------------+
void OnStart()
  {
   Context context("helloworld");
   Socket socket_push(context,ZMQ_PUSH);
   socket_push.bind("tcp://127.0.0.1:5558");
   Socket socket_pull(context,ZMQ_PULL);
   socket_pull.connect("tcp://127.0.0.1:5557");
   

   while(!IsStopped())
     {
     
      ZmqMsg reply("World");
      // Send reply back to client
      socket_push.send(reply);
      Print("send message to py");
   
      ZmqMsg message;
      socket_pull.recv(message);
      Print(message.getData());
      Sleep(1000);
     }
  }