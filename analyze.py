import matplotlib.pyplot as plt
import numpy

# backLegSensorValues = numpy.load('./data/back_leg_sensor_data.npy')
# frontLegSensorValues = numpy.load('./data/front_leg_sensor_data.npy')
frontLegMotorValues = numpy.load('./data/front_leg_motor_data.npy')
backLegMotorValues = numpy.load('./data/back_leg_motor_data.npy')

# plt.plot(backLegSensorValues, linewidth = 10, label = "Back Leg")
# plt.plot(frontLegSensorValues, linewidth = 3, label = "Front Leg")
plt.plot(frontLegMotorValues, label = "Front Leg")
plt.plot(backLegMotorValues, label = "Back Leg")
plt.legend()
plt.show()
