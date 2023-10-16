import os
import requests
import pytesseract
from PIL import Image
class tex:
    def texx(self):

        path="C:\\Users\\Aditya\\Downloads\\image-upload-react-django-master\\image-upload-react-django-master\\imguploaddjango\\images\\images"
        allfiles=os.listdir(path)
        print(allfiles)
        files=[file for file in allfiles  if os.path.isfile(os.path.join(path, file)) ]
        print(files)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)
        target=os.path.join(path,files[0])

    # target=files[0]



        img = Image.open(str(target))


        text = pytesseract.image_to_string(img)

        text+="extracted"
        url = 'http://localhost:8000/text-endpoint/'  # Replace with the actual endpoint URL
        data = {'text_data': text}

        response = requests.post(url, data=data)

        print(response.status_code)
        print(response.json())
        
# a=tex()
# a.texx()
