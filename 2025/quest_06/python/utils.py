def prepare_data_from_file(fname):
    with open(fname) as file:
        return file.readline()
