from utils import city_plan
import numpy as np

def generate_algorithm(plan):
    numof_intersections = plan.n_intersections

    algo = []

    for intersection in range(numof_intersections):
        time = np.zeros(len(plan.all_incoming_streets[intersection]))
        for i, street in enumerate(plan.all_incoming_streets[intersection]):
            time[i] += len(plan.cars_on_all_streets[street])

        time = time / np.min(time)
        time = np.ceil(time)
        print(time)
        algo.append([[s,t] for s,t in zip(plan.all_incoming_streets[intersection],time)])

    return algo
