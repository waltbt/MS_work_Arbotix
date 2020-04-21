; Auto-generated. Do not edit!


(cl:in-package arm_control-msg)


;//! \htmlinclude IR_sensor_data.msg.html

(cl:defclass <IR_sensor_data> (roslisp-msg-protocol:ros-message)
  ((sensor_reading
    :reader sensor_reading
    :initarg :sensor_reading
    :type (cl:vector cl:integer)
   :initform (cl:make-array 3 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass IR_sensor_data (<IR_sensor_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IR_sensor_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IR_sensor_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name arm_control-msg:<IR_sensor_data> is deprecated: use arm_control-msg:IR_sensor_data instead.")))

(cl:ensure-generic-function 'sensor_reading-val :lambda-list '(m))
(cl:defmethod sensor_reading-val ((m <IR_sensor_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_control-msg:sensor_reading-val is deprecated.  Use arm_control-msg:sensor_reading instead.")
  (sensor_reading m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IR_sensor_data>) ostream)
  "Serializes a message object of type '<IR_sensor_data>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'sensor_reading))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IR_sensor_data>) istream)
  "Deserializes a message object of type '<IR_sensor_data>"
  (cl:setf (cl:slot-value msg 'sensor_reading) (cl:make-array 3))
  (cl:let ((vals (cl:slot-value msg 'sensor_reading)))
    (cl:dotimes (i 3)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IR_sensor_data>)))
  "Returns string type for a message object of type '<IR_sensor_data>"
  "arm_control/IR_sensor_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IR_sensor_data)))
  "Returns string type for a message object of type 'IR_sensor_data"
  "arm_control/IR_sensor_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IR_sensor_data>)))
  "Returns md5sum for a message object of type '<IR_sensor_data>"
  "a614798fa533ba4b6588423e50c5f7ae")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IR_sensor_data)))
  "Returns md5sum for a message object of type 'IR_sensor_data"
  "a614798fa533ba4b6588423e50c5f7ae")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IR_sensor_data>)))
  "Returns full string definition for message of type '<IR_sensor_data>"
  (cl:format cl:nil "int32[3] sensor_reading~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IR_sensor_data)))
  "Returns full string definition for message of type 'IR_sensor_data"
  (cl:format cl:nil "int32[3] sensor_reading~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IR_sensor_data>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'sensor_reading) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IR_sensor_data>))
  "Converts a ROS message object to a list"
  (cl:list 'IR_sensor_data
    (cl:cons ':sensor_reading (sensor_reading msg))
))
