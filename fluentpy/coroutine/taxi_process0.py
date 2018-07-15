import argparse
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


def compute_delay(interval):
    """Compute action delay using exponential distribution"""
    return int(random.expovariate(1 / interval)) + 1


def taxi_process(ident, trips, start_time=0):
    """Yield to simulator issuing event at each state change"""
    time = yield Event(start_time, ident, LEAVE_GARAGE)
    for i in range(trips):
        prowling_ends = time + compute_delay(SEARCH_DURATION)
        time = yield Event(prowling_ends, ident, PICK_UP_PASSENGER)

        trip_ends = time + compute_delay(TRIP_DURATION)
        time = yield Event(trip_ends, ident, DROP_OFF_PASSENGER)

    yield Event(time + 1, ident, 'going home')


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
            try:
                next_event = active_proc.send(sim_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS, seed=None):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)  # get reproducible results

    taxis = {
        i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
        for i in range(num_taxis)
    }
    sim = Simulator(taxis)
    sim.run(end_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time',
                        type=int, default=DEFAULT_END_TIME,
                        help='simulation end time; default = %s' % DEFAULT_END_TIME)

    parser.add_argument('-t', '--taxis',
                        type=int, default=DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running; default = %s' % DEFAULT_NUMBER_OF_TAXIS)

    parser.add_argument('-s', '--seed',
                        type=int, default=None, help='random generator seed (for testing)')

    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)
