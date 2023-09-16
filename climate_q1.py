import matplotlib.pyplot as plt
import climate.db
        
years = []
co2 = []
temp = []

conn = climate.db.connect('climate.db')
cursor = conn.cursor()
cursor.execute("SELECT years, co2, temp FROM ClimateData")
for row in cursor.fetchall():
    years.append(row[0])
    co2.append(row[1])
    temp.append([2])
conn.close()
    
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
