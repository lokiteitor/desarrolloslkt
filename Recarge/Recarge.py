import sublime, sublime_plugin,os

class recargeCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        os.system('rsync -avv --delete --no-whole-file $HOME/git/Vantec/ /home/www/VantecWeb/')
        os.system('wmctrl -a VANTEC.MX')
        

