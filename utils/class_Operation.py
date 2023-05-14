from datetime import datetime
import re


class Operation:
    """
    Класс "Операция". Имеет атрибут "id". По умолчанию присваивается пустой список.
    """

    def __init__(self, id=[]):
        self.id = id

    def __repr__(self):
        return f'{self.id}'

    def reformat_date(self):
        """
        Возвращает читаемый для пользователя вид даты 01.01.2023 + назначение перевода
        """
        try:
            ref_date = datetime.strptime(self.id['date'], "%Y-%m-%dT%H:%M:%S.%f")
            ref_date = ref_date.strftime('%d.%m.%Y')
            destination = self.id['description']
            return f'{ref_date} {destination}'
        except KeyError:
            return ""

    def reformat_card_number(self):
        """
        Возвращает вид карты(~Visa) 1234 56** **** 7890
        """
        try:
            full_card_num = self.id['from']
            full_card_num = full_card_num.split(' ')
            reformat_num = re.findall(r'\d\d\d\d', full_card_num[-1])
            reformat_num = " ".join(reformat_num)
            reformat_num = reformat_num.replace(reformat_num[7:-5], "** ****")
            del full_card_num[-1]
            card_num = ' '.join(full_card_num)
            return f"{card_num} {reformat_num}"
        except KeyError:
            return ""

    def reformat_acc_number(self):
        """
        Возвращает строку в виде "Счет **1234"
        """
        try:
            ref_acc_num = self.id['to']
            ref_acc_num = ref_acc_num.replace(ref_acc_num[5:-4], "**")
            return ref_acc_num
        except KeyError:
            return ""

    def ref_acc_num(self):
        """
        Возвращает строку в виде "Счет **1234" если идет перевод со счета на счет.
        """
        try:
            ref_acc_num = self.id['from']
            ref_acc_num = ref_acc_num.replace(ref_acc_num[5:-4], "**")
            return ref_acc_num
        except KeyError:
            return ""

    def transfer_amount(self):
        """
        Возвращает сумму перевода в виде "1234.12 руб.(USD)"
        """
        amount = self.id['operationAmount']['amount']
        return f"{amount} {self.id['operationAmount']['currency']['name']}"
