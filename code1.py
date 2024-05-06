import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop

# Đường dẫn đến thư mục chứa dữ liệu huấn luyện trên máy tính của bạn
train_image_files_path = "C:\\Users\\ADM\\Desktop\\chuso"

# Các nhãn của dữ liệu
label = ['số 0','số 1','số 2', 'số 3','số 4', 'số 5', 'số 6', 'số 7', 'số 8', 'số 9']

# Tạo generator từ dữ liệu ảnh
train_data_gen = ImageDataGenerator(rescale=1/255)
train_generator = train_data_gen.flow_from_directory(
    train_image_files_path,
    target_size=(50,50),
    class_mode='categorical'
)

# Xây dựng mô hình
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='softmax')  # Số lượng lớp đầu ra phải là 10 (số nhãn)
])

# Compile mô hình
model.compile(optimizer=RMSprop(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['acc'])

# Số lượt lặp lại (epochs)
EPOCHS = 100

# Huấn luyện mô hình
history = model.fit(
    train_generator,
    steps_per_epoch=2,
    epochs=EPOCHS,
    verbose=1
)

# Lưu mô hình
model.save("hoa_model.h5")