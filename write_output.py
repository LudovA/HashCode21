import os
import pickle

working_dir = os.getcwd()


def write_output(scheme, input_filepath, output_filepath):
    filename = os.path.basename(input_filepath).split('.')[0]
    idx_to_street_list = pickle.load(open(os.path.join(working_dir, 'data', 'idx_to_street', filename + '.p'), 'rb'))

    with open(input_filepath, 'r') as input_file:
        first_line = input_file.readline().rstrip().split(' ')
        n_intersections = int(first_line[1])

    with open(output_filepath, 'w') as output_file:
        output_file.write(f"{n_intersections}\n")
        for intersection_number, intersection_scheme in enumerate(scheme):
            output_file.write(f"{intersection_number}\n"
                              f"{len(intersection_scheme)}\n")
            for [street_number, wait_time] in intersection_scheme:
                output_file.write(f"{idx_to_street_list[street_number]} {wait_time}\n")

