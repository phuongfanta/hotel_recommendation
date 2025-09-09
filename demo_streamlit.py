import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Using menu
st.title("Trung Tâm Tin Học")
menu = ["Home", "Capstone Project", "Sử dụng các điều khiển", "Gợi ý điều khiển project 1", "Gợi ý điều khiển project 2"]
choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Home':    
    st.subheader("[Trang chủ](https://csc.edu.vn)")  
elif choice == 'Capstone Project':    
    st.subheader("[Đồ án TN Data Science](https://csc.edu.vn/data-science-machine-learning/Do-An-Tot-Nghiep-Data-Science---Machine-Learning_229)")
    st.write("""### Có 2 chủ đề trong khóa học:    
    - Topic 1: Customer Clustering
    - Topic 2: Recommender System
             """)
    # hiển thị các hình ảnh liên quan đến đồ án
    st.image("RFM_clustering.png", width=400, caption="Customer Clustering")
    st.image("recommend.jpg", width=400, caption="Recommender System")
    
elif choice == 'Sử dụng các điều khiển':
    # Sử dụng các điều khiển nhập
    # 1. Text
    st.subheader("1. Text")
    name = st.text_input("Enter your name")
    st.write("Your name is", name)
    # 2. Slider
    st.subheader("2. Slider")
    age = st.slider("How old are you?", 1, 100, 20)
    st.write("I'm", age, "years old.")
    # 3. Checkbox
    st.subheader("3. Checkbox")
    if st.checkbox("I agree"):
        st.write("Great!")
    # 4. Radio
    st.subheader("4. Radio")
    status = st.radio("What is your status?", ("Active", "Inactive"))
    st.write("You are", status)
    # 5. Selectbox
    st.subheader("5. Selectbox")
    occupation = st.selectbox("What is your occupation?", ["Student", "Teacher", "Others"])
    st.write("You are a", occupation)
    # 6. Multiselect
    st.subheader("6. Multiselect")
    location = st.multiselect("Where do you live?", ("Hanoi", "HCM", "Danang", "Hue"))
    st.write("You live in", location)
    # 7. File Uploader
    st.subheader("7. File Uploader")
    file = st.file_uploader("Upload your file", type=["csv", "txt"])
    if file is not None:
        st.write(file)    
    # 9. Date Input
    st.subheader("9. Date Input")
    date = st.date_input("Pick a date")
    st.write("You picked", date)
    # 10. Time Input
    st.subheader("10. Time Input")
    time = st.time_input("Pick a time")
    st.write("You picked", time)
    # 11. Display JSON
    st.subheader("11. Display JSON")
    json = st.text_input("Enter JSON", '{"name": "Alice", "age": 25}')
    st.write("You entered", json)
    # 12. Display Raw Code
    st.subheader("12. Display Raw Code")
    code = st.text_area("Enter code", "print('Hello, world!')")
    st.write("You entered", code)
    # Sử dụng điều khiển submit
    st.subheader("Submit")
    submitted = st.button("Submit")
    if submitted:
        st.write("You submitted the form.")
        # In các thông tin phía trên khi người dùng nhấn nút Submit
        st.write("Your name is", name)
        st.write("I'm", age, "years old.")
        st.write("You are", status)
        st.write("You are a", occupation)
        st.write("You live in", location)
        st.write("You picked", date)
        st.write("You picked", time)
        st.write("You entered", json)
        st.write("You entered", code)
          
elif choice == 'Gợi ý điều khiển project 1':
    def customer_clustering(R_value, F_value, M_value):
        if R_value >= 3 and F_value >= 3 and M_value >= 3:
            st.write("Khách hàng thuộc nhóm VIP")
        elif R_value >= 3 and F_value >= 2 and M_value >= 2:
            st.write("Khách hàng thuộc nhóm Loyal")
        elif R_value >= 2 and F_value >= 2 and M_value >= 2:
            st.write("Khách hàng thuộc nhóm Potential")
        elif R_value <=1 and F_value <= 1 and M_value <= 1:
            st.write("Khách hàng thuộc nhóm Lost")
        else:
            st.write("Khách hàng thuộc nhóm New")

    st.write("Curomer Clustering")
    # Trường hợp 1: Nhập 1 khách hàng
    st.write("### Nhập 1 khách hàng")
    # Cho người dùng chọn giá trị R, F, M 1..4  (lưu ý đây chỉ là ví dụ đơn giản, trong thực tế R, F, M có thể là giá trị khác)      
    R_value = slider = st.slider("Select R value", 1, 4, 1)
    F_value = slider = st.slider("Select F value", 1, 4, 1)
    M_value = slider = st.slider("Select M value", 1, 4, 1)
    # Dựa trên 3 giá trị R, F, M để phân loại khách hàng vào các nhóm    
    if st.button("Phân loại khách hàng"):
        customer_clustering(R_value, F_value, M_value)

    # Trường hợp 2: Đọc dữ liệu từ file csv
    st.write("### Hoặc đọc dữ liệu từ file csv")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Dữ liệu đã nhập:")
        st.dataframe(df)
        if st.button("Phân loại khách hàng từ file"):
            # Hiển thị kết quả ra dataframe
            st.write("Kết quả phân loại khách hàng:")
            result = []
            for index, row in df.iterrows():
                R_value = row['R']
                F_value = row['F']
                M_value = row['M']
                if R_value >= 3 and F_value >= 3 and M_value >= 3:
                    result.append("VIP")
                elif R_value >= 3 and F_value >= 2 and M_value >= 2:
                    result.append("Loyal")
                elif R_value >= 2 and F_value >= 2 and M_value >= 2:
                    result.append("Potential")
                elif R_value <=1 and F_value <= 1 and M_value <= 1:
                    result.append("Lost")
                else:
                    result.append("New")
            df['Customer Segment'] = result
            st.dataframe(df)

            # st.write("Kết quả phân loại khách hàng theo dòng:")
            # for index, row in df.iterrows():
            #     R_value = row['R']
            #     F_value = row['F']
            #     M_value = row['M']
            #     st.write(f"Khách hàng {index+1}: R={R_value}, F={F_value}, M={M_value} --> ", end="")
            #     customer_clustering(R_value, F_value, M_value)

