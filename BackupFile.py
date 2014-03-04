import sublime, sublime_plugin
import time
import os
import shutil

class BackupFileCommand(sublime_plugin.WindowCommand):
	def run(self, paths):
		filesrc = paths[0]
		filedst = paths[0]+"-"+time.strftime('%Y%m%d-%H%M%S')
		if os.path.isfile(filesrc):
			try:
				shutil.copy(filesrc, filedst);
			except:
				sublime.status_message("Error copying file")
