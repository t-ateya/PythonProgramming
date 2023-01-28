"""
    We need to design and implement a class that will be used to represent a bank account.
    We want the following functionality and chacracters:
        - accounts are uniquely identified by an account number (assume it will just be passed in the initializer)
        - account holders have a first and last name
        - accounts have an associated preferred time zone offset (e.g. -7 for MST)
        - balances need to be zero or higher and should not be directly settable
        - but, deposits and withdrawals can be made (given sufficient funds)
            -if withdrawal is attempted that would result in negative funds, the transaction should be declined.
        - a monthly interest rate exists and is applicable to all accounts uniformly. There should be a method that can be called calculate the 
            interest on the current balance using the current interest rate, and add it to the balance.
        - each deposit and withdrawal must generate a confirmation number composed of:
            - the transaction type: D for deposit, and W for withdrawal, I for interest deposit, and X for declined (in which case the balance remains unaffected)
            - the account number
            - the time the transaction was made, using UTC
            -an incrementing number (that increments across all accounts and transactions)
            - for (extreme simplicity) assume that the transaction id starts at zero (or whatever number you choose) whenever the program starts.
            - the confirmation number should be returned from any of the transaction methods (deposit, withdraw, etc)
        - create a method that, given a confirmation number returns:
            - the account number, transaction code (D, W, etc), datetime(UTC format), date time (in whatever timezone is specified in the argument, but more human readable), the transaction ID
            - make it so it is a nicely structured object (so can use dotted notation to access these attributes)
            - I purposefully made it so the desired timezone is passed as an argument. Can you figure out why? (hint: does this method require any info from any instances?)


        For example, we may have an account with:
            . account number 140568
            - preferred time zone offset of -7(MST)
            - an existing balance of 100.00

        Suppose the last transaction ID in the system was 123, and a deposit is made for 50.00 on 2019-03-15T14:59:00 (UTC) on the account (or 2019-03-15T07:59:00
        in account's preferred time zone offset)
        The new balance should reflect 159.00 and the confirmation number returned should look something like this:
        D-140568-20190315145900-124
        We also want a method that given the confirmation number returns an object with attributes:
          -result.account_number->140568
          -result.transaction_code->D
          -result.transaction_id -> 124
          - result.time -> 2019-03-15 07:59:00 (MST)
          -result.time_utc -> 2019-03-15T14:59:00

        Furthermore, if current interest rate is 0.5%, and the account's balance is 100.00, then the result of calling the deposit_interest (or whatever name you choose )
        method, should result in a new transaction and a new balance of 1050.00. Calling this method should also return a confirmation number
        For simplicity, just use floats, but be aware that for these types of situations, you'll probably want to use Decimal objects instead of floasts.

        Hint:
            My approach will end up end up creating two classes: 1. TimeZone class used to store the time zone name and offset definition (in hours and minutes),
            and a main class called Account that will have the following public interface:
                - initializer with account number, first name, last name, optional preferred time zone, startiing balance (default to 0)
                - a first name property (read/write)
                - a last name property (read/write)
                

"""

#Project 1 Solution

import itertools
import numbers
from datetime import timedelta

class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes) -> None:
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty')
        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError ("Minute offset must be an integer")

        if offset_minutes > 50 or offset_minutes < -59:
            raise ValueError('Minutes offset must be between -59 and 59 (inclusive).')

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, microseconds=0):
            raise ValueError('Offset must be between -12:00 and +14:00')

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

        @property
        def offset(self):
            return self._offset

        @property
        def name(self):
            return self._name 
        
        def __equal__(self, other):
            return ( isinstance(other, TimeZone) and 
                self.name == other.name and 
                self._offset_minutes == other._offset_minutes and
                self._offset_hours == other._offset_hours ) 

        def __repr__(self):
            return (f"TimeZone(name='{self.name}', "
                    f"offset_hours={self._offset_hours},"
                    f"offset_minutes={self._offset_minutes}")


# from datetime import datetime
# dt = datetime.utcnow()


class TransactionID:
    def __init__(self, start_id) -> None:
        self._start_id = start_id

    def next(self):
        self._start_id += 1
        return self._start_id

class Account:
    #transaction_counter = TransactionID(100)
    transaction_counter = itertools.count(100)

    _interest_rate = 0.5
    _tansaction_codes = {
        'deposit': 'D',
        'withdraw' :'W',
        'interest' : 'I',
        'rejected' : 'X'
    }

    # def make_transaction_id(self):
    #     new_trans_id = Account.transaction_counter.next()
    #     return 
    
    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0) -> None:
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name

        if timezone is None:
            self._timezone = TimeZone('UTC', 0, 0)
        self._timezone = timezone
        self._balance = float(initial_balance)

    @property
    def balance(self):
        return self._balance
    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError("Time Zone must be a valid TimeZone object")
        self._timezone = value

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name 

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name(value, "First Name")
        
    @property
    def last_name(self):
        return self._last_name 

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('',value, "Last Name")

    def validate_and_set_name(self, attr_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty')
        setattr(self, attr_name, value)
    
    def generate_confirmation_code(self, account_number, transaction_id, transaction_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f"{transaction_code}-{account_number}-{dt_str}-{transaction_id}"

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be real number.')

        if value < 0:
            raise ValueError('interest rate cannot be negative')
        cls._interest_rate = value 

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        parts = confirmation_code.split('-')
        if len(parts) !=4:
            raise ValueError('Invalid confirmation code')
        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            raise ValueError('Invalid transaction datetime.') from ex
        
        if preferred_time_zone is None:
            preferred_time_zone = TimeZone('UTC', 0, 0)

        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError("Invalid TimeZone specified")

        dt_preferred = dt_utc + preferred_time_zone.offset

    def deposit(self, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Deposit value must be real number')
        if value <= 0:
            raise ValueError("Deposit value must be ")

        transaction_code = Account._tansaction_codes["deposit"]
        conf_code = self.generate_confirmation_code
        self._balance += value
        return conf_code

    def withdraw(self, value):

        accepted = False
        if self.balance - value < 0:
            transaction_code = Account._transaction_codes['rejected']
        else:
            accepted = True 
            transaction_code = Account._transaction_codes["withdraw"]
            self._balance -= value 

        conf_code = self.generate_confirmation_code(transaction_code) 

        if accepted:
            self._balance -= value

    def pay_intersect(self):
        interest = self.balance + Account.get_interest_rate() / 100 
        conf_code = self.generate_confirmation_code(Account._tansaction_codes['interest'])
        self._balance += interest 
        return conf_code


#Confirmation Codes
from datetime import datetime
def generate_confirmation_code(account_number, transaction_id, transaction_code):
    dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    return f"{transaction_code}-{account_number}-{dt_str}-{transaction_id}"



a1 = Account()
a2 = Account()

print(a1.make_transaction_id())
print(a2.make_transaction_id())
print(a1.make_transaction_id())

def transaction_ids(start_id):
    while True:
        start_id += 1
        yield start_id

t = transaction_ids(100)

# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))


try:
    a = Account(1234, None, None)
except ValueError as ex:
    print(ex)


    