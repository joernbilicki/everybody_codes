def prepare_data_from_file(fname):
    """
    Reads the sword data line by line into a dictionary.

    :param fname: The name of the file with the sword data.

    :return: Dictionary with the sword number as a key and the quality data as a list of integer values.
    """
    sword_quality = {}
    
    with open(fname) as file:
        for line in file:
            sword_data = line.split(":")
            sword_number = sword_data[0]
            quality_data = list(map(int, sword_data[1].split(",")))
            sword_quality[sword_number] = quality_data
    
    return sword_quality

NaN = -1
def add_new_spine(quality_data, fishbone):
    """
    Creates a new spine and adds it to a given list.
    Every spimne contains up to three elements:
    - Index 0: The value less than the spine value (init value: NaN).
    - Index 1: The spine value (equals to quality_data).
    - Index 2: The value greater than the spine value (init value: NaN).

    :param quality_data: quality value for the new spine.
    :param fishbone: List to add the new spine to.
    """
    new_spine = [NaN, quality_data, NaN]
    fishbone.append(new_spine)


def create_fishbone(quality_data):
    """
    Creates the complete fishbone.
    The fishbone is finally a list of inner lists.
    The resulting quality is equal to the concatenation of the spine values (index 1).

    :param quality_data: List of quality values.
    :return: The complete fishbone.
    """
    fishbone = []

    add_new_spine(quality_data[0], fishbone)

    for i in range(1, len(quality_data)):
        next_value = quality_data[i]
        new_spine_required = True
        for current_spine in fishbone:
            if next_value < current_spine[1] and current_spine[0] == NaN:
                current_spine[0] = next_value
                new_spine_required = False
                break
            elif next_value > current_spine[1] and current_spine[2] == NaN:
                current_spine[2] = next_value
                new_spine_required = False
                break
        if new_spine_required:
            add_new_spine(next_value, fishbone)

    return fishbone


def get_quality_of(fishbone):
    """
    Extracts the quality of a fishbone.

    :param fishbone: The fishbone to evaluate.
    :return: The result as string.
    """
    quality = ""
    for spine in fishbone:
        quality += str(spine[1])
    return quality
