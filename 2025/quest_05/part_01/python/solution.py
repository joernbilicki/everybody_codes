from os import path

workdir = path.abspath(path.dirname(__file__))

# Create the absolute path to the given data file
fname = path.join(workdir, "../everybody_codes_e2025_q05_p1.txt")

main_quality_value = ""
quality_data = []
with open(fname) as file:
    raw_data = file.readline()
    main_data = raw_data.split(":")
    main_quality_value = main_data[0]
    quality_data = list(map(int, main_data[1].split(",")))

# The fishbone is finally a list of inner lists.
# Every inner list contains up to three elements:
# - Index 0: The value less than the spine value
# - Index 1: The spine value
# - Index 2: The value greater than the spine value
# The resulting quality is equal to the concatenation of the spine values (index 1).
fishbone = []

NaN = -1

def add_new_spine(quality_data, fishbone):
    new_spine = [NaN, quality_data, NaN]
    fishbone.append(new_spine)

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

quality = ""
for spine in fishbone:
    quality += str(spine[1])
# Answer for: What is the quality of the sword currently being recorded by the armourer?
print(quality)