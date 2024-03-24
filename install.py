from nomeroff_net import pipeline


# Скачивает модели и тд.тп, далее при запуске не нужно этого повтрно делать
pipeline(
    'number_plate_detection_and_reading',
    image_loader='opencv',
)
