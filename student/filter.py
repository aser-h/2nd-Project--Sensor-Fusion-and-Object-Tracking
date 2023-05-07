# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        self.dim_state = params.dim_state # process model dimension 
        self.dt = params.dt # time increment
        self.q = params.q # process noise variable for Kalman filter Q


    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        
        dt = self.dt
        # System Matrix
        return np.matrix([[1,0,0,dt,0,0],
                          [0,1,0,0,dt,0],
                          [0,0,1,0,0,dt],
                          [0,0,0,1,0,0],
                          [0,0,0,0,1,0],
                          [0,0,0,0,0,1]])
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############

        dt = self.dt
        q = self.q
        q1 = ((dt**3)/3) * (q) 
        q2 = ((dt**2)/2) * (q) 
        q3 = dt * q 
        
        return np.matrix([[q1, 0,  0,  q2, 0,  0 ],
                          [0,  q1, 0,  0,  q2, 0 ],
                          [0,  0,  q1, 0,  0,  q2],
                          [q2, 0,  0,  q3, 0,  0 ],
                          [0,  q2, 0,  0,  q3, 0 ],
                          [0,  0,  q2, 0,  0,  q3]])
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############

        F = self.F()    # computes the state transition matrix F using the F() method
        Q = self.Q()    # computes the process noise covariance matrix Q using the Q() method
        x = F * track.x # prediction
        P = F * track.P * F.transpose() + Q # covariance prediction
        track.set_x(x)  # update the state estimate and covariance estimate, 
        track.set_P(P)  # of the track object with the predicted values

        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        
        H = meas.sensor.get_H(track.x) 
        gamma = self.gamma(track, meas) # residual
#       gamma = z - H*x # residual
        S = self.S(track, meas, H) 
        K = track.P * H.transpose()* np.linalg.inv(S) # Kalman gain
        x = track.x + K * gamma 
        I = np.identity(self.dim_state)
        P = (I - K * H) * track.P 
        track.set_x(x)
        track.set_P(P)
        track.update_attributes(meas)
        
        ############
        # END student code
        ############ 
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############

        gamma = meas.z - meas.sensor.get_hx(track.x) # residual 
        return gamma
    
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        S = H * track.P * H.transpose() + meas.R # covariance of residual
        return S
    
        ############
        # END student code
        ############ 