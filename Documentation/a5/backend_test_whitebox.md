# Whitebox testing for backend method

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
