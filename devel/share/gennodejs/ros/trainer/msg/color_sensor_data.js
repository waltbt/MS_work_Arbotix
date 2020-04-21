// Auto-generated. Do not edit!

// (in-package trainer.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class color_sensor_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.rgb_values = null;
      this.color_temp = null;
      this.lux = null;
    }
    else {
      if (initObj.hasOwnProperty('rgb_values')) {
        this.rgb_values = initObj.rgb_values
      }
      else {
        this.rgb_values = new Array(4).fill(0);
      }
      if (initObj.hasOwnProperty('color_temp')) {
        this.color_temp = initObj.color_temp
      }
      else {
        this.color_temp = 0;
      }
      if (initObj.hasOwnProperty('lux')) {
        this.lux = initObj.lux
      }
      else {
        this.lux = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type color_sensor_data
    // Check that the constant length array field [rgb_values] has the right length
    if (obj.rgb_values.length !== 4) {
      throw new Error('Unable to serialize array field rgb_values - length must be 4')
    }
    // Serialize message field [rgb_values]
    bufferOffset = _arraySerializer.int32(obj.rgb_values, buffer, bufferOffset, 4);
    // Serialize message field [color_temp]
    bufferOffset = _serializer.int32(obj.color_temp, buffer, bufferOffset);
    // Serialize message field [lux]
    bufferOffset = _serializer.float32(obj.lux, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type color_sensor_data
    let len;
    let data = new color_sensor_data(null);
    // Deserialize message field [rgb_values]
    data.rgb_values = _arrayDeserializer.int32(buffer, bufferOffset, 4)
    // Deserialize message field [color_temp]
    data.color_temp = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [lux]
    data.lux = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'trainer/color_sensor_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7c8cfe28df9aa44956a941b8c260653a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[4] rgb_values
    int32 color_temp
    float32 lux
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new color_sensor_data(null);
    if (msg.rgb_values !== undefined) {
      resolved.rgb_values = msg.rgb_values;
    }
    else {
      resolved.rgb_values = new Array(4).fill(0)
    }

    if (msg.color_temp !== undefined) {
      resolved.color_temp = msg.color_temp;
    }
    else {
      resolved.color_temp = 0
    }

    if (msg.lux !== undefined) {
      resolved.lux = msg.lux;
    }
    else {
      resolved.lux = 0.0
    }

    return resolved;
    }
};

module.exports = color_sensor_data;
