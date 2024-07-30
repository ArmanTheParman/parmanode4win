from variables import *
global pco, ico, dbo, tmpo, beforeo, aftero, differenceo
#parmanode_config directory needs to exist
pco = config(pc) #parmanode conf object
ico = config(ic) #installed conf object
dbo = config(db) #debug log object
tmpo = config(tmp) #temp config object - not config, but useful methods
beforeo = config(before)
aftero = config(after)
differenceo = config(difference)