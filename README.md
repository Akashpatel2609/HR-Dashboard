# HR Dashboard

## 🚀 Project Overview  
The HR Dashboard delivers a 360° view of your human-resources data—combining high-level KPIs with granular employee records. Built with a synthetic dataset (Claude + Python Faker), it simulates real-world HR scenarios, including demographics, job details, compensation, performance ratings, and attrition.

---

## 📦 Resources  

| Resource                    | Description & Link                                                                                  |
|-----------------------------|-----------------------------------------------------------------------------------------------------|
| **Icons & Images**          | Sourced from [Flaticon](https://www.flaticon.com/); customized in [Photopea](https://www.photopea.com/). PSD files live in `icon/`. |
| **Mockups**                 | Initial sketches in Procreate; container wireframes in [draw.io](https://www.drawio.com/).           |
| **Tableau Project File**    | Included in this repo’s ZIP. Also on my [Tableau Public Profile](https://public.tableau.com/app/profile/akash.patel3574/vizzes). |

---

## 👤 User Story  
**As an HR manager**, I need a dashboard that combines:  
1. **Summary insights** for quick decision-making  
2. **Detailed employee records** for deep dives  

---

## 📊 Dashboard Sections  

### 1. Summary View  
**High-level KPIs & trends**  

| Section      | Key Visuals & Metrics                                                                 |
|--------------|----------------------------------------------------------------------------------------|
| **Overview** | - Total hired / active / terminated employees<br>- Hiring vs. termination trends over time<br>- Employee counts by department & job title<br>- HQ vs. branch headcount comparison<br>- Geographic distribution (city/state) |
| **Demographics** | - Gender ratio<br>- Age-group distribution<br>- Education-level distribution<br>- Education vs. performance correlation |
| **Income Analysis** | - Salary comparison by education level & gender<br>- Age vs. salary trends by department |

### 2. Employee Records View  
**Interactive data table**  
- Columns: Name, Department, Position, Gender, Age, Education, Salary  
- Search & filter on any column for rapid lookup  

---

## 🛠️ Implementation Highlights  

1. **Data Generation**  
   - Python Faker + Claude prompts → realistic HR dataset  
2. **Tableau Design**  
   - Clean, minimalist layout with intuitive filters  
3. **Interactivity**  
   - Global slicers (Department, Location, Date)  
   - Highlight actions & tooltips for context  
4. **Performance**  
   - Optimized extracts for fast load times  

---
