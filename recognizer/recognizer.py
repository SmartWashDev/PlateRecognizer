from nomeroff_net.pipelines.number_plate_detection_and_reading import NumberPlateDetectionAndReading
from nomeroff_net.tools import unzip

from recognizer.exceptions import NotAvailableRegion, NotDetectedPlatesOnImage


class PlateNumberRecognizer:
    default_available_regions: set[str] = {'ru'}

    def __init__(self, available_regions: set[str] | None = None):
        self.available_regions = available_regions or self.default_available_regions

        self._plate_reading_detector = NumberPlateDetectionAndReading(
            task='number_plate_detection_and_reading_trt',
            image_loader='opencv',
        )

    def get_plate_number(self, image) -> str:
        (
            images,
            images_bboxs,
            images_points,
            images_zones,
            region_ids,
            region_names,
            count_lines,
            confidences,
            plate_numbers,
        ) = unzip(self._plate_reading_detector([image]))

        plate_number = self._validate_plate_numbers(plate_numbers[0])
        self._validate_region_names(region_names[0])

        return plate_number

    def _validate_plate_numbers(self, plate_numbers: list[str]):
        try:
            plate_number = plate_numbers[0]
        except KeyError:
            raise NotDetectedPlatesOnImage('На изображение не найдено изображения')
        return plate_number

    def _validate_region_names(self, region_names: list[str]):
        region_name = region_names[0]
        if region_name not in self.available_regions:
            raise NotAvailableRegion(f'Регион {region_name} недоступен')
        return region_name
