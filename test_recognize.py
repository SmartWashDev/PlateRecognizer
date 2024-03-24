from pathlib import Path

from nomeroff_net.pipelines.number_plate_detection_and_reading import NumberPlateDetectionAndReading
from nomeroff_net.tools import unzip


plate_detector = NumberPlateDetectionAndReading(
    task='number_plate_detection_and_reading_trt',
    image_loader='opencv',
    options={
        'class_region': [
            'ru',
        ]
    },
    default_label='ru',
)

test_images_path = Path('test_images')
for file in test_images_path.iterdir():
    expected_plate_number = file.name.split('.')[0]

    (*_, plate_number) = unzip(plate_detector([str(file)]))

    try:
        plate_number = plate_number[0][0]
    except KeyError:
        raise AssertionError(f'Not detected plates on image {file}')

    assert expected_plate_number == plate_number, plate_number

print('Test success')
