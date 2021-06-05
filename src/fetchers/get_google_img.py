from simple_image_download import simple_image_download as simp

class GetGoogleImg:

    def __init__(self, img_key):

        response = simp.simple_image_download
        # try to get author's photo from google graphics
        response().download(img_key, 1)