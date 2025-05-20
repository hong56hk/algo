import os
import threading
import time
import queue
import random


class Consumer(threading.Thread):
  def __init__(self, queue, name="consumer"):
    threading.Thread.__init__(self);
    self.name = name
    self.running = True
    self.queue = queue
    self.doneTaskCount = 0
    self.hp = 10

  def run(self):
    while self.running:
      task = self.queue.get();
      time.sleep(2)
      self.doneTaskCount += 1
      print("{} done task (#{}): {}".format(self.name, self.doneTaskCount, task))
      self.hp -= 1
      if self.hp <= 0:
        self.running = False

class Producer(threading.Thread):
  def __init__(self, queue, name="producer"):
    threading.Thread.__init__(self);
    self.name = name
    self.running = True
    self.queue = queue
    self.hp = 10
    self.doneTaskCount = 0

  def run(self):
    while self.running:
      time.sleep(1)
      task = random.random() * 100
      self.queue.put(task)
      self.doneTaskCount += 1
      print("{} created task (#{}): {}".format(self.name, self.doneTaskCount, task))
      
      self.hp -= 1
      if self.hp <= 0:
        self.running = False
          
# main
def main():
  print("start main")
  Q = queue.Queue()
  producer = Producer(Q, "Producer 1")
  consumer = Consumer(Q, "Consumer 1")
  
  producer.start()
  producer.join()
  
  consumer.start()
  
  print(threading.current_thread())
  
  
  consumer.join()
  print("performing cleaning, supposed after all thread finished")
  

if __name__ == "__main__":
  main()