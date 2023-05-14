from utils.func import last_operations
from utils.class_Operation import Operation


def test_last_operations():
    assert last_operations() == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                                  'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
                                  'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
                                 {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
                                  'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
                                  'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
                                  'to': 'Счет 35158586384610753655'},
                                 {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
                                  'operationAmount': {'amount': '30153.72',
                                                      'currency': {'name': 'руб.', 'code': 'RUB'}},
                                  'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
                                  'to': 'Счет 43241152692663622869'},
                                 {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
                                  'operationAmount': {'amount': '62814.53',
                                                      'currency': {'name': 'руб.', 'code': 'RUB'}},
                                  'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
                                  'to': 'Счет 46765464282437878125'},
                                 {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
                                  'operationAmount': {'amount': '21344.35',
                                                      'currency': {'name': 'руб.', 'code': 'RUB'}},
                                  'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]


test_list = {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
             'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Открытие вклада', 'from': 'Visa Classic 2842878893689012',
             'to': 'Счет 90424923579946435907'}

test_instance = Operation(test_list)


def test_operations_list():
    assert test_instance.reformat_date() == '08.12.2019 Открытие вклада'
    assert test_instance.transfer_amount() == '41096.24 USD'
    assert test_instance.reformat_acc_number() == 'Счет **5907'
    assert test_instance.reformat_card_number() == 'Visa Classic 2842 87** **** 9012'
    assert test_instance.ref_acc_num() == 'Visa **9012'


test_list_1 = {'id': 863064926, 'state': 'EXECUTED', '3': '2019-12-08T22:46:21.935582',
               'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Открытие вклада', '1': 'Visa Classic 2842878893689012', '2': 'Счет 90424923579946435907'}
test_instance_1 = Operation(test_list_1)


def test_operation_list_1():
    assert test_instance_1.reformat_date() == ''
    assert test_instance_1.reformat_card_number() == ''
    assert test_instance_1.reformat_acc_number() == ''
    assert test_instance_1.ref_acc_num() == ''
    assert test_instance_1.id == test_list_1
