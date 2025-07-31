# utils/file_handler.py

from typing import Union
import io

def read_email_content(text_input: str = "", file_input: Union[io.BytesIO, None] = None) -> str:
    """
    Kullanıcının girdiği metni veya yüklediği .txt dosyasını okuyarak e-posta içeriğini döner.
    
    :param text_input: TextArea'dan gelen yazılı içerik.
    :param file_input: Yüklenen .txt dosyası (BytesIO şeklinde).
    :return: E-posta metni (str)
    """
    if file_input is not None:
        return file_input.read().decode("utf-8")
    
    elif text_input.strip() != "":
        return text_input.strip()
    
    else:
        return "E-posta metni girilmedi."
