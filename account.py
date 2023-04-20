class Account:
    def __init__(self, name: str) -> None:
        """
        Create an account object with the given name and balance set to 0.

        Args:
            name: The name of the account holder.
        """
        self.__account_name: str = name
        self.__account_balance: float = 0.0

    def deposit(self, amount: float) -> bool:
        """
        Add the specified amount to the account balance.

        Args:
            amount: The amount to be deposited.

        Returns:
            A boolean value indicating if the transaction was successful or not.
        """
        if amount <= 0:
            return False
        self.__account_balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        Deduct the specified amount from the account balance.

        Args:
            amount: The amount to be withdrawn.

        Returns:
            A boolean value indicating if the transaction was successful or not.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def get_balance(self) -> float:
        """
        Return the account balance.

        Returns:
            The account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Return the name of the account holder.

        Returns:
            The name of the account holder.
        """
        return self.__account_name
