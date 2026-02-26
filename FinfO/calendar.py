events = [(8.30, 9.30), (9.15, 10.30), (10.15, 11.30)]
event_points = []

for point in events:
    event_points.append((point[0], False))
    event_points.append((point[1], True))

# Sort the events in time
event_points.sort()

started_event_counter = 0
events_count = 0
max_counter = 0

for event in event_points:
    events_count += 1
    if not event[1]:
        started_event_counter += 1
        if started_event_counter > max_counter:
            max_counter = started_event_counter
        
    else:
        started_event_counter -= 1

print(max_counter)
