# MIGHT - drone control application
this is a Command & Control drone app.
it allows takeoff, landing, manual control over pitch&roll (movement in every direction with an option to adjust speed through rate).

the sitl is activated within an Ubuntu VM, by entering the ardupilot/ArduCopter dir in root bash and entering the following command:
sudo ../Tools/autotest/sim_vehicle.py --vehicle=ArduCopter --map --console

roadmap for expanding the project:
- error handling - errors in backend will be caught and sent to the frontend as an alert.
- health check - manage a service which specifies in receiving an api health check call every X seconds, and if there isn't one return home Immediately
- waypoint navigation in guided mode - navigation to waypoints using longitude and latitude
- smart break - pitch and roll in opposite direction to break faster automatically, helps for sharper movement and manuvering