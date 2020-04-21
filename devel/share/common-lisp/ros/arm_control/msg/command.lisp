; Auto-generated. Do not edit!


(cl:in-package arm_control-msg)


;//! \htmlinclude command.msg.html

(cl:defclass <command> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type (cl:vector cl:integer)
   :initform (cl:make-array 6 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass command (<command>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <command>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'command)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name arm_control-msg:<command> is deprecated: use arm_control-msg:command instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_control-msg:pose-val is deprecated.  Use arm_control-msg:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <command>) ostream)
  "Serializes a message object of type '<command>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'pose))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <command>) istream)
  "Deserializes a message object of type '<command>"
  (cl:setf (cl:slot-value msg 'pose) (cl:make-array 6))
  (cl:let ((vals (cl:slot-value msg 'pose)))
    (cl:dotimes (i 6)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<command>)))
  "Returns string type for a message object of type '<command>"
  "arm_control/command")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'command)))
  "Returns string type for a message object of type 'command"
  "arm_control/command")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<command>)))
  "Returns md5sum for a message object of type '<command>"
  "1a1a3549ea1fbd90af851784fda8677a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'command)))
  "Returns md5sum for a message object of type 'command"
  "1a1a3549ea1fbd90af851784fda8677a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<command>)))
  "Returns full string definition for message of type '<command>"
  (cl:format cl:nil "int32[6] pose~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'command)))
  "Returns full string definition for message of type 'command"
  (cl:format cl:nil "int32[6] pose~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <command>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'pose) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <command>))
  "Converts a ROS message object to a list"
  (cl:list 'command
    (cl:cons ':pose (pose msg))
))
