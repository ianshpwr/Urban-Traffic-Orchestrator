import traci
import csv

sumoCmd = ["sumo-gui", "-c", "../simulation/run.sumo.cfg"]

traci.start(sumoCmd)

log_file = open("../logs/traffic_events.csv","w",newline="")
writer = csv.writer(log_file)

writer.writerow(["time","vehicle","speed","waiting_time"])

while traci.simulation.getMinExpectedNumber() > 0:

    traci.simulationStep()
    vehicles = traci.vehicle.getIDList()

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