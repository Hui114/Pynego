'''Define the action of the agents
Include:
AOP Base Action
1. Accept
2. Offer(Bid)
3. EndNegotiation\

4. Partial Offer
5. Partial Accept

AOP Advance Action
4. LeaveNegotiation
5. JoinNegotiation
6. Communicate

AOP
'''

def create_actionID():
    '''get the actionID via timestamp'''
    pass

class Action(object):

    def __init__(self, agentID, actionID):
        self.agentid = agentID
        self.actionid = actionID

    @classmethod
    def get_agentid(self):
        '''get the agentid of the action'''
        return self.agentid

    @classmethod
    def get_actionid(self):
        '''get the actionid of the action'''
        return self.actionid


class Accept(Action):
    '''accept '''
    def __init__(self, Bid):
        self.bid = Bid

    def description(self):
        '''get the description of the content'''
        des = self.bid.getContent()
        return ("Accept" + des)