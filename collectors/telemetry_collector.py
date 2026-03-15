import traci

def collect_vehicle_data():

    vehicles = traci.vehicle.getIDList()
    telemetry = []

    for v in vehicles:

        telemetry.append({
            "vehicle": v,
            "speed": traci.vehicle.getSpeed(v),
            "waiting_time": traci.vehicle.getWaitingTime(v),
            "acceleration": traci.vehicle.getAcceleration(v)
        })

    return telemetry