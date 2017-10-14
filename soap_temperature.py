import osa
import math


def soap_temperature(t):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(Temperature=t, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')


def soap_currency(from_currency, to_currency, amount):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum(fromCurrency=from_currency, toCurrency=to_currency, amount=amount,
                                       rounding=False)


def soap_distance(value):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(LengthValue=value, fromLengthUnit='Miles', toLengthUnit='Kilometers')


def average_temperature():
    temps_f = []
    av_temp_c = 0.0
    with open('temps.txt') as f:
        for line in f:
            temps_f.append(int(line.split()[0]))
    for t in temps_f:
        av_temp_c += t
    print(soap_temperature(av_temp_c)/len(temps_f))


def amount_trip():
    currencies = []
    amount = 0.0
    with open('currencies.txt') as f:
        for line in f:
            currencies.append(line.split())
    for currency in currencies:
        amount += soap_currency(currency[2], 'RUB', currency[1])
    print(math.ceil(amount))


def cost_travel():
    distance = 0.0
    travels = []
    with open('travel.txt') as f:
        for line in f:
            travels.append(line.split())
    for travel in travels:
        travel[1] = travel[1].replace(',', '')
        distance += float(travel[1])
    print('{:.2f}'.format(soap_distance(distance)))

average_temperature()
amount_trip()
cost_travel()

