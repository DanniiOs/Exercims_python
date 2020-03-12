day = {
    1:  {"ord": "first", "item": "a Partridge in a Pear Tree."},
    2:  {"ord": "second", "item": "two Turtle Doves, and "},
    3:  {"ord": "third", "item": "three French Hens, "},
    4:  {"ord": "fourth", "item": "four Calling Birds, "},
    5:  {"ord": "fifth", "item": "five Gold Rings, "},
    6:  {"ord": "sixth", "item": "six Geese-a-Laying, "},
    7:  {"ord": "seventh", "item": "seven Swans-a-Swimming, "},
    8:  {"ord": "eighth", "item": "eight Maids-a-Milking, "},
    9:  {"ord": "ninth", "item": "nine Ladies Dancing, "},
    10: {"ord": "tenth", "item": "ten Lords-a-Leaping, "},
    11: {"ord": "eleventh", "item": "eleven Pipers Piping, "},
    12: {"ord": "twelfth", "item": "twelve Drummers Drumming, "}
}


def recite(start_verse, end_verse):
    return [
        f"On the {day[i]['ord']} day of Christmas my true love gave to me: " +
        ''.join(day[j]['item'] for j in range(i, 0, -1))
        for i in range(start_verse, end_verse+1)
    ]
