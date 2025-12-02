def prepare_data_from_file(fname):
    """
    Reads the first line of the given data file.

    :param fname: The name of the file.
    :return: The first line of the file.
    """
    with open(fname) as file:
        return file.readline()

def add_mentor(mentor_dict:dict, category:str):
    """
    Increases the mentor count by one in the given dictionary for the given category (mentor).
    Creates a new dictionary entry, if there is no entry for the given category.

    :param mentor_dict: Dictionary for mentors.
    :param category: Category (mentor).
    """
    if category not in mentor_dict: mentor_dict[category] = 0
    mentor_dict[category] += 1


def add_mentors_for_novice(novice_dict:dict, mentor_dict, category:str):
    """
    Increases the novice count by the amount of the corresponding mentor in the given dictionary for the given category (novice).
    Creates a new dictionary entry, if there is no entry for the given category.

    :param novice_dict: Dictionary for novices.
    :param mentor_dict: Dictionary for mentors.
    :param category: Category (novice).
    """
    if category not in novice_dict: novice_dict[category] = 0
    novice_dict[category] += mentor_dict[category.capitalize()]


def get_count(training_plan:str, novices:str) -> int:
    """
    Calculates the count for all novices an its corresponding mentors.

    :param training_plan: String of novices and mentors.
    :param mentors: String of all novices to calculate with. The mentors's string will automatically created from this string.
    :return: Count of possible novice-mentor pairs.
    """
    mentors = novices.upper()

    mentor_dict = {}
    novice_dict = {}

    for category in training_plan:
        if category in mentors: add_mentor(mentor_dict, category)
        if category in novices: add_mentors_for_novice(novice_dict, mentor_dict, category)

    novice_mentor_count = 0

    for novice in novice_dict:
        novice_mentor_count += novice_dict[novice]

    return novice_mentor_count
