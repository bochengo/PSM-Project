"PSM-Project - NMPC implementation" 

The main objective of the research is to implement an NMPC model on-line to study the  control strategies of the liquid level (flow rate of F3 controlled by aperture of valve5) and temperature (coolant jacket controlled by aperture of valve3) in a pilot plant CSTR to achieve the desired setpoints.

Our approach to this model includes several features. First, we will use a Newton-type algorithm to structure the system expecting that it will lead to fewer iterations[3]. Secondly, multiple shooting methods will be implemented for unstable system solutions to compensate for the failures by direct integration methods. Lastly, this model will be extended to include integral action[4]. This is for removing the steady-state offset from step disturbances. 

The flow rates of the outlet and the coolant are manipulated by a Proportional Integral(PI) controller which controls the Vc5 and Vc3 valves to setpoints given by the NMPC model. However, the prediction of F3 will be compared with the corresponding NMPC setpoint to calculate the error of the PI controller. Also, the prediction of Ca will be used to initialize the model for each step. In simpler words, a NMPC controller will be demonstrated for tracking set point changes and different tuning parameters for the system described above.

