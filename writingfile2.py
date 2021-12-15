#!/usr/bin/python3
import time

with open("data/D2.txt","w") as f:
   i=0
   while True:
      print(f"writing from docker   {i}...")
      f.write(f"Writing from docker  {i}\n ")
      f.flush()
      time.sleep(1)
      i=i+1
