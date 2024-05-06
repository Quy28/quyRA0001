import cv2
import numpy as np
import time
import tensorflow as tf

# Tạo một hình ảnh trắng có kích thước 360x500 px
canvas = np.ones((500, 360), dtype="uint8") * 255

# Tạo một biến để theo dõi sự thay đổi của chuột
drawing = False

# Hàm callback khi sự kiện chuột di chuyển được kích hoạt
def draw(event, x, y, flags, param):
    global drawing

    # Khi chuột được nhấn
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    # Khi chuột được di chuyển
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(canvas, (x, y), 8, (0, 0, 0), -1)
    # Khi chuột được nhả ra
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Tạo một cửa sổ và gán hàm callback cho sự kiện chuột
cv2.namedWindow("Canvas", cv2.WINDOW_NORMAL)  # Thêm cv2.WINDOW_NORMAL để có thể thay đổi kích thước cửa sổ
cv2.setMouseCallback("Canvas", draw)

# Load mô hình đã được huấn luyện
model = tf.keras.models.load_model("hoa_model.h5")

# Một số nhãn tương ứng với các lớp trong mô hình
labels = ['số 0', 'số 1', 'số 2', 'số 3', 'số 4', 'số 5', 'số 6', 'số 7', 'số 8', 'số 9']

while True:
    # Hiển thị bảng viết
    cv2.imshow("Canvas", canvas)

    # Chờ người dùng ấn phím
    key = cv2.waitKey(1) & 0xFF

    # Nếu người dùng ấn phím 'q', thoát chương trình
    if key == ord("q"):
        break
    # Nếu người dùng ấn phím 'o' (ok)
    elif key == ord("o"):
        # Chụp lại màn hình của bảng viết
        cv2.imwrite("written_image.png", canvas)

        # Đọc ảnh từ tệp đã chụp và chuyển đổi thành ảnh grayscale
        written_image = cv2.imread("written_image.png", cv2.IMREAD_GRAYSCALE)

        # Resize ảnh thành kích thước 50x50
        written_image_resized = cv2.resize(written_image, (50, 50))

        # Mở rộng chiều của ảnh để phù hợp với định dạng của đầu vào của mô hình và mở rộng kênh màu
        written_image_expanded = np.expand_dims(written_image_resized, axis=0)
        written_image_expanded = np.expand_dims(written_image_expanded, axis=-1)
        written_image_expanded = np.tile(written_image_expanded, (1, 1, 1, 3))  # Copy kênh màu để tạo thành ảnh RGB

        # Tiến hành tiên đoán ảnh chữ viết đã được chụp
        prediction = model.predict(written_image_expanded)
        predicted_label = labels[np.argmax(prediction)]

        # In ra kết quả tiên đoán
        print("Kết quả tiên đoán:", predicted_label)

        # Hiển thị màn hình trong 5 giây
        time.sleep(5)

        # Reset bảng viết
        canvas.fill(255)

# Đóng cửa sổ khi kết thúc chương trình
cv2.destroyAllWindows()
