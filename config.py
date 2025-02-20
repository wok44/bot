from discord.ext.commands import (Flag, ColorConverter)

class Authorzation:
    token = '' # Bot Token
    prefix = ',' # Guild Prefix / Bot Prefix
    owner_ids = [1175783563602444329] # You're account ID 
    
    class database:
        
        host = ''
        password = ''
        database = ''
        user = ''
        port: int = 
class Color:
    
    normal = 0xffffff
    warn = 0xffffff
    approve = 0xffffff
    
class Emoji:
    approve = '<:approve:1341478993047715870>'
    locked = '<:locked:1341479172643618846>'
    deny = '<:deny:1341479139697233963>'
    warn = '<:warn:1341478970406731866>'
    information = '<:information:1341479155010769007>'
    negative = '<:negative:1341479025406644374>'
    add = '<:add:1341479123469729924>'
    unlocked = '<:unlocked:1341479008734412832>'