from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Website(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=500, blank=False, null=False)
    qrcode = models.ImageField(upload_to='qr_codes', blank=True, null=True)

    def __str__(self):
        return str(self.nome)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.url)
        canvas = Image.new('RGB', (400, 400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.nome}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

