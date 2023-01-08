#print(f"NameError - {type( NameError)} - {issubclass(NameError, BaseException)}")
#try:
    #print("start code")
    #print(error)
    #print("no errors")
#except:
   #print("we have an error")
#print("after capsule")

class BuildingError(Exception):
    def __str__(self):
        return f"З цих матеріалів ми не можемо будувати будинок"
def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return " матеріалів достатньо"
    else:
        raise BuildingError(amount_of_material)
material=123
check_material(material, 300)