'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal

MAX_ITEM_AMOUNT = 1e9
MAX_QUANTITY = 1e9
MAX_TOTAL = 1e9

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal('0')
    
    for item in order.items:
        if item.type == 'payment':
            if item.amount < MAX_ITEM_AMOUNT and item.amount > -MAX_ITEM_AMOUNT:
                net += Decimal(str(item.amount))
        elif item.type == 'product':
            if not (item.amount < MAX_ITEM_AMOUNT and item.amount > -MAX_ITEM_AMOUNT):
                return(f"{item.amount} exceeds the maximum price. Please try again with a value between {-MAX_ITEM_AMOUNT} and {MAX_ITEM_AMOUNT}")
            elif not (item.quantity < MAX_QUANTITY and item.quantity > -MAX_QUANTITY):
                return(f"{item.quantity} exceeds the maximum amount of items. Please try again with a value between {-MAX_QUANTITY} and {MAX_QUANTITY}")
            else:
                net -= Decimal(str(item.amount * item.quantity))
                if not (net < MAX_TOTAL and net > -MAX_TOTAL):
                    return(f"{item.total} exceeds the maximum total. Please try again with a a value between {-MAX_TOTAL} and {MAX_TOTAL}")
        else:
            return(f"Invalid item type: {item.type}")
    
    if net != 0:
        return(f"Order ID: {order.id} - Payment imbalance: ${Decimal(net).quantize(Decimal('1.00'))}")
    else:
        return(f"Order ID: {order.id} - Full payment received!")

print(validorder(Order(id="among", items=[Item('product', 'desc', 5, 5)])))
print(validorder(Order(id="among2", items=[Item('payment', 'decssss', 5, 5)])))