import queue
import random

import collections

GOING_HOME = 'going home'
DROP_OFF_PASSENGER = 'drop off passenger'
LEAVE_GARAGE = 'leave garage'
PICK_UP_PASSENGER = 'pick up passenger'

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', ['time', 'proc', 'action'])


def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""
    if previous_action in [LEAVE_GARAGE, DROP_OFF_PASSENGER]:
        # new state is prowling
        interval = SEARCH_DURATION
    elif previous_action == PICK_UP_PASSENGER:
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == GOING_HOME:
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1 / interval)) + 1


def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, LEAVE_GARAGE)
    for i in range(trips):
        time = yield Event(time, ident, PICK_UP_PASSENGER)
        time = yield Event(time, ident, DROP_OFF_PASSENGER)

    yield Event(time, ident, 'going home')


class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        # prime
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event

            print('taix:', proc_id, proc_id * '\t', current_event)

            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


if __name__ == '__main__':
    num_taxis = 3
    taxis = {
        i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
        for i in range(num_taxis)
    }
    sim = Simulator(taxis)
    sim.run(80)
