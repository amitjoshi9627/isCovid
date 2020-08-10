import config
from tensorflow.keras.preprocessing import image

train_datagen = image.ImageDataGenerator(
    rescale=1/255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
val_datagen = image.ImageDataGenerator(rescale=1/255)

train_generator = train_datagen.flow_from_directory(
    config.TRAIN_PATH, target_size=config.TARGET_SIZE, class_mode="binary", batch_size=config.BATCH_SIZE)
val_generator = val_datagen.flow_from_directory(
    config.VAL_PATH, target_size=config.TARGET_SIZE, class_mode="binary", batch_size=config.BATCH_SIZE)
