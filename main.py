# %% IMPORTING MODULES
from utils import city_plan
from utils import generate_algorithm



# %% DEFINE CONSTANTS


# %% FUNCTIONS
def main():
    plan = city_plan.load_city_plan("data/input/a.txt")

    print(generate_algorithm.generate_algorithm(plan))

    print("Hello world.")


# %% MAIN
if __name__ == '__main__':
    main()
