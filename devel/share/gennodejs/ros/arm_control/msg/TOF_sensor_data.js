// Auto-generated. Do not edit!

// (in-package arm_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class TOF_sensor_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.range_reading = null;
      this.lux_reading = null;
    }
    else {
      if (initObj.hasOwnProperty('range_reading')) {
        this.range_reading = initObj.range_reading
      }
      else {
        this.range_reading = new Array(3).fill(0);
      }
      if (initObj.hasOwnProperty('lux_reading')) {
        this.lux_reading = initObj.lux_reading
      }
      else {
        this.lux_reading = new Array(3).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TOF_sensor_data
    // Check that the constant length array field [range_reading] has the right length
    if (obj.range_reading.length !== 3) {
      throw new Error('Unable to serialize array field range_reading - length must be 3')
    }
    // Serialize message field [range_reading]
    bufferOffset = _arraySerializer.int32(obj.range_reading, buffer, bufferOffset, 3);
    // Check that the constant length array field [lux_reading] has the right length
    if (obj.lux_reading.length !== 3) {
      throw new Error('Unable to serialize array field lux_reading - length must be 3')
    }
    // Serialize message field [lux_reading]
    bufferOffset = _arraySerializer.float32(obj.lux_reading, buffer, bufferOffset, 3);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TOF_sensor_data
    let len;
    let data = new TOF_sensor_data(null);
    // Deserialize message field [range_reading]
    data.range_reading = _arrayDeserializer.int32(buffer, bufferOffset, 3)
    // Deserialize message field [lux_reading]
    data.lux_reading = _arrayDeserializer.float32(buffer, bufferOffset, 3)
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'arm_control/TOF_sensor_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3c37e3e2c7851686cb8c295f62489702';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[3] range_reading
    float32[3] lux_reading
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TOF_sensor_data(null);
    if (msg.range_reading !== undefined) {
      resolved.range_reading = msg.range_reading;
    }
    else {
      resolved.range_reading = new Array(3).fill(0)
    }

    if (msg.lux_reading !== undefined) {
      resolved.lux_reading = msg.lux_reading;
    }
    else {
      resolved.lux_reading = new Array(3).fill(0)
    }

    return resolved;
    }
};

module.exports = TOF_sensor_data;
