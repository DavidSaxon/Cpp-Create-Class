import sublime, sublime_plugin
from subprocess import call

class CppCreateClassCommand(sublime_plugin.WindowCommand):

    def run(self):

        call(["python", "/home/david/.config/sublime-text-2/Packages/" +
            "Cpp-Create-Class/CppCreateClass.py"])
