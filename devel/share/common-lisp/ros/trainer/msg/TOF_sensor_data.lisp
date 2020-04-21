; Auto-generated. Do not edit!


(cl:in-package trainer-msg)


;//! \htmlinclude TOF_sensor_data.msg.html

(cl:defclass <TOF_sensor_data> (roslisp-msg-protocol:ros-message)
  ((range_reading
    :reader range_reading
    :initarg :range_reading
    :type (cl:vector cl:integer)
   :initform (cl:make-array 3 :element-type 'cl:integer :initial-element 0))
   (lux_reading
    :reader lux_reading
    :initarg :lux_reading
    :type (cl:vector cl:float)
   :initform (cl:make-array 3 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass TOF_sensor_data (<TOF_sensor_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TOF_sensor_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TOF_sensor_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name trainer-msg:<TOF_sensor_data> is deprecated: use trainer-msg:TOF_sensor_data instead.")))

(cl:ensure-generic-function 'range_reading-val :lambda-list '(m))
(cl:defmethod range_reading-val ((m <TOF_sensor_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trainer-msg:range_reading-val is deprecated.  Use trainer-msg:range_reading instead.")
  (range_reading m))

(cl:ensure-generic-function 'lux_reading-val :lambda-list '(m))
(cl:defmethod lux_reading-val ((m <TOF_sensor_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trainer-msg:lux_reading-val is deprecated.  Use trainer-msg:lux_reading instead.")
  (lux_reading m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TOF_sensor_data>) ostream)
  "Serializes a message object of type '<TOF_sensor_data>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'range_reading))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'lux_reading))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TOF_sensor_data>) istream)
  "Deserializes a message object of type '<TOF_sensor_data>"
  (cl:setf (cl:slot-value msg 'range_reading) (cl:make-array 3))
  (cl:let ((vals (cl:slot-value msg 'range_reading)))
    (cl:dotimes (i 3)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))))
  (cl:setf (cl:slot-value msg 'lux_reading) (cl:make-array 3))
  (cl:let ((vals (cl:slot-value msg 'lux_reading)))
    (cl:dotimes (i 3)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TOF_sensor_data>)))
  "Returns string type for a message object of type '<TOF_sensor_data>"
  "trainer/TOF_sensor_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TOF_sensor_data)))
  "Returns string type for a message object of type 'TOF_sensor_data"
  "trainer/TOF_sensor_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TOF_sensor_data>)))
  "Returns md5sum for a message object of type '<TOF_sensor_data>"
  "3c37e3e2c7851686cb8c295f62489702")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TOF_sensor_data)))
  "Returns md5sum for a message object of type 'TOF_sensor_data"
  "3c37e3e2c7851686cb8c295f62489702")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TOF_sensor_data>)))
  "Returns full string definition for message of type '<TOF_sensor_data>"
  (cl:format cl:nil "int32[3] range_reading~%float32[3] lux_reading~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TOF_sensor_data)))
  "Returns full string definition for message of type 'TOF_sensor_data"
  (cl:format cl:nil "int32[3] range_reading~%float32[3] lux_reading~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TOF_sensor_data>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'range_reading) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'lux_reading) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TOF_sensor_data>))
  "Converts a ROS message object to a list"
  (cl:list 'TOF_sensor_data
    (cl:cons ':range_reading (range_reading msg))
    (cl:cons ':lux_reading (lux_reading msg))
))
