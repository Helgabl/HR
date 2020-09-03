

nafn = str(input("sláðu inn nafnið þitt"))
þyngd = int(input("sláðu inn þyngd þína"))

if þyngd <= 60:
    print(nafn, " þú ert í lightweight")
elif þyngd <= 90:
    print(nafn, "þú ert í middleweight")
else:
    print(nafn, "þú ert í heavyweight")