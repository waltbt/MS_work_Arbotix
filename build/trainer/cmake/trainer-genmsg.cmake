# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "trainer: 3 messages, 0 services")

set(MSG_I_FLAGS "-Itrainer:/home/ben/gripper_proj_2/src/trainer/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(trainer_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg" NAME_WE)
add_custom_target(_trainer_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "trainer" "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg" ""
)

get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg" NAME_WE)
add_custom_target(_trainer_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "trainer" "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg" ""
)

get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg" NAME_WE)
add_custom_target(_trainer_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "trainer" "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/trainer
)
_generate_msg_cpp(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/trainer
)
_generate_msg_cpp(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/trainer
)

### Generating Services

### Generating Module File
_generate_module_cpp(trainer
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/trainer
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(trainer_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(trainer_generate_messages trainer_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_cpp _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_cpp _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_cpp _trainer_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(trainer_gencpp)
add_dependencies(trainer_gencpp trainer_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS trainer_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/trainer
)
_generate_msg_eus(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/trainer
)
_generate_msg_eus(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/trainer
)

### Generating Services

### Generating Module File
_generate_module_eus(trainer
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/trainer
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(trainer_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(trainer_generate_messages trainer_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_eus _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_eus _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_eus _trainer_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(trainer_geneus)
add_dependencies(trainer_geneus trainer_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS trainer_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/trainer
)
_generate_msg_lisp(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/trainer
)
_generate_msg_lisp(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/trainer
)

### Generating Services

### Generating Module File
_generate_module_lisp(trainer
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/trainer
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(trainer_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(trainer_generate_messages trainer_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_lisp _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_lisp _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_lisp _trainer_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(trainer_genlisp)
add_dependencies(trainer_genlisp trainer_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS trainer_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/trainer
)
_generate_msg_nodejs(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/trainer
)
_generate_msg_nodejs(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/trainer
)

### Generating Services

### Generating Module File
_generate_module_nodejs(trainer
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/trainer
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(trainer_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(trainer_generate_messages trainer_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_nodejs _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_nodejs _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_nodejs _trainer_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(trainer_gennodejs)
add_dependencies(trainer_gennodejs trainer_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS trainer_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/trainer
)
_generate_msg_py(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/trainer
)
_generate_msg_py(trainer
  "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/trainer
)

### Generating Services

### Generating Module File
_generate_module_py(trainer
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/trainer
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(trainer_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(trainer_generate_messages trainer_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/color_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_py _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/TOF_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_py _trainer_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ben/gripper_proj_2/src/trainer/msg/IR_sensor_data.msg" NAME_WE)
add_dependencies(trainer_generate_messages_py _trainer_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(trainer_genpy)
add_dependencies(trainer_genpy trainer_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS trainer_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/trainer)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/trainer
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(trainer_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/trainer)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/trainer
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(trainer_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/trainer)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/trainer
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(trainer_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/trainer)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/trainer
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(trainer_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/trainer)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/trainer\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/trainer
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(trainer_generate_messages_py std_msgs_generate_messages_py)
endif()
