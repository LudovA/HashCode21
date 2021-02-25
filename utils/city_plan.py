class CityPlan:
    def __init__(self, n_intersections, streets, bonus_points, duration, cars, street_to_idx_dict, idx_to_street_list):
        self.n_intersections = n_intersections
        self.streets = streets
        self.bonus_points = bonus_points
        self.duration = duration
        self.cars = cars
        self.street_to_idx_dict = street_to_idx_dict
        self.idx_to_street_list = idx_to_street_list

        self.all_incoming_streets = self._calculate_all_incoming_streets()
        self.cars_on_all_streets = self._calculate_cars_on_all_streets()

    def incoming_streets(self, intersection):
        return [street_number for street_number, street in enumerate(self.streets) if street['connection'][1] == intersection]

    def outgoing_streets(self, intersection):
        return [street_number for street_number, street in enumerate(self.streets) if street['connection'][0] == intersection]

    def _calculate_cars_on_all_streets(self):
        cars_on_all_streets = [[] for _ in range(len(self.streets))]
        for car_number, path in enumerate(self.cars):
            for street_number in path:
                cars_on_all_streets[street_number].append(car_number)
        return cars_on_all_streets

    def _calculate_all_incoming_streets(self):
        return [self.incoming_streets(intersection) for intersection in range(self.n_intersections)]


def load_city_plan(filepath):
    street_number = 0
    car_number = 0

    first_line = True
    with open(filepath, 'r') as f:
        for line in f:
            line_split = line.rstrip().split(' ')
            if first_line:
                duration = int(line_split[0])
                n_intersections = int(line_split[1])
                n_streets = int(line_split[2])
                n_cars = int(line_split[3])
                bonus_points = int(line_split[4])

                idx_to_street_list = ['' for _ in range(n_streets)]
                street_to_idx_dict = {}
                street_list = [{'connection': (-1, -1), 'length': -1} for _ in range(n_streets)]
                car_list = [[] for _ in range(n_cars)]

                first_line = False
            else:
                # Check if line is about streets
                if street_number < n_streets:
                    street_list[street_number]['connection'] = (int(line_split[0]), int(line_split[1]))
                    idx_to_street_list[street_number] = line_split[2]
                    street_to_idx_dict[line_split[2]] = street_number
                    street_list[street_number]['length'] = (int(line_split[3]))

                    street_number += 1

                # Else add information for cars
                else:
                    car_list[car_number] = [street_to_idx_dict[street_name] for street_name in line_split[1:]]

                    car_number += 1

    return CityPlan(n_intersections=n_intersections,
                    streets=street_list,
                    bonus_points=bonus_points,
                    duration=duration,
                    cars=car_list,
                    street_to_idx_dict=street_to_idx_dict,
                    idx_to_street_list=idx_to_street_list)
