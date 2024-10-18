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

# Set kecepatan roda untuk gerakan maju
left_motor.setVelocity(6.28)
right_motor.setVelocity(6.28)

# Inisialisasi sensor proximity
proximity_sensors = []
for i in range(8):
    sensor = robot.getDevice(f"ps{i}")
    sensor.enable(timestep)
    proximity_sensors.append(sensor)

# Fungsi untuk memeriksa apakah ada objek di depan
def detect_obstacle():
    for sensor in proximity_sensors[0:3]:  # Sensor depan (ps0, ps1, ps2)
        if sensor.getValue() > 100:  # Threshold deteksi objek
            return True
    return False

# Loop utama simulasi
while robot.step(timestep) != -1:
    # Jika sensor proximity mendeteksi objek di depan, hentikan robot
    if detect_obstacle():
        left_motor.setVelocity(0)  # Berhenti
        right_motor.setVelocity(0)  # Berhenti
    else:
        left_motor.setVelocity(6.28)  # Maju
        right_motor.setVelocity(6.28)  # Maju
