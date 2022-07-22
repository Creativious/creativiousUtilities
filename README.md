# General purpose prebuilt functions for any project that I work on
```diff
- HIGHLY LIKELY TO BREAK FOR EACH VERSION, BACKUP BEFORE UPDATING, AND REQUIRE SPECIFIC VERSION IF YOU ARE TO USE THIS
```

<h3 align="center">Not designed for use for anyone other then myself, so bare with caution</h3>

-----

<h1 align="center">Modules</h1>

----
<h2 align="center">Logging</h2>
```Python
from creativiousUtilities.logging import Logger

theLogger = Logger(name="standardLog", logfile="logs/log.log").getLogger()
theLogger.log("This is logged")
```

<h3 align="center">Plans</h3>
* Reformat to be more user friendly
* Create a better way to get the logger object
* Create more config options
* Add YAML integration
----
<h2 align="center">Discord</h2>
```python
from discord.ext import commands
import discord
from creativiousUtilities import discord as discUtils
from discord.commands.context import ApplicationContext
# Optionally you can add logging too!
from creativiousUtilities.logging import Logger

class CoreBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
    #     self.logger = Logger(name="BotLog", debug=True, logfile="log.log").getLogger()
    #     self.logger.info("Bot Startup!")
    # 
    # def shutdown(self):
    #     self.logger.info("Bot has shutdown!")
    # 
    # def __del__(self):
    #     self.logger.warning("Bot has been garbage collected")

client = CoreBot('$')

@client.event
async def on_ready():
    #client.logger.info(f"Logged into {str(client.user.name)} ({str(client.user.id)})")
    print(f"Logged into {str(client.user.name)} ({str(client.user.id)})")
    discUtils.loadAllCogs(client, "cogs/") # If you have cogs this will automatically load them
    activity = discord.Game(name="Message me with /help to get started")
    client.remove_command("help")
    await client.change_presence(activity=activity, status=discord.Status.online)

@client.slash_command()
async def help(ctx: ApplicationContext):
    "Bot Help Command"
    helpCommandObject = discUtils.HelpCommand(client)
    helpEmbed = helpCommandObject.getHelp(0)
    await ctx.respond(embed=helpEmbed)

client.run("TOKEN")
# client.shutdown()
```
<h3 align="center">Plans</h3>
* Make some changes to the help command to have cog support
* YAML integration
* A few bug fixes

-----
<h2 align="center">Logging</h2>

default_config.yaml
```yaml
test messages:
  message 1: Hello World # This message will be printed
```
yamltest.py
```python
from creativiousUtilities.config import YAMLConfig

config = YAMLConfig("config/default_config.yaml", "config/config.yaml").load()

print("Message 1: " + config['test messages']["message 1"])
```


-----

### Todo

- [ ] Updated SQL Module for MySQL
- [ ] Add SQL Module to README.md
- [ ] Create GMOD Module
- [ ] Add GMOD Module to README.md
