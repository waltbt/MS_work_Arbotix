
(cl:in-package :asdf)

(defsystem "trainer-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IR_sensor_data" :depends-on ("_package_IR_sensor_data"))
    (:file "_package_IR_sensor_data" :depends-on ("_package"))
    (:file "TOF_sensor_data" :depends-on ("_package_TOF_sensor_data"))
    (:file "_package_TOF_sensor_data" :depends-on ("_package"))
    (:file "color_sensor_data" :depends-on ("_package_color_sensor_data"))
    (:file "_package_color_sensor_data" :depends-on ("_package"))
  ))