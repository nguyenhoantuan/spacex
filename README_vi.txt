KẾT QUẢ THỰC THI 01/10/2026
Đã chạy: kiểm tra nhãn/thiếu, EDA, 10 SQL queries, 4 mô hình GridSearchCV, hình và HTML Plotly.
Mô hình chọn theo CV: Decision tree. Confusion matrix: [[3, 3], [0, 12]].
Protocol: 83 đặc trưng từ Part 3; 80/20 stratify=Class random_state=2; scaler nằm trong 10-fold CV. Tree grid giảm (xem mã), max_features auto thay bằng None/sqrt. Accuracy không nhất thiết trùng protocol notebook khóa học.
Các bảng SQL strip khoảng trắng; truy vấn NASA dùng Customer LIKE '%NASA%' và F9 v1.1 dùng prefix. Part 1/2/3, SQL, Dash/Geo khác phạm vi; không gộp.

ĐẶT CẢ 6 CSV NGƯỜI DÙNG VÀO CÙNG THƯ MỤC VỚI MÃ.
Cài: pip install pandas numpy scikit-learn matplotlib seaborn plotly nbformat python-pptx dash folium
Phân tích: python run_analysis.py (xuất bảng vào results).
Dashboard: python spacex_dash_app.py (port 8050).
Folium: python build_folium_map.py (cần Internet cho tiles khi mở HTML).
interactive_dashboard.html là Plotly view offline, không phải Dash server.

GIỚI HẠN:
Không có Folium/Dash và executable browser trong môi trường hiện tại; mã 2 ứng dụng được kiểm tra cú pháp nhưng chưa chạy. Hình slides là static analytical views, KHÔNG phải screenshot trình duyệt.
API/web scraping không thực thi; không có HTML Wikipedia hoặc notebook API hoàn chỉnh. CSV đầu vào do người dùng cung cấp.
Khoảng cách chỉ tới điểm ví dụ trong notebook, chưa xác minh coastline gần nhất; chưa đo railway/highway.
Tên tác giả/GitHub URL chưa được cung cấp. Cần thêm nếu yêu cầu nộp bài đòi hỏi.
Notebook kèm có outputs của phần đã thực thi và hình được tạo thực tế; không giả outputs của notebook gốc.
