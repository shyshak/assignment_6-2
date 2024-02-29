import csv, sys
from convertor.temperature import fahrenheit_to_celcius as far_to_cel, celcius_to_fahrenheit as cel_to_far
from convertor.distance import meters_to_feet, feet_to_meters


def create_celcius_report(li: list):
    with open('out/output_celcius.csv', 'w') as file:
        fieldnames = ['Date', 'Reading', 'UOM']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for m in li:
            temp = float(m['Reading'][:-2])
            uom = m['Reading'][-1]
            if uom == 'F':
                writer.writerow({'Date': m['Date'], 'Reading': far_to_cel(temp), 'UOM': 'C'})
            if uom == 'C':
                writer.writerow({'Date': m['Date'], 'Reading': temp, 'UOM': 'C'})


def create_fahrenheit_report(li: list):
    with open('out/output_fahrenheit.csv', 'w') as file:
        fieldnames = ['Date', 'Reading', 'UOM']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for m in li:
            temp = float(m['Reading'][:-2])
            uom = m['Reading'][-1]
            if uom == 'F':
                writer.writerow({'Date': m['Date'], 'Reading': temp, 'UOM': 'F'})
            if uom == 'C':
                writer.writerow({'Date': m['Date'], 'Reading': cel_to_far(temp), 'UOM': 'F'})


def create_meters_report(li: list):
    with open('out/output_meters.csv', 'w') as file:
        fieldnames = ['Date', 'Distance', 'UOM', 'Reading']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for m in li:
            if 'm' in m['Distance']:
                temp = float(m['Distance'][:-1])
                writer.writerow({'Date': m['Date'], 'Distance': temp,
                                 'UOM': 'm', 'Reading': m['Reading']})
            if 'ft' in m['Distance']:
                temp = float(m['Distance'][:-2])
                writer.writerow({'Date': m['Date'], 'Distance': feet_to_meters(temp),
                                 'UOM': 'm', 'Reading': m['Reading']})



def create_feet_report(li: list):
    with open('out/output_feet.csv', 'w') as file:
        fieldnames = ['Date', 'Distance', 'UOM', 'Reading']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for m in li:
            if 'm' in m['Distance']:
                temp = float(m['Distance'][:-1])
                writer.writerow({'Date': m['Date'], 'Distance': meters_to_feet(temp),
                                 'UOM': 'ft', 'Reading': m['Reading']})
            if 'ft' in m['Distance']:
                temp = float(m['Distance'][:-2])
                writer.writerow({'Date': m['Date'], 'Distance': temp,
                                 'UOM': 'ft', 'Reading': m['Reading']})


try:
    unit = sys.argv[1].lower()
    print(unit)
    with open('input.csv', 'r') as csvfile:
        measurements = csv.DictReader(csvfile)
        if unit == 'c':
            create_celcius_report(measurements)
        elif unit == 'f':
            create_fahrenheit_report(measurements)
        elif unit == 'm':
            create_meters_report(measurements)
        elif unit == 'ft':
            create_feet_report(measurements)
        else:
            print('The conversion is unknown')
except Exception:
    print("Something went wrong")
