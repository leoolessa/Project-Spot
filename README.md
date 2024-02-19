**README - Project Spot: Choosing the Best Location**

You have recently established a new company in the gaming industry and are tasked with finding the ideal location for your offices. The company has a specific structure with employees in various roles, and you need to consider their preferences and requirements for the new office location. Here's a step-by-step guide on how the project was approached:

## Project Overview

The company has the following employee structure:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Analysts
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy who loves basketball
- 10 Executives
- 1 CEO/President

## Criteria and Preferences

1. **Designers:** Prefer locations near companies that conduct design talks and share knowledge.

2. **Parents:** 30% of the company staff have at least 1 child.

3. **Developers:** Prefer locations near successful tech startups that have raised at least 1 Million dollars.

4. **Executives:** Like Starbucks a lot; ensure there's a Starbucks nearby.

5. **Account Managers:** Need to travel a lot.

6. **Age Group:** Everyone in the company is between 25 and 40; consider places for social activities.

7. **CEO:** Is vegan.

8. **Maintenance Guy:** A basketball stadium must be around 10 Km.

9. **Office Dog ("Dobby"):** Needs a hairdresser every month.

## Approach

The project was divided into the following steps:

1. **Data Extraction:** Utilized the Google Maps API to extract data for various categories (bars, restaurants, schools, etc.) in three cities: Barcelona, London, and Silicon Valley.

2. **Data Analysis:** Created DataFrames for each category and city to analyze and filter the information.

3. **MongoDB Storage:** Exported the DataFrames to MongoDB for further analysis and storage.

4. **Map Visualization:** Created an interactive map using Folium, showcasing various categories and their proximity to potential office locations.

5. **Decision Making:** Chose Barcelona as the preferred city based on data analysis and visualization.

6. **Final Location:** Identified approximate locations within Barcelona, London and Silicon Valley that meet the specified criteria.

## Implementation

The provided code in the Jupyter Notebook covers the entire process, including data extraction, analysis, map creation, and decision-making. The resulting map is saved as `city_name_map.html`.

## How to Use

1. Execute the code in the Jupyter Notebook, providing the required input, including the Google Maps API token.

2. Analyze the map, considering the layers for different categories, and make an informed decision based on the company's criteria.

3. Review the exported MongoDB collections for further insights.

4. Refer to the generated HTML map (`city_name_map.html`) for a visual representation of the chosen location.

## Conclusion

Barcelona was selected as the most suitable city for the new company offices, considering the specified criteria. The final location within Barcelona provides a balanced mix of amenities and preferences for the diverse group of employees.

Feel free to adapt the code and criteria to explore other cities or refine the decision-making process based on your specific requirements.

[Click here to view the project presentation on Canva](https://www.canva.com/design/DAF8nXjfV00/jr7Y7O75Ts3WvyPVG2jbiw/edit)
