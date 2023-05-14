from utils.class_Operation import Operation
from utils.func import last_operations


data = last_operations()

def main():
    for i in range(len(data)):
        if i <= len(data):
            operation = Operation(data[i])
            print(f'Операция {i + 1}:\n')
            print(f'{operation.reformat_date()}')
            if "Перевод со счета на счет" in operation.reformat_date():
                print(f'{operation.ref_acc_num()} -> {operation.reformat_acc_number()}')
            else:
                print(f'{operation.reformat_card_number()} -> {operation.reformat_acc_number()}')
            print(f'{operation.transfer_amount()}\n')


if __name__ == '__main__':
    main()
