# DataSenseAI

DataSenseAI is a Streamlit-based application that leverages the **Google Gemini API** to provide intelligent insights and visualizations on user-uploaded datasets. The app allows users to upload CSV files, explore data summaries, generate AI-powered insights, and visualize data trends.

## **Features**

- **Upload Datasets**: Upload CSV files to analyze.
- **Data Summary**: Generate a quick summary of the dataset, including basic statistics.
- **AI Insights**: Use the Google Gemini API to provide intelligent insights and interpretations of the data.
- **Custom Visualizations**: Visualize data using Box Plots, Violin Plots, Bar Charts, and Scatter Plots.
- **Export Insights**: View and analyze insights directly in the app.

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mojmo/DataSenseAI.git
   cd DataSenseAI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Gemini API**:
   - Go to the [Google AI for Developers](https://ai.google.dev/gemini-api/docs).
   - Create a `.env` file in the root directory of the project and add your API key:
   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

   You can access the app at `http://localhost:8501` in your web browser.

## **Usage**

1. **Upload a Dataset**
   - Click the "Upload your dataset" button and select a CSV file.

2. **Explore Data**
   - The app will display a preview of the dataset.
   - Use the "Data Summary" section to get a quick overview of the data.
   - Use the "Full Dataset" section to view the entire dataset.

3. **Select Columns to Visualize**
   - Select the columns you want to visualize.
   - You can choose to visualize the data for a single column or two columns at once.

4. **Generate Insights**
   - Click the "Generate Insights" button to generate AI-powered insights.
   - The app will display the insights in the Insights section.

5. **Visualize Data**
   - Use the "Select X-axis (optional)" and "Select Y-axis" dropdowns to select the columns you want to visualize.
   - You can choose to visualize the data for a single column or two columns at once.
   - The app will display the visualization in the Insights section.
  
## **Demo**

You can try the app by uploading a CSV file and exploring the data. Here's a demo of the app in action:


https://github.com/user-attachments/assets/48685003-a42e-467e-9d76-5b24d221aff4



## **Screenshots**

![Screenshot 1](assets/screenshots/Screenshot%20(1).png)

![Screenshot 2](assets/screenshots/Screenshot%20(2).png)

![Screenshot 3](assets/screenshots/Screenshot%20(3).png)

![Screenshot 4](assets/screenshots/Screenshot%20(4).png)

![Screenshot 5](assets/screenshots/Screenshot%20(5).png)

![Screenshot 6](assets/screenshots/Screenshot%20(6).png)

![Screenshot 7](assets/screenshots/Screenshot%20(7).png)

![Screenshot 8](assets/screenshots/Screenshot%20(8).png)

![Screenshot 9](assets/screenshots/Screenshot%20(9).png)

![Screenshot 10](assets/screenshots/Screenshot%20(10).png)

## **Contributing**

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
