import statistics as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def TransformData(shortName):
    print("Transforming", shortName)
    data = pd.DataFrame(pd.read_csv("pgtt.csv"))
    #Gather all rows with shortName instance
    relevantRows = np.where(data['Statistic Short Name'] == shortName)[0]
    relevantRows = data.loc[relevantRows]
    values = relevantRows['Value']
    values = pd.DataFrame.reset_index(values, drop=True)
    #remove all commas from values
    values.replace(',', '', regex=True, inplace=True)
    values = pd.to_numeric(values)

    years = relevantRows['Year']
    years = pd.DataFrame.reset_index(years, drop=True)
    units = relevantRows['Units']
    units = pd.DataFrame.reset_index(units, drop=True)
    statistic = relevantRows['Statistic']
    statistic = pd.DataFrame.reset_index(statistic, drop=True)
    #format rows
    formattedData = pd.merge(statistic, years, right_index=True, left_index=True)
    formattedData = pd.merge(formattedData, values, right_index=True, left_index=True)
    formattedData = pd.merge(formattedData, units, right_index=True, left_index=True)
    
    return formattedData

def main():
    data = TransformData("Greenhouse Gas Emissions")
    data = pd.DataFrame.reset_index(data, drop=True)
    transport = data.loc[np.where(data['Statistic'] == "Transportation")[0]]
    transport = transport.sort_values(by='Year')
    
    # #Normal plot Transportation emissions over time
    # plt.plot(transport['Year'], transport['Value'])
    # plt.title("Transportation Emissions From 1992 to 2020")
    # plt.xlabel("Year")
    # plt.ylabel("CO2 Equivalent (1,000,000 Metric Tonne)")
    # plt.show()
    # plt.clf()

    # #Y-axis minimum at 0 Transportation emissions over time
    # plt.plot(transport['Year'], transport['Value'])
    # plt.title("Transportation Emissions From 1992 to 2020")
    # plt.yticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])
    # plt.xlabel("Year")
    # plt.ylabel("CO2 Equivalent (1,000,000 Metric Tonne)")
    # plt.show()

    # #Emissions by transportation sector
    # teSector = pd.read_csv("tEmissionsSectors.csv")
    # plt.plot(teSector['Year'], teSector['Comm Air'], label="Comm Air")
    # plt.plot(teSector['Year'], teSector['Freight Rail'], label="Freight/Rail")
    # plt.plot(teSector['Year'], teSector['Passenger Total'], label="Passenger Total")
    # plt.plot(teSector['Year'], teSector['Pipelines'], label="Pipelines")
    # plt.plot(teSector['Year'], teSector['Ships Boats'], label="Ships/Boats")
    # plt.plot(teSector['Year'], teSector['Trucking'], label="Trucking")
    # plt.legend(loc='upper right') #move this later https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot/43439132#43439132
    # plt.yscale('log')
    # plt.show()

    #Miles driven on US Highways
    highwayMilesDriven = TransformData("Highway Travel")
    plt.plot(highwayMilesDriven['Year'], highwayMilesDriven['Value'])
    plt.xlabel("Year")
    plt.ylabel("Distance Traveled (Trillions of miles)")
    plt.title("Highway Travel in US")
    plt.show()

main()