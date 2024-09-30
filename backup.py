# f string formatted sring
import shutil
import datetime
import os
def backup_file(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination , f"backup_{today}")
    shutil.make_archive(backup_file_name , 'gztar' , source)

source = "C:\Users\Soham\Documents\Python_For_Devops\mysource"
destination = "C:\Users\Soham\Documents\Python_For_Devops\pybackup"
backup_file(source, destination)



