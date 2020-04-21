# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from arm_control/TOF_sensor_data.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TOF_sensor_data(genpy.Message):
  _md5sum = "3c37e3e2c7851686cb8c295f62489702"
  _type = "arm_control/TOF_sensor_data"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32[3] range_reading
float32[3] lux_reading
"""
  __slots__ = ['range_reading','lux_reading']
  _slot_types = ['int32[3]','float32[3]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       range_reading,lux_reading

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TOF_sensor_data, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.range_reading is None:
        self.range_reading = [0] * 3
      if self.lux_reading is None:
        self.lux_reading = [0.] * 3
    else:
      self.range_reading = [0] * 3
      self.lux_reading = [0.] * 3

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_3i().pack(*self.range_reading))
      buff.write(_get_struct_3f().pack(*self.lux_reading))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 12
      self.range_reading = _get_struct_3i().unpack(str[start:end])
      start = end
      end += 12
      self.lux_reading = _get_struct_3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(self.range_reading.tostring())
      buff.write(self.lux_reading.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 12
      self.range_reading = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=3)
      start = end
      end += 12
      self.lux_reading = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
