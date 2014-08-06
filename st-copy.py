import sys
import os
import os.path
import platform
import shutil
from threading import Thread
import subprocess
import sublime
import sublime_plugin

PY2 = sys.version_info < (3, 0)

class HistorySave(sublime_plugin.EventListener):

    def on_post_save(self, view):

        def run(file_path):
            if PY2:
                file_path = file_path.encode("utf-8")

            if "src" in file_path and "main" in file_path and "webapp" in file_path:
                print("'webapp' file changed: '" + file_path + "'")
                main_path = file_path.split("src",1)[0]
                # get filepath relative to webapp folder
                relative_file_path = file_path.split("webapp",1)[1]
                # get 'target' folder path
                target_path = os.path.join(main_path, "target", "")
                # get all folders in 'target'
                target_folders = next(os.walk(os.path.dirname(target_path)))[1]
                # find '*-SNAPSHOT' folder into which file will be copied
                snapshot_folder = next((x for x in target_folders if "SNAPSHOT" in x), None)
                if snapshot_folder != None:
                    snapshot_path = os.path.join(target_path, snapshot_folder)
                    copy_path = os.path.join(snapshot_path,  relative_file_path[1:])
                    copy_path_dir = os.path.dirname(copy_path)
                    if not os.path.exists(copy_path_dir):
                        # create directory structure
                        os.makedirs(copy_path_dir)
                        print("  Created directory: '" + copy_path_dir + "'")

                    shutil.copyfile(file_path, copy_path)
                    print("  File:")
                    print("    " + file_path)
                    print("  Copied to:")
                    print("    " + copy_path)

        # process in a thread
        t = Thread(target=run, args=(view.file_name(),))
        t.start()