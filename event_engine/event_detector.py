from config.settings import WAITING_TIME_THRESHOLD

def detect_events(telemetry):

    events = []

    for data in telemetry:

        if data["speed"] == 0 and data["waiting_time"] > WAITING_TIME_THRESHOLD:

            events.append({
                "type": "vehicle_waiting",
                "vehicle": data["vehicle"],
                "waiting_time": data["waiting_time"]
            })

    return events