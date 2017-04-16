#!/usr/bin/python

import sys
import random
from pymongo import MongoClient

def main(id, strLength, db):
    # charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !@#$%^&*()_+-=,./<>?`~;:0123456789"
    text = ""

    for i in range(0, strLength):
        text += "A"

    db.BM_DATA.insert_one(
        {
            "seq" : id,
            "data" : text
        }
    )

    print("Done for ", strLength)

client = MongoClient()
db = client.BM
main(1, 50000, db)
main(2, 100000, db)
main(3, 200000, db)
main(4, 300000, db)
main(5, 400000, db)
main(6, 500000, db)
main(7, 600000, db)
main(8, 700000, db)
main(9, 800000, db)
main(10, 900000, db)
main(11, 1000000, db)
main(12, 1500000, db)
main(13, 2000000, db)
main(14, 2100000, db)
main(15, 2200000, db)
main(16, 2300000, db)
main(17, 2400000, db)
main(18, 2500000, db)
main(19, 2600000, db)
main(20, 2700000, db)
main(21, 2800000, db)
main(22, 2900000, db)
main(23, 3000000, db)
main(24, 3500000, db)
main(25, 4000000, db)
main(26, 4500000, db)
main(27, 5000000, db)
main(28, 5500000, db)
main(29, 6000000, db)
main(30, 6500000, db)
main(31, 7000000, db)
main(32, 7500000, db)
main(33, 8000000, db)
main(34, 8500000, db)
main(35, 9000000, db)
main(36, 9100000, db)
main(37, 9200000, db)
main(38, 9300000, db)
main(39, 9400000, db)
main(40, 9500000, db)
main(41, 9600000, db)
main(42, 9700000, db)
main(43, 9800000, db)
main(44, 9900000, db)
main(45, 10000000, db)
main(46, 11000000, db)
main(47, 12000000, db)
main(48, 13000000, db)
main(49, 14000000, db)
main(50, 15000000, db)
main(51, 16000000, db)
main(52, 16200000, db)
main(53, 16400000, db)
main(54, 16600000, db)
main(55, 16800000, db)

