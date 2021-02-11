from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS

def get_decimal_coordinates(info):
    try:
        latitud = 0;

        lat_hemisferio = info[1]
        lat_coordenadas = info[2]
        lat_grados = lat_coordenadas[0]
        lat_minutos = lat_coordenadas[1]
        lat_segundos = lat_coordenadas[2]
        #print(lat_hemisferio)
        #print(lat_coordenadas)
        #print(lat_grados)
        #print(lat_minutos)
        #print(lat_segundos)

        latitud = (float(lat_grados) + ((float(lat_minutos) / 60)+(float(lat_segundos)/3600)))

        if lat_hemisferio == 'S':
            latitud = latitud * -1

        longitud = 0;

        lon_hemisferio = info[3]
        lon_coordenadas = info[4]
        lon_grados = lon_coordenadas[0]
        lon_minutos = lon_coordenadas[1]
        lon_segundos = lon_coordenadas[2]
        #print(lon_hemisferio)
        #print(lon_coordenadas)
        #print(lon_grados)
        #print(lon_minutos)
        #print(lon_segundos)

        longitud = (float(lon_grados) + ((float(lon_minutos) / 60) + (float(lon_segundos)/3600)))

        if lon_hemisferio == 'W':
            longitud = longitud * -1

        return [latitud, longitud]
    except Exception as e:
        print('Fail')
        print(e)
        return None


def get_exif(filename):
    try:
        exif = Image.open(filename)._getexif()
        if exif is not None:
            print(exif[34853])

        return exif[34853]

    except:
        print('Fail')
        return None

if __name__ == '__main__':
    sfilepath = "images/image01.jpg"
    exif = get_exif(sfilepath)
    #print(exif)

    #exif_print(sfilepath)
    lat, lon = get_decimal_coordinates(exif)
    print("%s,%s" % (lat, lon))


