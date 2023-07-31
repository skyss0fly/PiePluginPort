from piemc.plugin.PluginBase import PluginBase
from piemc.plugin.Terminal import Terminal

   import requests 
import os
class Main(PluginBase):
  def on_enable(self):
    self.logger.info(Terminal.green("[PiePluginPort] enabling..."))
    
 def onCommand(sender, command, label, args):
  if command == "getplugin":
    if len(args) == 1:
      pluginname = args[0]
      try:
        plugin = PieMC.getPluginManager().getPlugin(pluginname)
        sender.sendMessage("Plugin " + pluginname + " found!")
      except:
        sender.sendMessage("Plugin " + pluginname + " not found!")
    else:
      sender.sendMessage("Usage: /getplugin <pluginname>")
