# Runner script for all modules
from load_data import load_sensor_data
from house_info import HouseInfo
from datetime import datetime
from temperature_info import TemperatureData
from humidity_info import HumidityData
from particle_count_info import ParticleData
from energy_info import EnergyData
from statistics import mean


##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print('Sensor Data App')
##############################

# Module 1 code here:
data = load_sensor_data()
print(f'Loaded records: {len(data)}')

house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area('id', rec_area=test_area)
print(f'\nHouse sensor records for area {test_area} = {len(recs)}')

test_date = datetime.strptime('5/9/20', '%m/%d/%y')
recs = house_info.get_data_by_date('id', rec_date=test_date)
print(f"House sensor records for date {test_date.strftime('%m/%d/%y')} = "
      f'{len(recs)}')

# Module 2 code here:
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)
print(f'\nHouse Temperature sensor records for area {test_area}, = '
      f'{len(recs)}')
print(f"\tMaximum: {max(recs)}, Minimum {min(recs)}")

recs = temperature_data.get_data_by_date(rec_date=test_date)
print(f"\nHouse Temperature sensor records for date: "
      f"{test_date.strftime('%m/%d/%Y')} = {len(recs)} ")
print("\tMaximum: {max(recs)}, Minimum: {min(recs)} temperatures")

# Module 3 code here:
humidity_data = HumidityData(data)
recs = humidity_data.get_data_by_area(rec_area=test_area)
print(f'\nHouse Humidity sensor records for area {test_area}, = '
      f'{len(recs)}')
print(f"\tAverage Humidity: {mean(recs)}")

recs = humidity_data.get_data_by_date(rec_date=test_date)
print(f"\nHouse Humidity sensor records for date: "
      f"{test_date.strftime('%m/%d/%Y')} = {len(recs)} ")
print(f"\tAverage Humidity: {mean(recs)}")

# Module 4 code here:
particle_data = ParticleData(data)
recs = particle_data.get_data_by_area(rec_area=test_area)
print(f'\nHouse Particle sensor records for area {test_area}, = '
      f'{len(recs)}')
concentrations = particle_data.get_data_concentrations(data=recs)
print(f"\tGood Air Quality recs: {concentrations['good']}")
print(f"\tModerate Air Quality recs: {concentrations['moderate']}")
print(f"\tBad Air Quality recs: {concentrations['bad']}")

recs = particle_data.get_data_by_date(rec_date=test_date)
print(f"\nHouse Particle sensor records for date: "
      f"{test_date.strftime('%m/%d/%Y')} = {len(recs)} ")
concentrations = particle_data.get_data_concentrations(data=recs)
print(f"\tGood Air Quality recs: {concentrations['good']}")
print(f"\tModerate Air Quality recs: {concentrations['moderate']}")
print(f"\tBad Air Quality recs: {concentrations['bad']}")

# Module 5 code here:
energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area=test_area)
print(f"\nHouse Energy sensor records for area {test_area} = {len(recs)}")
total_energy = energy_data.calculate_energy_usage(data=recs)
print(f"\tEnergy Usage: {total_energy:2.2} Watts")

recs = energy_data.get_data_by_date(rec_date=test_date)
print(f"\nHouse Energy sensor records for date: "
      f"{test_date.strftime('%m/%d/%Y')} = {len(recs)} ")
total_energy = energy_data.calculate_energy_usage(data=recs)
print(f"\tEnergy Usage: {total_energy:2.2} Watts")
