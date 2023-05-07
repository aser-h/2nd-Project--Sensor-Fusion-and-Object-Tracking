# Final Project: Sensor Fusion and Object Tracking

 This is the project for the second course in the Udacity Self-Driving Car Engineer Nanodegree Program : Sensor Fusion and Tracking.
___
# Introduction
In order to be able to start the project and keep up with me it is highly recommended check first the [UDACITY_README.md](UDACITY_README.md) which will brief you regarding the project and what models needs to be downloaded and fill you in with through the project.
## The final project consists of four main steps:
* Step 1: Implementing an extended Kalman filter.
* Step 2: Implementing track management including track state and track score, track initialization and deletion.
* Step 3: Implementing single nearest neighbour data association and gating.
* Step 4: Appling sensor fusion by implementing the nonlinear camera measurement model and a sensor visibility check.

The process will walk you through the implementation of sensor fusion system that is able to track vehicles over time with real-world camera and lidar measurements!
___
# Repository Overview
The final project uses the following folder structure and files:
* The main file for our lidar detection and tracking loop, which processes each measurement frame, is already known as `loop_over_dataset.py`
* `student/filter.py` contains the EKF class including predict and update step. EKF will be implemented in Step 1 of the project.
* `student/trackmanagement.py` includes two classes for tracking:
    * A class `Track` with attributes `x` and `P` for state and covariance. Both have fixed initial values implemented, but will be changed in Step 2.
    * A class `Trackmanagement` with a `track_list` to store all tracks, as well as methods to manage tracks. This will also be implemented in Step 2.
* `student/association.py` includes a class `Association` with logic to associate tracks to measurements and call the EKF update function with these associated measurements in `associate_and_update()`. Data association will be implemented in Step 3.
* `student/measurements.py` includes two classes for measurement handling:
    * A class `Sensor` which distinguishes between names `camera` and `lidar`. It includes the sensor's calibration data, field of view and coordinate transforms as well as the EKF measurement model.
    * A class `Measurement` with the attributes `z` and `R` for the measurement vector and corresponding covariance. The lidar measurement code is given and the camera measurement WILL be implemented (not given) for sensor fusion in Step 4.

* All parameters for tracking are included in `misc/params.py` . The parameters, such as the timestep, initialization parameters, track management settings, and gating threshold, should be loaded where needed. The parameters do not have to be modified. However, they can be tuned further after the project is completed to improve tracking, for example, by using the lidar standard deviation evaluated in the mid-term project. Changing parameters is recommended only after completion of Step 4 to avoid additional error sources.

___

## Project Instructions Step 1
### What is this task about?
In Step 1 of the final project, an EKF will be implemented to track a single real-world target with lidar measurement input over time!
### Task preparation
First of all, the same model settings for the Resnet neural network as in the mid-term project need to be applied. Therefore, the code solution from the mid-term project workspace in `student/objdet_detect.py` should be copied into the final project workspace.

To select the right single-target-scenario, apply the following settings in `loop_over_dataset.py`:
* Select Sequence 2 (`training_segment-10072231702153043603_5725_000_5745_000_with_camera_labels.tfrecord`) by uncommenting this line in loop_over_dataset.py and commenting the other sequences.
* Set `show_only_frames = [150, 200]` in order to limit the sequence to frames 150 to 200. This is the time span where our single object is visible.
* Set `configs_det = det.load_configs(model_name='fpn_resnet')` to use the Resnet neural network architecture. Note that Darknet is not applicable here because it does not estimate the height.
* Set `configs_det.lim_y = [-5, 10]` to limit the y-range and remove other targets left and right of our target. To do so, uncomment the respective line.
* Set `exec_detection = []` to skip the lidar detection for faster execution and to load the lidar results from file instead.
* Set `exec_tracking = ['perform_tracking']` to activate tracking.
* Set `exec_visualization = ['show_tracks']` for track visualization.
### Where to find this task?
This task involves writing code within the file `student/filter.py`

### Results






















  






