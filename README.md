# MIGHT - drone control application
this is a Command & Control drone app.
it allows takeoff, landing, manual control over pitch&roll (movement in every direction with an option to adjust speed through rate).

the sitl is activated within an Ubuntu VM, by entering the ardupilot/ArduCopter dir in root bash and entering the following command:
sudo ../Tools/autotest/sim_vehicle.py --vehicle=ArduCopter --map --console

roadmap for expanding the project:
- health check - measure the connectivity latency between client and drone and provide a health status to the user (so we would know to not use manual mode in large latency)
- waypoint navigation in guided mode - navigation to waypoints using longitude and latitude
- smart break - pitch and roll in opposite direction to break faster automatically, helps for sharper movement and manuvering
- safety - identify connection loss between drone and user and taking automatic actions. example - stopping and switching to guided mode, and maybe returning home after a while
- testing - unitesting, integration testing and perhaps even real-life testing
- security - auth, encryption