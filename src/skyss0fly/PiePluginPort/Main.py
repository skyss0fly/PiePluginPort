from piemc.plugin.PluginBase import PluginBase
from piemc.plugin.Terminal import terminal

class Main(PluginBase):
  def on_enable(self):
    self.logger.info(Terminal.green("[PiePluginPort] enabling..."))
    
