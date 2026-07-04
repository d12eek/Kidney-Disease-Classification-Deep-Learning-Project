import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = tf.saved_model.load(
            os.path.join("artifacts", "training", "saved_model")
        )
        infer = model.signatures["serving_default"]

        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0
        test_tensor = tf.constant(test_image, dtype=tf.float32)

        predictions = infer(test_tensor)
        output = list(predictions.values())[0].numpy()
        result = np.argmax(output, axis=1)

        if result[0] == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [{"image": prediction}]