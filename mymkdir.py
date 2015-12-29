def mymkdir(dir_name,delete=False):
    import os
    import shutil
    if delete:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            os.mkdir(dir_name)
    else:
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            print('Directory '+"'"+dir_name+"'"+' had already existed!\nProgram have decided to use that directory!')