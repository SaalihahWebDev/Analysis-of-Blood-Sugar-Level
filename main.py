#Step-1-Importing
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Step 2-Data
labels=['Male',"Female","Children","Adults","Elderly"]
sugar_levels=[120,100,90,110,150]

#Step 3-Converting Dataframe to seaborn
data=pd.DataFrame({
    "Gender":labels,
    "BloodSugar":sugar_levels
})

#Step 4-Create side by side plots
fig,axes=plt.subplots(1,2,figsize=(10,5))
axes[0].pie(sugar_levels,labels=labels,autopct='%2.2f%%',startangle=90)
axes[0].set_title("Pie Chart:Blood Sugar")
sns.barplot(x="Gender",y="BloodSugar",data=data,ax=axes[1])
axes[1].set_title("Bar Chart:Blood Sugar")
axes[0].set_ylabel("Sugar level")
plt.tight_layout()
plt.show()