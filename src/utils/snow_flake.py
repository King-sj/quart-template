'''
 雪花算法生成唯一ID
'''
import time
import threading


class SnowFlake:
  '''
  雪花算法生成唯一ID

  Example:
  ```python
  snow_flake = SnowFlake()
  for i in range(10):
    print(snow_flake.gen_id())
  ```

  '''
  def __init__(self, worker_id=0, data_center_id=0):
    self.worker_id = 0
    self.data_center_id = 0
    self.sequence = 0
    self.last_timestamp = -1
    self.lock = threading.Lock()

  def _gen_timestamp(self):
    return int(time.time() * 1000)

  def _gen_next_millis(self, last_timestamp):
    timestamp = self._gen_timestamp()
    while timestamp <= last_timestamp:
      timestamp = self._gen_timestamp()
    return timestamp

  def gen_id(self) -> int:
    timestamp = self._gen_timestamp()
    if timestamp < self.last_timestamp:
      timestamp = self._gen_next_millis(self.last_timestamp)
    if timestamp == self.last_timestamp:
      self.sequence = (self.sequence + 1) & 4095
      if self.sequence == 0:
        timestamp = self._gen_next_millis(timestamp)
    else:
      self.sequence = 0
    self.last_timestamp = timestamp
    return ((timestamp - 1609459200000) << 22) | (
        self.data_center_id << 17) | (self.worker_id << 12) | self.sequence
