from salesByMatch import sockMerchant

assert sockMerchant(1,[1,1,2,3,1,1]) == 2
assert sockMerchant(1,[1,1,2,3]) == 1
assert sockMerchant(1,[]) == 0
assert sockMerchant(1,[1,2,3]) == 0