import os
import glob

data_path = "../data/"
SOURCE_PATH = data_path + "raw_data/InVivo/T1_resized"
patients = [f.path for f in os.scandir(SOURCE_PATH) if f.is_dir()]
for name in patients:
    pattern = os.path.join(name, "*")
    contents = glob.glob(pattern)
    files = [f for f in contents if os.path.isfile(f)]
    for [index, filename] in enumerate(files, start=1):
        old_name = r"" + str(filename)
        new_name = r"" + name + str(index).rjust(4, '0')
        # Renaming the file
        os.rename(old_name, new_name)
