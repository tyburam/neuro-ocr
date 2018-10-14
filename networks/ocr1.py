from keras import layers, models


class OcrNetwork1:
    def __init__(self):
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(320, 240, 3)))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.Reshape((76, 3584)))
        self.model.add(layers.Bidirectional(layers.GRU(128, return_sequences=True)))
        self.model.add(layers.Bidirectional(layers.GRU(32, return_sequences=True)))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(11, activation='softmax'))

        print(self.model.summary())

    def train(self, x_train, y_train, epochs=5, batch_size=64):
        self.model.compile(optimizer='rmsprop',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

    def evaluate(self, x_test, test_labels):
        self.model.evaluate(x_test, test_labels)
