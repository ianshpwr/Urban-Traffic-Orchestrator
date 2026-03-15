def analyze_events(events):

    waiting = [e for e in events if e["type"] == "vehicle_waiting"]

    if len(waiting) > 10:
        return "High congestion forming"

    elif len(waiting) > 3:
        return "Moderate congestion detected"

    else:
        return "Traffic flow normal"