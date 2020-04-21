;; Auto-generated. Do not edit!


(when (boundp 'arm_control::command)
  (if (not (find-package "ARM_CONTROL"))
    (make-package "ARM_CONTROL"))
  (shadow 'command (find-package "ARM_CONTROL")))
(unless (find-package "ARM_CONTROL::COMMAND")
  (make-package "ARM_CONTROL::COMMAND"))

(in-package "ROS")
;;//! \htmlinclude command.msg.html


(defclass arm_control::command
  :super ros::object
  :slots (_pose ))

(defmethod arm_control::command
  (:init
   (&key
    ((:pose __pose) (make-array 6 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _pose __pose)
   self)
  (:pose
   (&optional __pose)
   (if __pose (setq _pose __pose)) _pose)
  (:serialization-length
   ()
   (+
    ;; int32[6] _pose
    (* 4    6)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[6] _pose
     (dotimes (i 6)
       (write-long (elt _pose i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[6] _pose
   (dotimes (i (length _pose))
     (setf (elt _pose i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     )
   ;;
   self)
  )

(setf (get arm_control::command :md5sum-) "1a1a3549ea1fbd90af851784fda8677a")
(setf (get arm_control::command :datatype-) "arm_control/command")
(setf (get arm_control::command :definition-)
      "int32[6] pose

")



(provide :arm_control/command "1a1a3549ea1fbd90af851784fda8677a")


