;; Auto-generated. Do not edit!


(when (boundp 'arm_control::IR_sensor_data)
  (if (not (find-package "ARM_CONTROL"))
    (make-package "ARM_CONTROL"))
  (shadow 'IR_sensor_data (find-package "ARM_CONTROL")))
(unless (find-package "ARM_CONTROL::IR_SENSOR_DATA")
  (make-package "ARM_CONTROL::IR_SENSOR_DATA"))

(in-package "ROS")
;;//! \htmlinclude IR_sensor_data.msg.html


(defclass arm_control::IR_sensor_data
  :super ros::object
  :slots (_sensor_reading ))

(defmethod arm_control::IR_sensor_data
  (:init
   (&key
    ((:sensor_reading __sensor_reading) (make-array 3 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _sensor_reading __sensor_reading)
   self)
  (:sensor_reading
   (&optional __sensor_reading)
   (if __sensor_reading (setq _sensor_reading __sensor_reading)) _sensor_reading)
  (:serialization-length
   ()
   (+
    ;; int32[3] _sensor_reading
    (* 4    3)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[3] _sensor_reading
     (dotimes (i 3)
       (write-long (elt _sensor_reading i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[3] _sensor_reading
   (dotimes (i (length _sensor_reading))
     (setf (elt _sensor_reading i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     )
   ;;
   self)
  )

(setf (get arm_control::IR_sensor_data :md5sum-) "a614798fa533ba4b6588423e50c5f7ae")
(setf (get arm_control::IR_sensor_data :datatype-) "arm_control/IR_sensor_data")
(setf (get arm_control::IR_sensor_data :definition-)
      "int32[3] sensor_reading

")



(provide :arm_control/IR_sensor_data "a614798fa533ba4b6588423e50c5f7ae")


