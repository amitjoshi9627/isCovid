from tensorflow.keras.losses import binary_crossentropy

LOSS = binary_crossentropy
OPTIMIZER = "adam"
INPUT_SHAPE = (256, 256, 3)

TARGET_SIZE = (256, 256)
BATCH_SIZE = 32
EPOCHS = 20

STEPS_PER_EPOCH = 8
VALIDATION_STEPS = 2

TRAIN_PATH = "../data/train"
VAL_PATH = "../data/val"
TEST_PATH = "../data/test"
MODEL_PATH = "../saved_model/CovidClassifierModel.h5"