elif choice=='Gợi ý điều khiển project 2':
    st.write("##### Gợi ý điều khiển project 2: Recommender System")
    st.write("##### Dữ liệu mẫu")
    # Tạo dataframe có 3 cột là Id, CompanyName, CompanyInfo
    data = {
        'Id': [1, 2, 3, 4, 5],
        'CompanyName': ['Mường Thanh', 'Alpha Bird', 'Panorama', 'Balcony Nha Trang', 'Megalight'],
        'CompanyInfo': ['Khách sạn Mường Thanh Luxury Nha Trang 5 sao hiện đại', 'Khách sạn Alpha Bird 4 sao sang trọng', 
                        'Khách sạn Panorama 5 sao trung tâm', 'Khách sạn Balcony Nha Trang 4 sao trung tâm', 'Khách sạn Megalight 3 sao mới mẻ']
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.write("### 1. Tìm kiếm khách sạn tương tự")
    # Tạo điều khiển để người dùng chọn công ty
    selected_company = st.selectbox("Chọn khách sạn", df['CompanyName'])
    st.write("Khách sán đã chọn:", selected_company) 
    # Từ khách sạn đã chọn này, người dùng có thể xem thông tin chi tiết của khách sạn
    # hoặc thực hiện các xử lý khác
    # tạo điều khiển để người dùng tìm kiếm công ty dựa trên thông tin người dùng nhập
    search = st.text_input("Nhập thông tin tìm kiếm")
    # Tìm kiếm khách sạn dựa trên thông tin người dùng nhập vào search, chuyển thành chữ thường trước khi tìm kiếm
    result = df[df['CompanyInfo'].str.lower().str.contains(search.lower())]    
    # In danh sách khách sạn tìm được ra màn hình     
    st.write("Danh sách khách sạn tìm được:")
    st.dataframe(result)

    st.write("### 2. Recommend or Not")

    # Tạo một điều khiển combobox để người dùng chọn khách sạn, một lần chỉ chọn được một khách sạn
    selected_company_info = st.selectbox("Chọn khách sạn để xem thông tin chi tiết", df['CompanyName'])
    # Lấy thông tin chi tiết của khách sạn đã chọn
    company_info = df[df['CompanyName'] == selected_company_info]
    # Tạo 1 radio button list để người dùng chọn điểm số từ 1 đến 5 cho Vị trí, Giá cả, Dịch vụ, Chất lượng
    location = st.radio("Chọn điểm số cho Vị trí", [1, 2, 3, 4, 5], horizontal=True)

    price = st.radio("Chọn điểm số cho Giá cả", [1, 2, 3, 4, 5], horizontal=True)

    service = st.radio("Chọn điểm số cho Dịch vụ", [1, 2, 3, 4, 5], horizontal=True)

    quality = st.radio("Chọn điểm số cho Chất lượng", [1, 2, 3, 4, 5], horizontal=True)    

    # Tạo một button để người dùng submit các thông tin đã chọn
    submit = st.button("Submit")
    # Giả sử điểm trung bình của các lựa chọn >=4 thì sẽ hiển thị thông báo "Recommend", ngược lại sẽ hiển thị thông báo "Not Recommend"
    if submit:
        st.write("Khách sạn đã chọn:", selected_company_info)
        st.write("Thông tin chi tiết khách sạn:", company_info['CompanyInfo'].values[0])
        # Tính điểm trung bình của các điểm số đã chọn
        average_score = (location + price + service + quality) / 4
        # Hiển thị điểm trung bình
        st.write("Điểm trung bình của các điểm số đã chọn là:", average_score)
        # Hiển thị thông báo Recommend or Not
        if average_score >= 3.5:
            st.write("#### -> Recommend")
        else:
            st.write("#### -> Not Recommend")
        
        # vẽ biểu đồ cột thể hiện điểm số của từng lựa chọn        
        scores = {
            'Vị trí': location,
            'Giá cả': price,
            'Dịch vụ': service,
            'Chất lượng': quality
        }
        scores_df = pd.DataFrame(list(scores.items()), columns=['Category', 'Score'])
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Category', y='Score', data=scores_df, palette='viridis')
        plt.title('Scores for ' + selected_company_info)
        plt.xticks(rotation=45)
        st.pyplot(plt)   
# Done
    
    
    
        

        
        

    



