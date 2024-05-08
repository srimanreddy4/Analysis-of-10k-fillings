import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Your existing visualization code
st.set_option('deprecation.showPyplotGlobalUse', False)


companies=['Apple','Amazon']

selected_company = st.selectbox('Select a company', [''] + companies)

if selected_company=="" :
    st.write("Currently analysis is done for Apple company only, it wil soon updated for Amazon too")

if selected_company=='Apple' :




# Add a new section for Insights
    st.title("Insights into Apple Inc. Financial Data")

    # Revenue Recognition
    st.subheader("Revenue Recognition")
    st.write("""
    **Insight:**
    - Apple's revenue recognition policy has consistently been a critical factor in its financial results. The introduction of new products, such as iPhones, iPads, and Services, has had a significant impact on revenue recognition.
    - With each new product release, Apple identifies performance obligations and recognizes revenue accordingly. For example, with the launch of new iPhone models every year, iPhone net sales have consistently contributed a significant portion of Apple's overall net sales growth.
    - A shift in product mix, such as the increased focus on Services in recent years, has also played a role in revenue recognition. Services revenue, including Apple Music, Apple Pay, and App Store sales, has been growing and now accounts for a notable portion of Apple's total revenue.

    **Why this insight is valuable:**
    This insight is crucial for investors and analysts as it provides an understanding of Apple's revenue recognition policies and how they affect the company's financial performance, especially with the introduction of new products and services.
    """)

    # Revenue breakdown by category (e.g., iPhone, iPad, Services)
    revenue_data = pd.DataFrame({
        'Year': ['2018', '2019', '2020', '2021', '2022'],
        'iPhone': [165597, 142719, 137781, 192835, 205507],
        'iPad': [18809, 21280, 23724, 31862, 29615],
        'Services': [39516, 46294, 53768, 68425, 78131]
    })

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=pd.melt(revenue_data, id_vars=['Year'], value_vars=['iPhone', 'iPad', 'Services']), x='Year', y='value', hue='variable')
    plt.title('Revenue Breakdown by Category')
    plt.xlabel('Year')
    plt.ylabel('Revenue ($ million)')
    st.pyplot()
    # Warranty Costs
    st.subheader("Warranty Costs")
    st.write("""
    **Insight:**
    - Apple's limited warranty policies and associated costs have remained relatively stable over the years.
    - The company's focus on product quality and reliability has likely contributed to manageable warranty costs. However, the introduction of new products, such as the M2-powered MacBook Air and MacBook Pro, could influence these costs due to potential variations in reliability and repair expenses.
    - Efficient management of warranty costs is vital to maintaining profitability, especially as Apple continues to expand its product offerings and global reach.

    **Why this insight is valuable:**
    Understanding warranty costs is essential for assessing Apple's product quality, reliability, and overall profitability. Tracking warranty costs over time and visualizing them alongside product launches could provide valuable insights into their impact on the company's financials.
    """)

    # Warranty costs over time
    warranty_data = pd.DataFrame({
        'Year': ['2018', '2019', '2020', '2021', '2022'],
        'Warranty Costs': [4916, 5235, 5726, 6097, 6832]
    })

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=warranty_data, x='Year', y='Warranty Costs')
    plt.title('Warranty Costs Over Time')
    plt.xlabel('Year')
    plt.ylabel('Warranty Costs ($ million)')
    st.pyplot()

    # Inventory Valuation
    st.subheader("Inventory Valuation")
    st.write("""
    **Insight:**
    - Effective inventory management and valuation have always been crucial for Apple, given the dynamic nature of its product portfolio.
    - Apple regularly introduces new products and discontinues older ones, making inventory valuation a complex task. Proper valuation ensures the accurate reflection of product values in financial statements.
    - In recent years, with the introduction of new iPhone models and other product updates, effective inventory management has been essential to maintaining healthy gross margins. Fluctuations in product demand, especially during the COVID-19 pandemic, further emphasize the importance of accurate inventory valuation.

    **Why this insight is valuable:**
    Accurate inventory valuation is critical for Apple's financial reporting and profitability, especially with frequent product launches and discontinuations. Visualizing inventory levels, turnover ratios, and their impact on gross margins could provide valuable insights for investors and analysts.
    """)

    # Inventory levels and turnover ratio
    # Inventory levels and turnover ratio
    inventory_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Inventory': [3956, 4106, 4994, 6307, 7579],
        'Cost of Sales': [163756, 161701, 169558, 193282, 212243],
        'Turnover Ratio': [41.3, 39.4, 33.9, 30.6, 28.0]
    })

    plt.figure(figsize=(10, 6))

    # Inventory Levels
    ax1 = plt.subplot(1, 3, 1)
    sns.lineplot(data=inventory_data, x='Year', y='Inventory')
    ax1.set_title('Inventory Levels')
    ax1.set_ylabel('Inventory ($ million)')

    # Cost of Sales
    ax2 = plt.subplot(1, 3, 2)
    sns.lineplot(data=inventory_data, x='Year', y='Cost of Sales')
    ax2.set_title('Cost of Sales')
    ax2.set_ylabel('Cost of Sales ($ million)')

    # Turnover Ratio
    ax3 = plt.subplot(1, 3, 3)
    sns.lineplot(data=inventory_data, x='Year', y='Turnover Ratio')
    ax3.set_title('Turnover Ratio')
    ax3.set_ylabel('Turnover Ratio')

    plt.tight_layout()
    st.pyplot()













    # Streamlit app
    st.title("Apple Inc. Financial Data Visualizations based on information generated")

    # Net Sales Over Time
    st.subheader("Net Sales Over Time")
    # Your code for net sales over time visualization
    plt.figure(figsize=(10, 6))
    net_sales = [32.48, 36.54, 39.33, 108.25]
    years = ['2008', '2009', '2010', '2011']

    # Creating a DataFrame
    df = pd.DataFrame({'Net Sales': net_sales}, index=years)

    # Plotting net sales over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, marker='o')
    plt.title('Net Sales Over Time')
    plt.ylabel('Net Sales ($ billion)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    st.pyplot()
    # After rendering the plot using st.pyplot()
    st.write("This line plot shows the net sales of Apple Inc. over the years 2008 to 2011. It demonstrates a significant increase in net sales from 2008 to 2011, with the highest net sales in 2011.")
    # Operating Segments Net Sales
    st.subheader("Operating Segments Net Sales")
    # Your code for operating segments net sales visualization
    americas_net_sales = [16.552, 18.981, 24.498]
    europe_net_sales = [9.233, 11.810, 18.692]
    japan_net_sales = [1.728, 2.279, 3.981]
    years=['2009','2010','2011']
    # Creating a DataFrame
    operating_segments = pd.DataFrame({
        'Americas': americas_net_sales,
        'Europe': europe_net_sales,
        'Japan': japan_net_sales
    }, index=years)

    # Plotting operating segments net sales
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=operating_segments, marker='o')
    plt.title('Operating Segments Net Sales')
    plt.ylabel('Net Sales ($ billion)')
    plt.xticks(rotation=45)
    plt.legend(title='Operating Segments')
    plt.grid(True)
    plt.show()
    st.pyplot()
    st.write("This line plot compares the net sales of three operating segments: Americas, Europe, and Japan. The Americas segment consistently had the highest net sales, followed by Europe and Japan. All segments showed an increasing trend in net sales over time.")


    # Operating Expenses Over Time
    st.subheader("Operating Expenses Over Time")
    # Your code for operating expenses over time visualization
    research_development = [1109, 1333, 1782]
    sg_a = [3761, 4149, 5517]

    # Creating a DataFrame
    operating_expenses = pd.DataFrame({
        'Research & Development': research_development,
        'Selling, General & Administrative': sg_a
    }, index=years)

    # Plotting operating expenses over time
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=operating_expenses, marker='o')
    plt.title('Operating Expenses Over Time')
    plt.ylabel('Operating Expenses ($ million)')
    plt.xticks(rotation=45)
    plt.legend(title='Operating Expenses')
    plt.grid(True)
    plt.show()
    st.pyplot()
    st.write("This line plot compares the operating expenses for research and development (R&D) and selling, general, and administrative (SG&A) expenses over time. Both R&D and SG&A expenses increased steadily from 2008 to 2010, indicating rising costs associated with these activities.")
    st.subheader("Net sales by operating systems")

    import matplotlib.pyplot as plt
    import pandas as pd

    # Sample data
    net_sales_data = {
        'Year': ['2013', '2012', '2011'],
        'Americas': [65232, 62739, 57512],
        'Europe': [40929, 37883, 36323],
        'Greater China': [29846, 25417, 22533],
        'Japan': [14982, 13462, 10571],
        'Rest of Asia Pacific': [10344, 11181, 10741],
        'Retail': [21462, 20228, 18828]
    }

    net_sales_df = pd.DataFrame(net_sales_data)

    # Net Sales by Operating Segment bar chart
    net_sales_df.plot(kind='bar', x='Year', y=['Americas', 'Europe', 'Greater China', 'Japan', 'Rest of Asia Pacific', 'Retail'], figsize=(10, 6))
    plt.xlabel('Year')
    plt.ylabel('Net Sales ($ millions)')
    plt.title('Net Sales by Operating Segment')
    plt.show()

    st.pyplot()
    st.write("bar chart that compares net sales by operating segment (Americas, Europe, Greater China, Japan, Rest of Asia Pacific, Retail) for 2013, 2012, and 2011")
    st.subheader("Salels by product")

    net_sales_and_unit_sales_data = {
        'Year': ['2013', '2012', '2011'],
        'iPhone': [101991, 91279, 78692],
        'iPad': [30283, 31980, 30945],
        'Mac': [24079, 21483, 23221],
        'iPod': [2286, 4411, 5615],
        'Other': [18063, 16051, 12890]
    }

    net_sales_and_unit_sales_df = pd.DataFrame(net_sales_and_unit_sales_data)

    # Net Sales and Unit Sales by Product grouped bar chart
    net_sales_and_unit_sales_df.plot(kind='bar', x='Year', y=['iPhone', 'iPad', 'Mac', 'iPod', 'Other'], figsize=(10, 6))
    plt.xlabel('Year')
    plt.ylabel('Net Sales and Unit Sales')
    plt.title('Net Sales and Unit Sales by Product')
    plt.show()

    st.pyplot()
    st.write("grouped bar chart that compares net sales and unit sales for iPhone, iPad, Mac, iPod, and Other products for 2013, 2012, and 2011.")



    st.title("Summary of Analysis Provided")

    # Executive Overview
    st.subheader("Executive Overview")
    st.write("""
    - Apple designs, manufactures, and markets a diverse range of products, including iPhones, iPads, Macs, Apple Watches, AirPods, Apple TVs, HomePods, and related software, services, peripherals, and networking solutions.
    - The company's primary focus is on delivering exceptional user experiences by seamlessly integrating hardware, software, and services.
    """)

    # Financial Performance and Sales Analysis
    st.subheader("Financial Performance and Sales Analysis")
    st.write("""
    - Apple's net sales exhibited consistent growth over the years, increasing from $32.48 billion in 2008 to $229.2 billion in fiscal year 2017, driven by strong demand for iPhones, Services, and Macs.
    - The iPhone remained the top-selling product, contributing $141.3 billion (62%) to net sales in 2017, although it saw a slight decrease of 12% compared to the previous year.
    - Services emerged as a significant growth driver, with net sales increasing by 23% in 2017 to $29.9 billion, primarily due to higher App Store and licensing sales.
    - Mac net sales grew by 14% to $25.9 billion, driven by robust demand for Mac portables.
    - The Americas remained the largest operating segment, contributing $96.6 billion (42%) to net sales in 2017, followed by Europe ($55.0 billion) and Greater China ($44.8 billion).
    - Greater China experienced an 8% decline in net sales due to lower iPhone sales and unfavorable currency impacts.
    """)

    # Gross Margin and Operating Expenses
    st.subheader("Gross Margin and Operating Expenses")
    st.write("""
    - Apple's gross margin percentage slightly decreased to 38.5% in 2017, primarily due to higher product costs and unfavorable currency impacts.
    - Research and Development (R&D) expenses increased by 15% in 2017 to $11.6 billion, driven by higher headcount and expanded R&D activities.
    - Selling, General, and Administrative (SG&A) expenses grew by 8% to $15.3 billion, influenced by higher headcount-related expenses, variable selling expenses, and infrastructure costs.
    - Total operating expenses rose by 11% in 2017 to $26.8 billion.
    """)

    # Other Financial Highlights
    st.subheader("Other Financial Highlights")
    st.write("""
    - Apple's cash, cash equivalents, and marketable securities reached $268.9 billion in 2017, reflecting a significant increase over the years.
    - The company had total term debt of $103.7 billion as of September 30, 2017, with future principal payments expected over the next few years.
    - Apple returned $115.5 billion to shareholders through dividends and share repurchases under its capital return program from August 2012 through September 30, 2017.
    - As of September 30, 2017, Apple had total contractual obligations of $157.3 billion, including term debt, operating leases, manufacturing purchase obligations, and other purchase obligations.
    - The company did not enter into any significant off-balance sheet arrangements.
    """)

elif selected_company=='Amazon' :
    st.write("To be updated soon")
