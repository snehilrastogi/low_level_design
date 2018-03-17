from auto_assignment import constants
from auto_assignment.services.strategy.low_first_mile_strategy import AssignmentStrategyLowFirstMile
from auto_assignment.services.strategy.premium_customer_strategy import AssignmentStartegyPremiumCustomer


class StrategyFactory(object):
    @classmethod
    def factory(self, strategy_type):
        if strategy_type == constants.ASSIGNMENT_STRATEGIES[constants.LOW_FIRST_MILE_STRATEGY]:
            return AssignmentStrategyLowFirstMile()

        if strategy_type == constants.ASSIGNMENT_STRATEGIES[constants.PREMIUM_FIRST_MILE_STRATEGY]:
            return AssignmentStartegyPremiumCustomer()
