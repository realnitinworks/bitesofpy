import pytest


from account import Account

# write your pytest functions below, they need to start with test_


@pytest.fixture(scope="function")
def create_account():
    def _create_account(owner, amount=0):
        return Account(owner=owner, amount=amount)
    return _create_account


@pytest.fixture(scope="module")
def acc():
    account = Account("Aeben", 100)
    transactions = [100, 20, 30, 40, -2, -10, 5, 7, 8]
    for amount in transactions:
        account.add_transaction(amount)
    return account


def test_account_representation(create_account):
    account = create_account("nitin", 100)
    assert str(account) == (
        f"Account of {account.owner} with starting amount: {account.amount}"
    )
    assert repr(account) == (
        "Account({!r}, {!r})".format(account.owner, account.amount)
    )


def test_account_creation(create_account):
    account = create_account("nitin", 100)
    assert account.owner == "nitin"
    assert account.amount == 100
    assert account.balance == 100

    account = Account("nitin")
    assert account.owner == "nitin"
    assert account.amount == 0
    assert account.balance == 0


def test_add_transaction(create_account):
    account = create_account("nitin", 50)
    account.add_transaction(50)
    account.add_transaction(-50)
    account.add_transaction(10)
    account.add_transaction(40)
    assert account.balance == 100


@pytest.mark.parametrize('amount', [
    112.4,
    "100",
    [100, -50, 200, 30]
])
def test_invalid_transaction_amount(create_account, amount):
    account = create_account("nitin", 50)
    with pytest.raises(ValueError) as exc:
        account.add_transaction(amount)

    assert str(exc.value) == "please use int for amount"


def test_num_transactions(create_account, acc):
    account = create_account("nitin", 50)
    assert len(account) == 0
    assert len(acc) == 9


def test_get_account_transaction(acc):
    assert acc[0] == 100
    assert acc[-1] == 8


def test_account_iterability(acc):
    assert iter(acc)


def test_account_equality(create_account):
    account1 = create_account("nitin")
    account2 = create_account("aeben")
    assert account1 == account2

    account1 = create_account("nitin", 10)
    account2 = create_account("aeben", 10)
    assert account1 == account2
    assert not account1 < account2

    account1 = create_account("nitin", 10)
    account2 = create_account("aeben", 20)
    assert account1 < account2


def test_account_addition(create_account):
    account1 = create_account("nitin", 10)
    account2 = create_account("aeben", 20)
    account1.add_transaction(10)
    account1.add_transaction(20)
    account2.add_transaction(100)
    account2.add_transaction(-10)
    account = account1 + account2

    assert account.owner == "nitin&aeben"
    assert account.balance == 150
    assert list(account) == [10, 20, 100, -10]
