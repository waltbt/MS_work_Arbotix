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

class position {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.point = null;
    }
    else {
      if (initObj.hasOwnProperty('point')) {
        this.point = initObj.point
      }
      else {
        this.point = new Array(4).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type position
    // Check that the constant length array field [point] has the right length
    if (obj.point.length !== 4) {
      throw new Error('Unable to serialize array field point - length must be 4')
    }
    // Serialize message field [point]
    bufferOffset = _arraySerializer.float32(obj.point, buffer, bufferOffset, 4);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type position
    let len;
    let data = new position(null);
    // Deserialize message field [point]
    data.point = _arrayDeserializer.float32(buffer, bufferOffset, 4)
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'arm_control/position';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c8e7818df37db2cf138689cbda172d04';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[4] point
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new position(null);
    if (msg.point !== undefined) {
      resolved.point = msg.point;
    }
    else {
      resolved.point = new Array(4).fill(0)
    }

    return resolved;
    }
};

module.exports = position;
