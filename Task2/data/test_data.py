BASE_URL = "https://qa-internship.avito.com/"
ID_PATTERN = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
INVALID_ID = "123123"
NOEX_ID = "aa111111-aa1a-1a11-a111-a11a111111aa"
INVALID_SELLERID = 11111
INVALID_STR_SELLERID = "aaaaaa"


# DATA FOR CREATE -------------------------------------------
VALID_DATA_CREATE = {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 1500,
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
}
DATA_CREATE_WITHOUT_SELLERID = {
        "name": "Test Item",
        "price": 1500,
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
}
DATA_CREATE_WITHOUT_NAME = {
        "sellerID": 111121,
        "price": 1500,
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
}
DATA_CREATE_WITHOUT_PRICE = {
        "sellerID": 111121,
        "name": "Test Item",
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
}
DATA_CREATE_WITHOUT_STATISTICS = {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 1500
}
INVALID_SELLER_DATA_CREATE = [
    {
        "sellerID": 11111,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": 3
        }
    },
    {
        "sellerID": "aaaaaa",
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": 3
        }
    },
    {
        "sellerID": "",
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": 3
        }
    }
]
INVALID_PRICE_DATA_CREATE = [
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": -100,
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": "aaa",
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": "",
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": 3
        }
    }
]
INVALID_STATPARAMS_DATA_CREATE = [
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": -10,
            "viewCount": 15,
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": -15,
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": -3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": "aaa",
            "viewCount": 15,
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": "aaa",
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": "aaa"
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": "",
            "viewCount": 15,
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": "",
            "contacts": 3
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {
            "likes": 10,
            "viewCount": 15,
            "contacts": ""
        }
    },
    {
        "sellerID": 111121,
        "name": "Test Item",
        "price": 100,
        "statistics": {}
    }
]
INVALID_EXTRA_DATA_CREATE = {
    "sellerID": 111121,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    },
    "extra": 100
}

# DATA FOR GET ITEM -------------------------------------------
VALID_DATA_GET_ITEM = {
    "sellerID": 111122,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}

# DATA FOR GET ALL ITEMS OF SELLER ----------------------------
VALID_DATA_GET_ITEMS_EMPTY = {
    "sellerID": 111123,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
VALID_DATA_GET_ITEMS = {
    "sellerID": 111127,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
VALID_DATA_GET_ITEMS_1 = {
    "sellerID": 111124,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
VALID_DATA_GET_ITEMS_2 = {
    "sellerID": 111124,
    "name": "Test Item 2",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}
VALID_DATA_GET_ITEMS_3 = {
    "sellerID": 111124,
    "name": "Test Item 3",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}

# DATA FOR GET STATISTICS  ----------------------------------
VALID_DATA_GET_STATISTICS = {
    "sellerID": 111125,
    "name": "Test Item",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 15,
        "contacts": 3
    }
}

# DATA FOR DELETE -------------------------------------------
VALID_DATA_DELETE = {
        "sellerID": 111126,
        "name": "Test Item",
        "price": 1500,
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
}

# DATA FOR PUT -------------------------------------------
VALID_DATA_PUT = {
        "sellerID": 111126,
        "name": "Test Item",
        "price": 1500,
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
}