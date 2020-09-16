CORRECT_PARAMS = {
    "amount": "400",
    "currency": "USD",
    "type": "creditcard",
    "card": {
        "number": "1234567890124567",
        "expirationMonth": "2",
        "expirationYear": "2020",
        "cvv": "111"
    }
}

MISSING_AMOUNT = {
    "amount": "",
    "currency": "USD",
    "type": "creditcard",
    "card": {
        "number": "1234567890124567",
        "expirationMonth": "2",
        "expirationYear": "2020",
        "cvv": "111"
    }
}

MISSING_CURRENCY = {
    "amount": "400",
    "currency": "",
    "type": "creditcard",
    "card": {
        "number": "1234567890124567",
        "expirationMonth": "2",
        "expirationYear": "2020",
        "cvv": "111"
    }
}

MISSING_TYPE = {
    "amount": "400",
    "currency": "USD",
    "type": "",
    "card": {
        "number": "1234567890124567",
        "expirationMonth": "2",
        "expirationYear": "2020",
        "cvv": "111"
    }
}

INCORRECT_CARD_NUMBER = {
    "amount": "400",
    "currency": "USD",
    "type": "creditcard",
    "card": {
        "number": "1234567890124",
        "expirationMonth": "2",
        "expirationYear": "2020",
        "cvv": "111"
    }
}

MISSING_CARD_NUMBER = {
    "amount": "400",
    "currency": "USD",
    "type": "creditcard",
    "card": {
        "number": "",
        "expirationMonth": "2",
        "expirationYear": "2020",
        "cvv": "111"
    }
}

MISSING_EXP_MONTH = {
    "amount": "400",
    "currency": "USD",
    "type": "creditcard",
    "card": {
        "number": "1234567890124567",
        "expirationMonth": "",
        "expirationYear": "2020",
        "cvv": "111"
    }
}

MISSING_EXP_YEAR = {
    "amount": "400",
    "currency": "USD",
    "type": "creditcard",
    "card": {
        "number": "1234567890124567",
        "expirationMonth": "2",
        "expirationYear": "",
        "cvv": "111"
    }
}

MISSING_CVV = {
    "amount": "400",
    "currency": "USD",
    "type": "creditcard",
    "card": {
        "number": "1234567890124567",
        "expirationMonth": "2",
        "expirationYear": "2020",
        "cvv": ""
    }
}
