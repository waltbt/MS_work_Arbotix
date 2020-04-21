
(cl:in-package :asdf)

(defsystem "arm_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "command" :depends-on ("_package_command"))
    (:file "_package_command" :depends-on ("_package"))
    (:file "position" :depends-on ("_package_position"))
    (:file "_package_position" :depends-on ("_package"))
  ))