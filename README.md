# 🔧 Mechanic Recommendation System  
A **location-based recommendation system** that helps users find nearby mechanics using **K-Means clustering** and **geospatial data processing**. The system processes location data and suggests relevant mechanics based on clustering.

---

## 🚀 Features  
✔️ **Mechanic Search & Recommendation** based on user location.  
✔️ **K-Means Clustering** for grouping mechanics efficiently.  
✔️ **Interactive API** for fetching mechanic recommendations.  
✔️ **Fast Spatial Data Processing** with Pandas & NumPy.  
✔️ **Logging & Error Handling** for smooth performance.  

---

## 🛠 Tech Stack  

- **Backend:** Flask (Python)  
- **Machine Learning:** K-Means Clustering  
- **Data Processing:** Pandas, NumPy  
- **Model Storage:** Pickle  
- **Logging & Debugging:** Python Logging  
- **CORS Support:** Flask-CORS (Optional)  
- **Dataset:** Mechanic data (CSV)  

---

## 📊 Libraries Used  

| Library       | Purpose                                         |  
|--------------|-------------------------------------------------|  
| **Flask**     | API development & request handling            |  
| **Pickle**    | Loading the trained K-Means model             |  
| **Pandas**    | Reading and processing mechanic dataset       |  
| **NumPy**     | Handling numerical computations               |  
| **Logging**   | Debugging and error tracking                  |  
| **Flask-CORS** | Enables cross-origin requests (Optional)     |  

---

### 🔗 **How It Works?**  
1️⃣ **User sends location (latitude & longitude).**  
2️⃣ **K-Means model predicts the cluster** for the location.  
3️⃣ **Mechanics from the same cluster** are fetched from the dataset.  
4️⃣ **Recommendations are returned as JSON.**  



---

### 🎯 **Use Cases**  
✅ Finding the best **mechanics nearby**.  
✅ Efficient **location-based recommendations**.  
✅ Handles **large datasets** with clustering.  

---

🚀 **Ready to find the best mechanics in your area? Let's go!** 🔧🛠️
