import sublime, sublime_plugin
from subprocess import call

class CppCreateClassCommand(sublime_plugin.WindowCommand):

    def run(self):

        try:
            call(["ls"])
            call(["python", "/home/david/.config/sublime-text-2/Packages/" +
                "Cpp-Create-Class/CppCreateClass.py"])
            print "fuck"
        except Exception as e:
            print e
        print "Hello World"
