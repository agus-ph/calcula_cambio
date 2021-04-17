import requests
import json

"""
Este modulo consume una api y devuelve el valor
del tipo de cambio del dolar oficial y blue
"""

url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"

response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()
    # -------- Dolar Oficial ----------
    def dolaroficial_compra():
        """
        Devuelve el valor del tipo de cambio oficial para la compra
        """
        oficial = response_json[0]
        casa_oficial = oficial["casa"]
        compra_oficial = casa_oficial["compra"]
        return compra_oficial

    def dolaroficial_venta():
        """
        Devuelve el valor del tipo de cambio oficial para la venta
        """
        oficial = response_json[0]
        casa_oficial = oficial["casa"]
        venta_oficial = casa_oficial["venta"]
        return venta_oficial

    # ----------- Dolar Blue ------------
    def dolarblue_compra():
        """
        Devuelve el valor del tipo de cambio blue para la compra
        """
        blue = response_json[1]
        casa_blue = blue["casa"]
        compra_blue = casa_blue["compra"]
        return compra_blue

    def dolarblue_venta():
        """
        Devuelve el valor del tipo de cambio oficial para la venta
        """
        blue = response_json[1]
        casa_blue = blue["casa"]
        venta_blue = casa_blue["venta"]
        return venta_blue
