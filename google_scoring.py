# %% IMPORTING MODULES
import sys
import os


# %% FUNCTIONS
def collect_arguments():
    working_dir = os.getcwd()

    arguments = sys.argv
    if len(arguments) >= 4:
        print("Not all arguments used, only first two used, others are neglected.")
    elif len(arguments) != 3:
        raise ValueError("You should give two arguments!")

    # Make filepath
    input_google_filepath = os.path.join(working_dir, 'data', 'input', arguments[1])
    output_model_filepath = os.path.join(working_dir, 'data', 'output', arguments[2])
    if not os.path.isfile(input_google_filepath) or not os.path.isfile(output_model_filepath):
        raise ValueError(f"Could not find these files: {arguments[1]} and {arguments[2]} in their folders.")
    else:
        print(f"Using input google filepath: {input_google_filepath}")
        print(f"Using model output filepath: {output_model_filepath}")

    return input_google_filepath, output_model_filepath


def google_score(input_google_filename, output_model_filename):
    return


# %% MAIN
if __name__ == '__main__':
    input_google_filepath, output_model_filepath = collect_arguments()

    google_score(input_google_filepath, output_model_filepath)
