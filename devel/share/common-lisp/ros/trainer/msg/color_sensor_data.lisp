; Auto-generated. Do not edit!


(cl:in-package trainer-msg)


;//! \htmlinclude color_sensor_data.msg.html

(cl:defclass <color_sensor_data> (roslisp-msg-protocol:ros-message)
  ((rgb_values
    :reader rgb_values
    :initarg :rgb_values
    :type (cl:vector cl:integer)
   :initform (cl:make-array 4 :element-type 'cl:integer :initial-element 0))
   (color_temp
    :reader color_temp
    :initarg :color_temp
    :type cl:integer
    :initform 0)
   (lux
    :reader lux
    :initarg :lux
    :type cl:float
    :initform 0.0))
)

(cl:defclass color_sensor_data (<color_sensor_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <color_sensor_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'color_sensor_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name trainer-msg:<color_sensor_data> is deprecated: use trainer-msg:color_sensor_data instead.")))

(cl:ensure-generic-function 'rgb_values-val :lambda-list '(m))
(cl:defmethod rgb_values-val ((m <color_sensor_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trainer-msg:rgb_values-val is deprecated.  Use trainer-msg:rgb_values instead.")
  (rgb_values m))

(cl:ensure-generic-function 'color_temp-val :lambda-list '(m))
(cl:defmethod color_temp-val ((m <color_sensor_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trainer-msg:color_temp-val is deprecated.  Use trainer-msg:color_temp instead.")
  (color_temp m))

(cl:ensure-generic-function 'lux-val :lambda-list '(m))
(cl:defmethod lux-val ((m <color_sensor_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trainer-msg:lux-val is deprecated.  Use trainer-msg:lux instead.")
  (lux m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <color_sensor_data>) ostream)
  "Serializes a message object of type '<color_sensor_data>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'rgb_values))
  (cl:let* ((signed (cl:slot-value msg 'color_temp)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lux))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <color_sensor_data>) istream)
  "Deserializes a message object of type '<color_sensor_data>"
  (cl:setf (cl:slot-value msg 'rgb_values) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'rgb_values)))
    (cl:dotimes (i 4)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'color_temp) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lux) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<color_sensor_data>)))
  "Returns string type for a message object of type '<color_sensor_data>"
  "trainer/color_sensor_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'color_sensor_data)))
  "Returns string type for a message object of type 'color_sensor_data"
  "trainer/color_sensor_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<color_sensor_data>)))
  "Returns md5sum for a message object of type '<color_sensor_data>"
  "7c8cfe28df9aa44956a941b8c260653a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'color_sensor_data)))
  "Returns md5sum for a message object of type 'color_sensor_data"
  "7c8cfe28df9aa44956a941b8c260653a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<color_sensor_data>)))
  "Returns full string definition for message of type '<color_sensor_data>"
  (cl:format cl:nil "int32[4] rgb_values~%int32 color_temp~%float32 lux~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'color_sensor_data)))
  "Returns full string definition for message of type 'color_sensor_data"
  (cl:format cl:nil "int32[4] rgb_values~%int32 color_temp~%float32 lux~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <color_sensor_data>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'rgb_values) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <color_sensor_data>))
  "Converts a ROS message object to a list"
  (cl:list 'color_sensor_data
    (cl:cons ':rgb_values (rgb_values msg))
    (cl:cons ':color_temp (color_temp msg))
    (cl:cons ':lux (lux msg))
))
