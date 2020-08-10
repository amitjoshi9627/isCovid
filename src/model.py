import config
import dataset
import utils
import config
from tensorflow.keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout
from tensorflow.keras.models import Sequential


class CovidModel:

    def __init__(self):
        self.model = Sequential()

        self.model.add(Conv2D(32, kernel_size=(3, 3),
                              activation="relu", input_shape=config.INPUT_SHAPE))
        self.model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(128, kernel_size=(3, 3), activation="relu"))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(256, kernel_size=(3, 3), activation="relu"))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(64, activation="relu"))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(1, activation="sigmoid"))

        self.model.compile(
            loss=config.LOSS, optimizer=config.OPTIMIZER, metrics=["accuracy"])

        self.model.summary()

    def train(self):

        self.model.fit_generator(dataset.train_generator, steps_per_epoch=config.STEPS_PER_EPOCH,
                                 epochs=config.EPOCHS, validation_data=dataset.val_generator, validation_steps=config.VALIDATION_STEPS)
        utils.save(self.model)