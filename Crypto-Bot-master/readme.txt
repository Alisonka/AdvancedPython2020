Hello! This is CryptoBot.
Usage:
/crate crypto crypto_to=USD <-- get current rate of crypto in crypto_to(separated by comma)
/history crypto_code, time_from time_to, resolution, crypto_to <-- get history of crypto_code from time_from to time_to with given resolution, where resolution is either minute, hour or day
Example:
/crate RUB <-- current rate of RUB in USD(default)
/crate RUB EUR <-- current rate of RUB in EUR
/history ETH 2017.02.03 2017.03.03 day USD <-- history of rate of ETH in USD