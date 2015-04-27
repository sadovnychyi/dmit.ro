import json
import base64
import time
import main
from google.appengine.api import images
from google.appengine.api import files


class Img(main.BaseHandler):
  def get(self):
    return self.render('img.html')

  def post(self):
    img = self.request.get('img')
    img = img.replace('data:image/png;base64,', '')

    image = images.Image(base64.b64decode(img))
    image.resize(width=1600, height=1600)
    height = image.height
    width = image.width
    image = image.execute_transforms(output_encoding=images.PNG)

    size = max(height, width) if max(height, width) < 1600 else 1600

    file_name = files.blobstore.create(
      mime_type='image/png',
      _blobinfo_uploaded_filename=str(int(time.time())))
    with files.open(file_name, 'a') as f:
      f.write(image)
    files.finalize(file_name)
    blob_key = files.blobstore.get_blob_key(file_name)

    img_url = images.get_serving_url(blob_key, size=size, secure_url=True)
    response = {'url': img_url}
    return self.response.write(json.dumps(response))
