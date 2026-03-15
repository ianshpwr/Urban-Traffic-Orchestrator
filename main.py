import traci

from collectors.telemetry_collector import collect_vehicle_data
from event_engine.event_detector import detect_events
from agents.traffic_reasoning_agent import analyze_events

sumoCmd = ["sumo-gui", "-c", "simulation/run.sumo.cfg", "--start"]

traci.start(sumoCmd)

while traci.simulation.getMinExpectedNumber() > 0:

    traci.simulationStep()

    telemetry = collect_vehicle_data()

    events = detect_events(telemetry)

    report = analyze_events(events)

    print(report)

traci.close()