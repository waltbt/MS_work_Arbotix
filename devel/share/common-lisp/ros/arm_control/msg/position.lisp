; Auto-generated. Do not edit!


(cl:in-package arm_control-msg)


;//! \htmlinclude position.msg.html

(cl:defclass <position> (roslisp-msg-protocol:ros-message)
  ((point
    :reader point
    :initarg :point
    :type (cl:vector cl:float)
   :initform (cl:make-array 4 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass position (<position>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <position>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'position)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name arm_control-msg:<position> is deprecated: use arm_control-msg:position instead.")))

(cl:ensure-generic-function 'point-val :lambda-list '(m))
(cl:defmethod point-val ((m <position>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader arm_control-msg:point-val is deprecated.  Use arm_control-msg:point instead.")
  (point m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <position>) ostream)
  "Serializes a message object of type '<position>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'point))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <position>) istream)
  "Deserializes a message object of type '<position>"
  (cl:setf (cl:slot-value msg 'point) (cl:make-array 4))
  (cl:let ((vals (cl:slot-value msg 'point)))
    (cl:dotimes (i 4)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<position>)))
  "Returns string type for a message object of type '<position>"
  "arm_control/position")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'position)))
  "Returns string type for a message object of type 'position"
  "arm_control/position")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<position>)))
  "Returns md5sum for a message object of type '<position>"
  "c8e7818df37db2cf138689cbda172d04")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'position)))
  "Returns md5sum for a message object of type 'position"
  "c8e7818df37db2cf138689cbda172d04")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<position>)))
  "Returns full string definition for message of type '<position>"
  (cl:format cl:nil "float32[4] point~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'position)))
  "Returns full string definition for message of type 'position"
  (cl:format cl:nil "float32[4] point~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <position>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'point) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <position>))
  "Converts a ROS message object to a list"
  (cl:list 'position
    (cl:cons ':point (point msg))
))
