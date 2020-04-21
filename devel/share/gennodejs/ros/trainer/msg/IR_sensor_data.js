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

class IR_sensor_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.sensor_reading = null;
    }
    else {
      if (initObj.hasOwnProperty('sensor_reading')) {
        this.sensor_reading = initObj.sensor_reading
      }
      else {
        this.sensor_reading = new Array(3).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IR_sensor_data
    // Check that the constant length array field [sensor_reading] has the right length
    if (obj.sensor_reading.length !== 3) {
      throw new Error('Unable to serialize array field sensor_reading - length must be 3')
    }
    // Serialize message field [sensor_reading]
    bufferOffset = _arraySerializer.int32(obj.sensor_reading, buffer, bufferOffset, 3);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IR_sensor_data
    let len;
    let data = new IR_sensor_data(null);
    // Deserialize message field [sensor_reading]
    data.sensor_reading = _arrayDeserializer.int32(buffer, bufferOffset, 3)
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'trainer/IR_sensor_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a614798fa533ba4b6588423e50c5f7ae';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[3] sensor_reading
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new IR_sensor_data(null);
    if (msg.sensor_reading !== undefined) {
      resolved.sensor_reading = msg.sensor_reading;
    }
    else {
      resolved.sensor_reading = new Array(3).fill(0)
    }

    return resolved;
    }
};

module.exports = IR_sensor_data;
