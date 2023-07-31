from piemc.plugin.PluginBase import PluginBase
from piemc.plugin.Terminal import Terminal

   import requests 
import os
class Main(PluginBase):
  def on_enable(self):
    self.logger.info(Terminal.green("[PiePluginPort] enabling..."))
    
 def on_command(self):

url = 'http://www.PieMC-Dev.github.io/Plugins/'
folder_name = 'Plugins'

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for filename in os.listdir(url):
    r = requests.get(url + filename, allow_redirects=True)
    open(folder_name + '/' + filename, 'wb').write(r.content)
