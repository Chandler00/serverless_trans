import datetime


def purchase(message, context):

    # input example
    # {'TransactionType': 'PURCHASE'}
    # log the message
    print('Received message from step functions {message}'.format(message=message))

    # 2 response
    response = {'TransType': message['TransactionType']
                , 'Timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                , 'Message': 'lambda processing the purchase'}

    return response