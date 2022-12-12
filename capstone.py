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
    
    #Normal plot Transportation emissions over time
    plt.plot(transport['Year'], transport['Value'])
    plt.title("Transportation Emissions From 1990 to 2020")
    plt.xlabel("Year")
    plt.ylabel("CO2 Equivalent (1,000,000 Metric Tonne)")
    plt.grid(True, 'major', 'y')
    plt.show()
    plt.clf()

    #Y-axis minimum at 0 Transportation emissions over time
    plt.plot(transport['Year'], transport['Value'])
    plt.title("Transportation Emissions From 1990 to 2020")
    plt.yticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])
    plt.xlabel("Year")
    plt.ylabel("CO2 Equivalent (1,000,000 Metric Tonne)")
    plt.grid(True, 'major', 'y')
    plt.show()
    plt.clf()

    #Emissions by transportation sector
    teSector = pd.read_csv("tEmissionsSectors.csv")
    plt.plot(teSector['Year'], teSector['Comm Air'], label="Comm Air")
    plt.plot(teSector['Year'], teSector['Freight Rail'], label="Freight/Rail")
    plt.plot(teSector['Year'], teSector['Passenger Total'], label="Passenger Total")
    plt.plot(teSector['Year'], teSector['Pipelines'], label="Pipelines")
    plt.plot(teSector['Year'], teSector['Ships Boats'], label="Ships/Boats")
    plt.plot(teSector['Year'], teSector['Trucking'], label="Trucking")
    #add all but passenger
    sumofall = teSector['Freight Rail'].add(teSector['Pipelines']).add(teSector['Ships Boats']).add(teSector['Trucking'])
    plt.plot(teSector['Year'], sumofall, label="Non-Passenger")
    plt.xlabel("Year")
    plt.ylabel("CO2 Equivalent (1,000,000 Metric Tonne)")
    plt.title("Emissions by Transportation Sector")
    plt.legend(loc='center right') #move this later https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot/43439132#43439132
    plt.yscale('log')
    plt.grid(True, 'both', 'y')
    plt.show()
    plt.clf()

    #Pie plot transportation sector 2019
    transportSectorPct = []
    transportSum = (teSector['Comm Air'].to_numpy()[12] + teSector['Freight Rail'].to_numpy()[12] + 
                    teSector['Passenger Total'].to_numpy()[12] + teSector['Pipelines'].to_numpy()[12] +
                    teSector['Ships Boats'].to_numpy()[12] + teSector['Trucking'].to_numpy()[12])
    transportSectorPct.append(teSector['Comm Air'].to_numpy()[12] / transportSum)
    transportSectorPct.append(teSector['Freight Rail'].to_numpy()[12] / transportSum)
    transportSectorPct.append(teSector['Passenger Total'].to_numpy()[12] / transportSum)
    transportSectorPct.append(teSector['Pipelines'].to_numpy()[12] / transportSum)
    transportSectorPct.append(teSector['Ships Boats'].to_numpy()[12] / transportSum)
    transportSectorPct.append(teSector['Trucking'].to_numpy()[12] / transportSum)
    #https://stackoverflow.com/questions/64411633/how-to-rotate-the-percentage-label-in-a-pie-chart-to-match-the-category-label-ro
    #For rotating pct labels thank you JohanC
    tsLabels = ["Comm Air", "Freight Rail", "Passenger Total", "Pipelines", "Ships Boats", "Trucking"]
    patches, labels, pct_texts = plt.pie(transportSectorPct, autopct="%1.1f%%", labels=tsLabels, rotatelabels=True, pctdistance=0.8)
    for label, pct_text in zip(labels, pct_texts):
        pct_text.set_rotation(label.get_rotation())
    plt.title("Percentage of Emissions by Transportation Sector in 2019")
    #plt.pie(transportSectorPct, labels=tsLabels, autopct="%1.1f%%")
    plt.legend()
    plt.show()

    #Miles driven on US Highways
    highwayMilesDriven = TransformData("Highway Travel")
    plt.plot(highwayMilesDriven['Year'], highwayMilesDriven['Value'])
    plt.xlabel("Year")
    plt.ylabel("Distance Traveled (Trillions of miles)")
    plt.title("Highway Travel in US")
    plt.grid(True, 'major', 'y')
    plt.show()
    plt.clf()
    
    #Miles driven on US Highways
    highwayMilesDriven = TransformData("Highway Travel")
    plt.plot(highwayMilesDriven['Year'], highwayMilesDriven['Value'])
    plt.xlabel("Year")
    plt.ylabel("Distance Traveled (Trillions of miles)")
    plt.title("Highway Travel in US")
    plt.show()
    plt.clf()
    
    #Miles of road and cost to maintain all that road nationally (US)
    roadMaintMiles = pd.read_csv("roadLengthMaintCost.csv")
    maintCost = pd.to_numeric(roadMaintMiles['Maintenance_US'])
    milesRoad = pd.to_numeric(roadMaintMiles['Miles of Road'])
    fig, ax = plt.subplots()
    ax.plot(roadMaintMiles['Year'], roadMaintMiles['Maintenance_US'], label="Maitenance Cost")
    secax = ax.twinx()
    secax.plot(roadMaintMiles['Year'], roadMaintMiles['Miles of Road'], color='red', label="Length of Road")
    ax.set_title("Maintenance Cost and Miles of Public Roads in US")
    ax.set_xlabel("Year")
    ax.set_ylabel("Maintenance Cost (Millions of Dollars)")
    secax.set_ylabel("Length of Road (mile)")
    ax.legend()
    secax.legend(bbox_to_anchor=(0.15, .95))
    ax.grid(True, 'major', 'y')
    plt.show()
    plt.clf()
    
    #Hybrid sales
    hybridSales = TransformData("Sales of Hybrids")
    hybridSales = pd.DataFrame.reset_index(hybridSales, drop=True)
    phev = hybridSales.loc[np.where(hybridSales['Statistic'] == "PHEV")[0]]
    phev = phev.sort_values(by='Year')
    hev = hybridSales.loc[np.where(hybridSales['Statistic'] == "HEV")[0]]
    hev = hev.sort_values(by='Year')
    bev = hybridSales.loc[np.where(hybridSales['Statistic'] == "BEV")[0]]
    bev = bev.sort_values(by='Year')
    plt.plot(phev['Year'], phev['Value'], label="PHEV")
    plt.plot(hev['Year'], hev['Value'], label="HEV")
    plt.plot(bev['Year'], bev['Value'], label="BEV")
    plt.legend()
    plt.title("Amount of Electric Vehicles Sold in US")
    plt.xlabel("Year")
    plt.ylabel("Vehicles Sold (thousands)")
    plt.show()

    

main()
