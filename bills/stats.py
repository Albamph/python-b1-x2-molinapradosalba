# Write your imports here
from .item import Bill, Product
from .entity import Buyer


class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        # Write here your code
        counter = {}
        for bill in self.bills:
            for product in bill.products:
                counter[product] = counter.get(product, 0) + 1
        top_product = None
        top_count = 0
        for product, count in counter.items():
            if count > top_count:
                top_product = product
                top_count = count
        return (top_product, top_count)

    def find_top_two_sellers(self) -> list:
        # Write here your code
        sales = {}
        for bill in self.bills:
            sales[bill.seller] = (sales.get(bill.seller, 0)
                                  + bill.calculate_total())
        ordered = sorted(sales.items(), key=lambda item: item[1], reverse=True)
        return [seller for seller, total in ordered[:2]]

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
         purchases = {}
        for bill in self.bills:
            purchases[bill.buyer] = (purchases.get(bill.buyer, 0)
                                     + bill.calculate_total())
        lowest = min(purchases.items(), key=lambda item: item[1])
        return (lowest[0], round(lowest[1], 2))

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        taxes = {}
        for bill in self.bills:
            for product in bill.products:
                taxes[product] = (taxes.get(product, 0)
                                  + product.calculate_total_taxes())
        result = [(product, round(total, 2))
                  for product, total in taxes.items()]
        result.sort(key=lambda item: item[1],
                    reverse=(order_type == OrderType.DES))
        return result

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
