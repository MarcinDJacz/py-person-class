class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(p["name"], p["age"]) for p in people]
    for person_id in range(len(new_list)):
        his_wife = people[person_id].get("wife")
        if his_wife is not None:
            for wife_id in new_list:
                if wife_id.name == his_wife:
                    new_list[person_id].wife = wife_id
        else:
            del (new_list[person_id].wife)

    for person_id in range(len(new_list)):
        her_husband = people[person_id].get("husband")
        if her_husband is not None:
            for husband_id in new_list:
                if husband_id.name == her_husband:
                    new_list[person_id].husband = husband_id
        else:
            del (new_list[person_id].husband)
    return new_list
