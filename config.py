from os import path, environ
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env')) # koda erişimi olan herhangi bir kişinin görüntülememesi gereken SECRET_KEY
                                        # gibi bilgiler .env dosyasında saklanır. Localde çalışırken bu satırın aktif olması gerekir.
                                        # Productionda bu satır kaldırılır, keyler digitalocean enviromentta saklanır.

class Config(object):
    # Flask configure etmek için gerekli sınıf. İçerisinde keyler, pathler 
    # ve session_time gibi parametreler bulundurabilir.
    SECRET_KEY = environ.get('SECRET_KEY')