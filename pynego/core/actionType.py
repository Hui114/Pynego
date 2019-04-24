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

Mediator Action
1. Vote
2. Reject

3. Vote multiple
4. Reject multiple
'''

def create_actionID():
    '''get the actionID via timestamp'''
    pass


class Bid(object):
    '''define the bid in the protocol'''
    def __init__(self):
        pass

    def getContent(self):
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
    def __init__(self, agentid, actionid, Bid):

        super(Accept, self).__init__(agentid, actionid)
        self.bid = Bid

    def description(self):
        '''get the description of the content'''
        des = self.bid.getContent()
        return ("Accept" + des)


class EndNegotiation(Action):
    '''end negotiation action'''
    def __init__(self, agentid, actionid, Bid = None):

        super(EndNegotiation, self).__init__(agentid, actionid)
        self.bid = Bid

    def description(self):
        '''get the description'''
        if self.bid:
            des = self.bid.getContent()
            return ("End Negoitiation with the Bid:" + des)
        else:
            return ("No agreement is achieved!")


class Offer(Action):
    '''offer(bid) action'''
    def __init__(self, agentid, actionid, Bid):
        super(Offer, self).__init__(agentid, actionid)
        self.bid = Bid

    def description(self):
        return ("Raise a potential offer:" + self.bid.getContent)


class PartialAccept(Action):
    '''partial accept and partial offer action'''
    def __init__(self, agentid, actionid, accept_subbid, bargin_subbid):

        super(PartialAccept, self).__init__(agentid, actionid)
        self.accept_bid = accept_subbid
        self.bargin_bid = bargin_subbid

    def description(self):
        '''get the description'''
        ac_bid = self.accept_bid.getContent()
        ba_bid = self.bargin_bid.getContent()
        return ("Achieve a partial aggreemnet:" + ac_bid + ", and raise a partial offer:" + ba_bid)


class JoinNegotiation(Action):
    '''this is the action for multiple agents in a negoptiation'''
    def __init__(self, agentid, actionid):
        super(JoinNegotiation, self).__init__(agentid, actionid)

    def description(self):
        return (self.agentid + " join the negotiation!")


class LeaveNegotiation(Action):
    '''this is the action for multiple agents in a negoptiation'''

    def __init__(self, agentid, actionid):
        super(LeaveNegotiation, self).__init__(agentid, actionid)

    def description(self):
        return (self.agentid + " join the negotiation!")


class CommunitewithTarget(Action):
    '''In a multiple agents negotiation, this is the action when one agent wants to communicate with its partner,
    this is a cooperative action'''
    def __init__(self, agentid, actionid, target_agentid, information):
        '''note that the information form is not defined yet!!!'''
        super(CommunitewithTarget, self).__init__(agentid, actionid)
        self.target_agent = target_agentid
        self.info = information

    def descrption(self):
        return (self.agentid + "communicate with " + self.target_agent)


class Vote(Action):
    '''this is the base action of a protocol with mediator'''
    def __init__(self, agentid, actionid, Bid):
        super(Vote, self).__init__(agentid, actionid)
        self.votebid = Bid

    def descrption(self):
        return (self.agentid + " vote for Bid: " + self.votebid.getContent())


class Reject(Action):
    '''this is the base action of a protocol with mediator'''

    def __init__(self, agentid, actionid, Bid):
        super(Reject, self).__init__(agentid, actionid)
        self.rejectbid = Bid

    def descrption(self):
        return (self.agentid + " reject Bid: " + self.rejectbid.getContent())


class VoteGroup(Action):
    '''the agent could vote for a group of Bids'''
    def __init__(self, agentid, actionid, Bidgroup):
        super(VoteGroup, self).__init__(agentid, actionid)
        self.vote_bidgroup = Bidgroup

    def description(self):
        pass


class RejectGroup(Action):
    '''the agent could vote for a group of Bids'''

    def __init__(self, agentid, actionid, Bidgroup):
        super(RejectGroup, self).__init__(agentid, actionid)
        self.reject_bidgroup = Bidgroup

    def description(self):
        pass

