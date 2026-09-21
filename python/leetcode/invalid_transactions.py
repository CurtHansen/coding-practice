# Based on https://leetcode.com/problems/invalid-transactions/
from typing import List


from collections import namedtuple
Transaction = namedtuple('Transaction', ['name', 'time', 'amount', 'city'])


class Solution:

    def create_tuple(self, transaction):
        transaction_list = transaction.split(',')
        transaction_list[1:3] = map(int, transaction_list[1:3])
        transaction_tuple = Transaction(*transaction_list)
        return transaction_tuple

    def process_group(self, group):
        n = len(group)
        invalid = [False] * n

        for idx, transaction in enumerate(group):
            if transaction.amount > 1000:
                invalid[idx] = True
            if idx < n - 1:
                next_transaction = group[idx + 1]
                if transaction.city != next_transaction.city and\
                        abs(transaction.time - next_transaction.time) <= 60:
                    invalid[idx] = True
                    invalid[idx + 1] = True

        for idx, isinvalid in enumerate(invalid):
            if isinvalid:
                self.ans.append(",".join(map(str, group[idx])))

    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        self.ans = []

        transaction_tuples = list()
        for transaction in transactions:
            transaction_tuples.append(self.create_tuple(transaction))
        transaction_tuples = sorted(transaction_tuples, key=lambda x: (x.name, x.time))

        common_name_transactions = []
        current_name = None
        for transaction in transaction_tuples:
            if current_name == transaction.name:
                common_name_transactions.append(transaction)
            else:
                self.process_group(common_name_transactions)
                common_name_transactions.clear()
                common_name_transactions.append(transaction)
                current_name = transaction.name
        if len(common_name_transactions) > 0:
            self.process_group(common_name_transactions)

        return self.ans


if __name__ == '__main__':
    indata = \
        ['alex,119,16,toronto',
         'alex,175,1127,mexico',
         'alex,354,1328,luxembourg',
         'alex,406,776,istanbul',
         'alex,443,537,taipei',
         'alex,456,889,newdelhi',
         'alex,628,861,moscow',
         'alex,783,81,moscow',
         'alex,893,1976,shenzhen',
         'alex,924,223,milan',
         'bob,150,1634,singapore',
         'bob,263,1258,tokyo',
         'bob,337,593,chicago',
         'bob,402,922,montreal',
         'bob,436,530,warsaw',
         'bob,465,1080,taipei',
         'bob,478,928,barcelona',
         'bob,510,1923,madrid',
         'bob,568,1674,toronto',
         'bob,649,842,prague',
         'bob,65,1559,zurich',
         'bob,688,451,beijing',
         'bob,777,542,taipei',
         'bob,798,343,hongkong',
         'bob,836,1904,dubai',
         'bob,901,815,tokyo',
         'chalicefy,16,176,rome',
         'chalicefy,19,592,singapore',
         'chalicefy,212,1865,chicago',
         'chalicefy,283,399,zurich',
         'chalicefy,36,1984,paris',
         'chalicefy,415,22,montreal',
         'chalicefy,517,266,luxembourg',
         'chalicefy,548,363,barcelona',
         'chalicefy,671,583,singapore',
         'chalicefy,820,71,newdelhi',
         'chalicefy,867,1520,montreal',
         'chalicefy,95,1222,montreal',
         'iris,164,119,paris',
         'iris,176,268,milan',
         'iris,25,657,singapore',
         'iris,268,391,chicago',
         'iris,344,1452,bangkok',
         'iris,39,264,istanbul',
         'iris,406,433,bangkok',
         'iris,420,1818,zurich',
         'iris,45,904,beijing',
         'iris,643,1703,madrid',
         'iris,666,231,chicago',
         'iris,677,1451,milan',
         'iris,678,788,madrid',
         'iris,716,754,moscow',
         'iris,749,200,amsterdam',
         'iris,803,691,milan',
         'iris,825,484,madrid',
         'iris,928,1565,paris',
         'iris,951,930,dubai',
         'iris,967,1119,guangzhou',
         'lee,152,981,mexico',
         'lee,158,987,mexico',
         'lee,166,3,madrid',
         'lee,21,119,taipei',
         'lee,293,1102,istanbul',
         'lee,373,184,munich',
         'lee,432,520,dubai',
         'lee,558,727,paris',
         'lee,622,194,amsterdam',
         'lee,664,463,frankfurt',
         'lee,734,1915,prague',
         'lee,895,1876,taipei',
         'lee,991,1570,mexico',
         'maybe,140,222,amsterdam',
         'maybe,230,1434,barcelona',
         'maybe,231,1790,paris',
         'maybe,390,5,shanghai',
         'maybe,457,1802,montreal',
         'maybe,467,1178,munich',
         'maybe,481,1504,munich',
         'maybe,545,608,shanghai',
         'maybe,560,587,milan',
         'maybe,607,1953,tokyo',
         'maybe,636,558,milan',
         'maybe,668,572,mexico',
         'maybe,685,602,madrid',
         'maybe,75,1980,shanghai',
         'maybe,860,517,toronto',
         'maybe,874,36,hongkong',
         'xnova,201,1375,madrid',
         'xnova,293,24,newdelhi',
         'xnova,405,957,mexico',
         'xnova,443,1687,taipei',
         'xnova,535,270,munich',
         'xnova,560,825,prague',
         'xnova,589,837,budapest',
         'xnova,627,834,budapest',
         'xnova,640,513,jakarta',
         'xnova,704,274,newdelhi',
         'xnova,786,804,guangzhou',
         'xnova,836,153,jakarta',
         'xnova,852,330,barcelona']
    sol = Solution()
    print(sol.invalidTransactions(indata))
