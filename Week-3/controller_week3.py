from controller import Robot

# Inisialisasi robot
robot = Robot()

# Set time step (interval waktu simulasi)
timestep = int(robot.getBasicTimeStep())

# Ambil referensi ke motor roda kiri dan kanan
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Set posisi roda agar bisa bergerak bebas (tanpa batasan posisi)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set kecepatan roda agar robot bergerak maju
left_motor.setVelocity(6.28)  # Kecepatan maksimum
right_motor.setVelocity(6.28) # Kecepatan maksimum

# Loop utama simulasi
while robot.step(timestep) != -1:
    # Tidak ada kontrol tambahan, robot akan terus bergerak maju
    pass
