from utils.plottenbakker import *
from utils.city_plan import load_city_plan
import os


#%% MAIN
working_dir = os.getcwd()
output_dir = os.path.join(working_dir, 'statistics', 'plots')
for filename in ['a', 'b', 'c', 'd', 'e', 'f']:
    filepath = os.path.join(working_dir, 'data', 'input', filename + '.txt')
    city_plan = load_city_plan(filepath)
    bins = len(city_plan.cars)

    # streets occupied
    occupation_values = [len(street_occupation) for street_occupation in city_plan.cars_on_all_streets]
    plot_histogram(values=occupation_values,
                   bins=bins,
                   title=f'{filename}_B{bins}_street_occupation',
                   output_dir=output_dir)

    # length of streets
    street_length_values = [street['length'] for street in city_plan.streets]
    plot_histogram(values=street_length_values,
                   bins=bins,
                   title=f'{filename}_B{bins}_street_lengths',
                   output_dir=output_dir)

    # how many incoming streets per intersection
    inc_streets_values = [len(inc_streets) for inc_streets in city_plan.all_incoming_streets]
    plot_histogram(values=inc_streets_values,
                   bins=bins,
                   title=f'{filename}_B{bins}_incoming_streets_per_intersection',
                   output_dir=output_dir)
