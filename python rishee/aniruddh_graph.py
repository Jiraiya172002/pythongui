import matplotlib.pyplot as plt
a=[10,14,25,19,25,15,19,12,19,9,17]
b=['markin','jessica','waltmut','redolf','rishee',"loren","lusica","markus","antonie","david","rex"]
plt.title("marks obtained by the students")
plt.xlabel("name of students")
plt.ylabel("Marks")
plt.plot(b,a, "b",linewidth="3", linestyle="dashdot", marker="d" , markeredgecolor="red",markersize="20")
plt.show()
