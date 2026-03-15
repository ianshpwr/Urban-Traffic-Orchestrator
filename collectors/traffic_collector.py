import os
import sys
import traci
import csv

# Locate SUMO
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

sumoBinary = "sumo-gui"
sumoCmd = ["sumo-gui", "-c", "simulation/run.sumo.cfg", "--start", "--quit-on-end"]

# Start simulation
traci.start(sumoCmd)

log_file = open("logs/traffic_events.csv", "w", newline="")
writer = csv.writer(log_file)
writer.writerow(["time","vehicle","speed","waiting_time"])

while traci.simulation.getMinExpectedNumber() > 0:

    traci.simulationStep()

    vehicles = traci.vehicle.getIDList()

    print("Vehicles:", len(vehicles))

    for v in vehicles:
        speed = traci.vehicle.getSpeed(v)
        wait = traci.vehicle.getWaitingTime(v)

        writer.writerow([
            traci.simulation.getTime(),
            v,
            speed,
            wait
        ])
        
traci.close()
log_file.close()