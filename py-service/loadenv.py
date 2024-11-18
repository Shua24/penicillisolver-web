# Kode hanya untuk mempersiapkan koneksi ke database
# Kode pasti menunggu login/register dan atur akses.
# Kode juga menunggu pengaturan database Firebase.

from dotenv import load_dotenv
import os

load_dotenv('../.env')

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')