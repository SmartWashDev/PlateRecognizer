class RecognizerError(Exception):
    pass


class NotDetectedPlatesOnImage(RecognizerError):
    pass


class NotAvailableRegion(RecognizerError):
    pass
