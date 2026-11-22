# Bài thực hành 5 — Tự động hóa sáng tạo và quản lý nội dung số

## Mục tiêu
1. Đọc dữ liệu CSV, xử lý bằng pandas, vẽ biểu đồ bằng matplotlib và sinh PDF bằng ReportLab.
2. Đọc nội dung Markdown/TXT, tạo slide PowerPoint bằng python-pptx (các text box chỉnh sửa được).

Dữ liệu mẫu Wine: https://archive.ics.uci.edu/dataset/109/wine — 178 mẫu, 13 đặc trưng, 3 lớp. Sử dụng lại CSV từ bài thực hành 6.

## Cách chạy bằng VS Code trên Mac
1. Mở thư mục `BT5_Tu_dong_hoa_noi_dung` (có file `run_all.py`).
2. Mở terminal tại thư mục này, chạy:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

3. Trong VS Code chọn interpreter `.venv/bin/python` (Command+Shift+P → Python: Select Interpreter).
4. Mở `run_all.py` rồi nhấn nút **Run Python File**. Hoặc lệnh `python run_all.py`.
5. Lấy file tại `results/`.

## Đổi dữ liệu và nội dung
- Thay `data/wine_uci.csv` bằng CSV của bạn (giữ tên file) hoặc chạy `python src/csv_to_pdf.py /duong/dan/du_lieu.csv`.
- Sửa `input/noi_dung_thuyet_trinh.md` theo cấu trúc `# tiêu đề`, `## tiêu đề slide`, `- ý chính`. Chạy lại `run_all.py`.
- Có thể dùng file `.txt` nếu nội dung vẫn có `##` để chia slide.

## Các sản phẩm
- `results/Bao_cao_tu_dong_tu_CSV.pdf`: Báo cáo tự động, có tiêu đề, mô tả, bảng thống kê, 2 biểu đồ, kết luận.
- `results/Slide_tu_dong_tu_van_ban.pptx`: Slide tự động từ Markdown, có tiêu đề, bullet và hình minh họa.
- `results/du_lieu_sau_xu_ly.csv`: Dữ liệu sau làm sạch.
- `results/bieu_do_phan_bo.png`, `results/bieu_do_so_sanh.png`: Hình minh họa.

## Minh chứng đề xuất cho báo cáo Word
1. Chụp thư mục `data/` và `input/` (đầu vào).
2. Chụp terminal chạy `run_all.py` hiện “HOÀN THÀNH”.
3. Chèn ảnh PDF trang có biểu đồ; chụp slide PowerPoint.
4. Chụp thư mục `results/` chứa PDF và PPTX.
