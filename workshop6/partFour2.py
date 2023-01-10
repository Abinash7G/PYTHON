temperature= int (input('enter current temperature'))

if temperature >= 85 and humidity > 60:
    print("muggy day today")
else:
    if temperature >= 85:
        print("warm, but not muggy today")
    else:
        if temperature >= 65:
            print("pleasant today")
        else:
            if temperature <= 45:
                print("cold today")
            else:
                print("cool today")
