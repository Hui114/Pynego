'''Define the negotiation agent
Include:
1. property: agentid(agent name),
2. load config info from json file
3. create config via code
'''


class Agent(object):
    '''the basic agent class'''
    def __init__(self, agentname, strategy, configfile = None, utilityfile = None):
        self.agentid = agentname
        self.strategy = strategy
        #to load the agents config from the json file
        self.configfile = configfile
        self.utilityfile = utilityfile

    def get_config_info(self):
        return self.config




