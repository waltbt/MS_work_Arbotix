;; Auto-generated. Do not edit!


(when (boundp 'arm_control::position)
  (if (not (find-package "ARM_CONTROL"))
    (make-package "ARM_CONTROL"))
  (shadow 'position (find-package "ARM_CONTROL")))
(unless (find-package "ARM_CONTROL::POSITION")
  (make-package "ARM_CONTROL::POSITION"))

(in-package "ROS")
;;//! \htmlinclude position.msg.html


(defclass arm_control::position
  :super ros::object
  :slots (_point ))

(defmethod arm_control::position
  (:init
   (&key
    ((:point __point) (make-array 4 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _point __point)
   self)
  (:point
   (&optional __point)
   (if __point (setq _point __point)) _point)
  (:serialization-length
   ()
   (+
    ;; float32[4] _point
    (* 4    4)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[4] _point
     (dotimes (i 4)
       (sys::poke (elt _point i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[4] _point
   (dotimes (i (length _point))
     (setf (elt _point i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;;
   self)
  )

(setf (get arm_control::position :md5sum-) "c8e7818df37db2cf138689cbda172d04")
(setf (get arm_control::position :datatype-) "arm_control/position")
(setf (get arm_control::position :definition-)
      "float32[4] point

")



(provide :arm_control/position "c8e7818df37db2cf138689cbda172d04")


