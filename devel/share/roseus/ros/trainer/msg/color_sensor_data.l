;; Auto-generated. Do not edit!


(when (boundp 'trainer::color_sensor_data)
  (if (not (find-package "TRAINER"))
    (make-package "TRAINER"))
  (shadow 'color_sensor_data (find-package "TRAINER")))
(unless (find-package "TRAINER::COLOR_SENSOR_DATA")
  (make-package "TRAINER::COLOR_SENSOR_DATA"))

(in-package "ROS")
;;//! \htmlinclude color_sensor_data.msg.html


(defclass trainer::color_sensor_data
  :super ros::object
  :slots (_rgb_values _color_temp _lux ))

(defmethod trainer::color_sensor_data
  (:init
   (&key
    ((:rgb_values __rgb_values) (make-array 4 :initial-element 0 :element-type :integer))
    ((:color_temp __color_temp) 0)
    ((:lux __lux) 0.0)
    )
   (send-super :init)
   (setq _rgb_values __rgb_values)
   (setq _color_temp (round __color_temp))
   (setq _lux (float __lux))
   self)
  (:rgb_values
   (&optional __rgb_values)
   (if __rgb_values (setq _rgb_values __rgb_values)) _rgb_values)
  (:color_temp
   (&optional __color_temp)
   (if __color_temp (setq _color_temp __color_temp)) _color_temp)
  (:lux
   (&optional __lux)
   (if __lux (setq _lux __lux)) _lux)
  (:serialization-length
   ()
   (+
    ;; int32[4] _rgb_values
    (* 4    4)
    ;; int32 _color_temp
    4
    ;; float32 _lux
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[4] _rgb_values
     (dotimes (i 4)
       (write-long (elt _rgb_values i) s)
       )
     ;; int32 _color_temp
       (write-long _color_temp s)
     ;; float32 _lux
       (sys::poke _lux (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[4] _rgb_values
   (dotimes (i (length _rgb_values))
     (setf (elt _rgb_values i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     )
   ;; int32 _color_temp
     (setq _color_temp (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _lux
     (setq _lux (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get trainer::color_sensor_data :md5sum-) "7c8cfe28df9aa44956a941b8c260653a")
(setf (get trainer::color_sensor_data :datatype-) "trainer/color_sensor_data")
(setf (get trainer::color_sensor_data :definition-)
      "int32[4] rgb_values
int32 color_temp
float32 lux

")



(provide :trainer/color_sensor_data "7c8cfe28df9aa44956a941b8c260653a")


