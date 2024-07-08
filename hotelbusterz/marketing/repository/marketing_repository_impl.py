from datetime import datetime, timedelta

from account.entity.action_type import ActionType
from marketing.entity.models import Marketing
from marketing.repository.marketing_repository import MarketingRepository


class MarketingRepositoryImpl(MarketingRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createDfFromNMonths(self, dataFrame, month):
        days = month * 30
        fromMonth = datetime.today() - timedelta(days)

        return dataFrame[dataFrame["action_time"] >= fromMonth]

    def createCountActionPerId(self, dataFrame):
        groupByDataFrame = dataFrame.groupby(["account_id", "action"]).count()

        result = {}
        for (account_id, action), action_time in groupByDataFrame.iterrows():

            if account_id not in result:
                result[account_id] = {}
            result[account_id][action] = int(action_time.values[0])

        return result

    def createAARRR(self, accountList, dict):
        for account in accountList:
            if account.id in dict.keys():
                aarrrPerId = Marketing.objects.create(
                    account=account,
                    acquisition=1,
                    activation=1,
                    revenue=1 if dict.get(ActionType.ORDER) else 0,
                    retention=1 if dict.get(ActionType.ORDER, 0) >= 2 else 0,
                    referral=1 if dict.get(ActionType.BUTTON_REFERRAL) else 0)
            else:
                aarrrPerId = Marketing.objects.create(
                    account=account,
                    acquisition=1,
                    activation=0,
                    revenue=0,
                    retention=0,
                    referral=0)

        return aarrrPerId

