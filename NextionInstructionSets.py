"""
Nextion uses a CRC32 type algorithm.
"""

class Checksum:
  def CRC(self, data, salt: int = 0xffffffff, skip: int = 0, length: int = -1):
    if length < 0:
      length = len(data)
    data = data[skip:length]
    if type(data) is bytes:
      data = [int(b) for b in data]
    return self._CRC32(data, salt)

  def _CRC32(self, l: list, xorIn=0xffffffff, xorOut=0):
    poly = 0x4c11db7
    poly |= (1 << 32)
    reg = 0
    l = l + [0]
    l[0] ^= xorIn
    for word in l:
      for i in range(32):
        reg <<= 1
        if word >= (1 << 31):
          reg += 1
        word <<= 1
        word &= 0xffffffff
        if reg >= (1 << 32):
          reg ^= poly
    reg &= 0xffffffff
    reg ^= xorOut
    return reg
