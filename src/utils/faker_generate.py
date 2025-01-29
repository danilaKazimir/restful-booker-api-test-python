from faker import Faker


class FakerGenerate:
    fake = Faker()

    @staticmethod
    def generate_first_name() -> str:
        return FakerGenerate.fake.first_name()

    @staticmethod
    def generate_last_name() -> str:
        return FakerGenerate.fake.last_name()

    @staticmethod
    def generate_total_price() -> int:
        return FakerGenerate.fake.random_int(500, 1000)

    @staticmethod
    def generate_is_deposit_paid() -> bool:
        return FakerGenerate.fake.boolean()

    @staticmethod
    def generate_date(start_date, end_date) -> str:
        date = FakerGenerate.fake.date_between(start_date, end_date)
        return date.strftime('%Y-%m-%d')

    @staticmethod
    def generate_additional_needs() -> str:
        additional_needs_options = ["Breakfast", "Lunch", "Dinner", "Airport Transfer", "Extra Bed", "Late Checkout"]
        return FakerGenerate.fake.random_element(additional_needs_options)
