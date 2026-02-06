import matplotlib.pyplot as plt
import numpy

backLegSensorValues = numpy.load('./data/back_leg_sensor_data.npy')
frontLegSensorValues = numpy.load('./data/front_leg_sensor_data.npy')

plt.plot(backLegSensorValues, linewidth = 10, label = "Back Leg")
plt.plot(frontLegSensorValues, linewidth = 3, label = "Front Leg")
plt.legend()
plt.show()