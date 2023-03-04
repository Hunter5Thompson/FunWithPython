# Nesting a Dictionary in a Dictionary

travel_log_v1 = {
    "Europe": {
        "countries_visited": ["Spain", "France", "Belgium", "Czech Republic", "Slovakia", "Austria", "Italy", "England",
                              "Slowenia", "Portugal", "Greece", "Cyprus"]
        , "total_visits": 24},
    "Asia": {"countries_visited": ["Dubai", "Oman", "Thailand", "Malaysia"], "total_visits": 5},
    "Africa": {"countries_visited": ["Tunesia"], "total_visits": 1},

}

# Nesting a Dictionary in a List

travel_log_v2 = [

    {
        "destinations": "Europe",
        "country": ["Spain", "France", "Belgium", "Czech Republic", "Slovakia", "Austria", "Italy",
                    "England", "Slovenia", "Portugal", "Greece", "Cyprus"],
        "total_visits": 24
    },
    {"destinations": "Asia",
     "country": ["Dubai", "Oman", "Thailand", "Malaysia"],
     "total_visits": 5
     },
    {"destinations": "Africa",
     "country": ["Tunisia"],
     "total_visits": 1
     }
]


def add_country_visit(destination, country, total_visits):
    new_destination = {"destinations": destination, "country": country, "total_visits": total_visits}
    travel_log_v2.append(new_destination)


add_country_visit("America", ["Canada"], 1)
print(travel_log_v2)
