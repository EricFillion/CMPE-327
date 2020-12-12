# Whitebox testing for backend method

For the whitebox testing of a backend method, we chose to test the `sell_ticket` function using
data interface coverage. Here are the input variables and the different partitions that will be
targeted by our testing.

| Input | Partition | Expected output |
|-|-|-|
| User |||
|| User object, exists in database | No error |
|| User object, doesn't exist in database | Error, database is unable to create the foreign key relation|
|| None | Error, database is unable to create the foreign key relation|
||||
| Name |||
|| str, non-duplicate | No error |
|| str, duplicate | Error: "A ticket with that name already exists." |
|| None, non-duplicate | No error |
|| None, duplicate | Error: "A ticket with that name already exists." |
||||
| Quantity |||
|| int | No error |
|| None | No error |
||||
| Price |||
|| str | No error |
|| int | No error |
|| float, no fractional part | No error |
|| float with fractional part | No error |
|| None | No error |
||||
| Expiry Date |||
|| date object | No error |
|| str ("yyyymmdd") | Error, not date object |
|| str ("yyyy-mm-dd") | Error, not date object |
||||
