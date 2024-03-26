import tensorflow as tf
from tensorflow.keras import layers

def create_model(input_shape, num_classes):
    """
    Create a deep learning model for image classification.
    :param input_shape: The input shape of images.
    :param num_classes: Number of output classes.
    :return: A compiled and ready-to-train TensorFlow Keras Model.
    """

    inputs = layers.Input(shape=input_shape)

    # Block 1
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)

    # Block 2
    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)

    x = layers.Flatten()(x)

    # Fully Connected Layers
    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.Model(inputs, x, name="image_classifier")

    # Compile the Model
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=['accuracy']
    )

    return model

def main():
    input_shape = (224, 224, 3)
    num_classes = 10

    model = create_model(input_shape, num_classes)

    # Training and testing the model can be implemented here
    # ...

if __name__ == "__main__":
    main()
