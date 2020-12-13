# Whitebox testing for backend method
## Data interface partitioning
For the whitebox testing of a backend method, we chose to test the `sell_ticket` function using
data interface coverage. Here are the input variables and the different partitions that will be
targeted by our testing.

| Input | Partition | Expected output |
|-|-|-|
| User |||
|| User object, exists in database | No error |
|| User object, doesn't exist in database | Internal Error: user does not exist in database |
|| non-User type (incl. None) | Internal Error: 'user' must be of type 'User' |
||||
| Name |||
|| str, non-duplicate | No error |
|| str, duplicate | Error: "A ticket with that name already exists." |
|| non-str type (incl. None) | Internal Error: 'name' must be of type 'str' |
||||
| Quantity |||
|| int | No error |
|| non-int type (incl. None) | Internal Error: 'quantity' must be of type 'int' |
||||
| Price |||
|| float with no fractional part | No error |
|| float with fractional part | No error |
|| non-float type (incl. None) | Internal Error: 'price' must be of type 'float' |
||||
| Expiry Date |||
|| date object | No error |
|| non-date type (incl. None) | Internal Error: 'expiryDate' must be of type 'date' |
||||

## Test enumeration
From the above partitions, the following tests were derived:
| Test partitions | Inputs | Expected output |
|-|-|
| All inputs valid, price with no fractional part | user=&lt;user in DB> name="Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | No error |
| All inputs valid, price with fractional part | user=&lt;user in DB> name="Unique" quantity=1 price=12.34 expiryDate=date(2030, 1, 1) | No error |
| User object that doesn't exist in database | user=&lt;user not in DB> name="Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: user does not exist in database |
| Non-User type user parameter | user=None name="Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: 'user' must be of type 'User' |
| Duplicate name | user=&lt;user in DB> name="Not Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Error: "A ticket with that name already exists." |
| Non-str type name parameter | user=&lt;user in DB> name=None quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: 'name' must be of type 'str' |
| Non-int type quantity parameter | user=&lt;user in DB> name="Unique" quantity=None price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: 'quantity' must be of type 'int' |
| Non-float type price parameter | user=&lt;user in DB> name="Unique" quantity=1 price=None expiryDate=date(2030, 1, 1) | Internal Error: 'price' must be of type 'float' |
| Non-date type expiryDate parameter | user=&lt;user in DB> name="Unique" quantity=1 price=10.00 expiryDate=None | Internal Error: 'expiryDate' must be of type 'date' |
