import matplotlib.pyplot as plt

y = ["1982-1987", "1987-1992", "1992-1997", "1997-2002", "2002-2007","2007-2012"]
acres = [1200, 1450, 2300, 1750, 1250, 750]
plt.bar(y[0],acres[0], color = "green")
plt.bar(y[1],acres[1], color = "maroon")
plt.bar(y[2],acres[2], color = "red")
plt.bar(y[3],acres[3], color = "orange")
plt.bar(y[4],acres[4], color = "blue")
plt.xlabel("Year")
plt.ylabel("Amount of land in acres")
plt.title("Amount of Sprawl increase")
plt.show()

years = ["1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995"
         ,"1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009"
         ,"2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]

unhealthy = [54,37,52,43,54,52,63,63,57,51,59,45,41,45,47,32,22,27,51,48,53,57,67,49,39,30,46,
             43,15,36,35,25,26,36,19,38,18,28,44,26]

healthy = [8,11,5,10,7,6,9,10,17,16,22,29,22,43,42,33,54,17,27,20,34,41,29,57,64,45,31,34,32,
           17,33,22,23,26,32,38,35,66,60,41]

plt.figure(figsize=(10,10))
plt.plot(years,unhealthy, color = "red", marker = "s")
plt.plot(years, healthy, color = "green", marker = "o")
plt.xlabel("Year")
plt.xticks(fontsize = 4)
plt.ylabel("# of Days")
plt.title("Air quality in Los Angeles")
label = ["unhealthy", "healthy"]
plt.legend(label)
plt.show()


y1 = ["2014","2015","2016","2017","2018","2019","2020"]
delay = [18,18,18,18,18,18,12]
plt.plot(y1,delay, color = "gold")
plt.xlabel("Year")
plt.ylabel("Hours")
plt.title("Average amount of delay for commuter")
plt.show()

yd = [2257,2254,2250,2247,2230,2210,1451]
plt.plot(y1,yd, color = "purple", marker = "*")
plt.xlabel("Year")
plt.ylabel("Hours")
plt.title("Total amount of delay for commuters")
plt.show()


causes = ["Killing of Animals", "Habitat Degradation", "Habitat Loss", "Climate Change","Other"]
per = [37,31,13,7,12]
plt.pie(per, labels = causes, autopct='%1.2f%%')
plt.title("Causes of Decline in Wildlife")
plt.show()