import sublime_plugin

class AppendNewlineCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):

    def insert_newline(point):
      self.view.insert(edit, point, '\n')

    for region in self.view.sel():
      line = self.view.line(region)
      line_end = line.end()

      insert_newline(line_end)
