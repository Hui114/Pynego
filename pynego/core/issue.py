'''the negotiation usually contain multiple issues, here we define different kind of issues.
Include:
1. DiscreteIssue
2. RealIssue
3. IntegerIssue

User can check the value via define the checkInRange function. and define the validate value of the issue.
'''

class Issue(object):

    def __init__(self, name, id):
        self.issuename = name
        self.issueid = id

    def getIssuename(self):
        return self.issuename

    def getIssueid(self):
        return self.issueid


class DiscreteIssue(Issue):

    def __init__(self, name, id, valuelist):

        super(DiscreteIssue, self).__init__(name, id)
        self.issuespace = valuelist
        self.valuenum = len(valuelist)

    def checkInRange(self, value):
        '''check if the value is validate'''
        if value in self.issuespace:
            return True
        else:
            raise ValueError(str(value) + 'of' + self.issuename + 'is illegal! please check!')

    def getContent(self):
        content = [self.valuenum, self.issuespace]
        return content


class IntegerIssue(DiscreteIssue):

    def __init__(self, name, id, valuelist):
        super(IntegerIssue, self).__init__(name, id, valuelist)

    def checkInRange(self, value):
        if value in self.valuelist and isinstance(value, int):
            return True
        else:
            raise ValueError(str(value) + 'of' + self.issuename + 'is illegal! please check!')



class RangeIntegerIssue(Issue):

    def __init__(self, name, id, valuemin, valuemax):
        super(RangeIntegerIssue, self).__init__(name, id)
        self.min = valuemin
        self.max = valuemax
        self.valuenum = valuemax-valuemin+1

    def checkInRange(self, value):
        if value <= self.max and value >= self.min and isinstance(value, int):
            return True
        else:
            raise ValueError(str(value) + 'of' + self.issuename + 'is illegal! please check!')

    def getContent(self):
        content = [self.valuenum, self.min, self.max]
        return content


class RealIssue(Issue):

    def __init__(self, name, id, valuemin, valuemax):
        super(RealIssue, self).__init__(name, id)
        self.min = valuemin
        self.max = valuemax

    def checkInRange(self, value):
        if value <= self.max and value >= self.min:
            return True
        else:
            raise ValueError(str(value) + 'of' + self.issuename + 'is illegal! please check!')

    def getContent(self):
        content = [self.min, self.max]
        return content


