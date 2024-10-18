from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan roda
left_motor.setVelocity(3.14)  # Setengah dari kecepatan maksimum
right_motor.setVelocity(6.28) # Kecepatan maksimum

while robot.step(timestep) != -1:
    pass  # Robot bergerak melingkar
