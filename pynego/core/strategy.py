'''The negotiation strategy of the agents.

'''

def getvalidateaction(protocolname):
    '''to get the validate actions in the strategy, current have two'''


class NegoStrategy(object):

    def __init__(self, protocolname):
        self.actions = getvalidateaction(protocolname)

    def get_utility(self):
        pass

    def choose_action(self):
        pass

    def generate_offer(self):
        pass
